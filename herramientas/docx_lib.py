"""Utilidades para leer y editar .docx a nivel de XML sin perder el formato.

Uso típico:
    import docx
    from docx_lib import parrafos, reemplazar, reemplazar_parrafo, resaltar_tramo
    d = docx.Document('entrada.docx')
    for p in parrafos(d):
        print(p['i'], p['seccion'], p['texto'][:80])
    reemplazar(p['el'], 'texto viejo', 'texto nuevo')   # marca en cian
    d.save('salida.docx')
"""
import copy
import re

NS_W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'


def W(tag):
    return '{%s}%s' % (NS_W, tag)


def texto(p_el):
    """Texto visible de un párrafo (w:p), incluidos tabs."""
    out = []
    for el in p_el.iter():
        if el.tag == W('t'):
            out.append(el.text or '')
        elif el.tag == W('tab'):
            out.append('\t')
        elif el.tag in (W('br'), W('cr')):
            out.append('\n')
    return ''.join(out)


def estilo(p_el):
    ppr = p_el.find(W('pPr'))
    if ppr is not None and ppr.find(W('pStyle')) is not None:
        return ppr.find(W('pStyle')).get(W('val'))
    return ''


def es_titulo(p_el, t):
    st = estilo(p_el).lower()
    if 'heading' in st or 'ttulo' in st or 'titulo' in st:
        return True
    return bool(re.match(r'^\s*([IVX]+\.|\d+(\.\d+)*\.?)\s+\S', t)) and len(t.split()) <= 14


def parrafos(doc):
    """Lista de párrafos del cuerpo (incluye celdas de tablas) con su sección."""
    out, seccion = [], ''
    for i, el in enumerate(doc.element.body.iter(W('p'))):
        t = texto(el)
        en_tabla = any(a.tag == W('tbl') for a in el.iterancestors())
        if t.strip() and not en_tabla and es_titulo(el, t.strip()):
            seccion = t.strip()[:80]
        out.append({'i': i, 'el': el, 'texto': t, 'estilo': estilo(el),
                    'en_tabla': en_tabla, 'seccion': seccion})
    return out


def _runs_con_texto(p_el):
    """[(run, t_el, inicio, fin)] en orden, con offsets sobre texto(p)."""
    res, pos = [], 0
    for r in p_el.iter(W('r')):
        for el in r:
            if el.tag == W('t'):
                n = len(el.text or '')
                res.append((r, el, pos, pos + n))
                pos += n
            elif el.tag == W('tab'):
                pos += 1
            elif el.tag in (W('br'), W('cr')):
                pos += 1
    return res


def _set_highlight(run, color):
    rpr = run.find(W('rPr'))
    if rpr is None:
        rpr = run.makeelement(W('rPr'), {})
        run.insert(0, rpr)
    h = rpr.find(W('highlight'))
    if h is None:
        h = rpr.makeelement(W('highlight'), {})
        rpr.append(h)
    h.set(W('val'), color)


def _partir_run(run, t_el, corte):
    """Parte un run en dos en la posición `corte` de su w:t. Devuelve el run derecho."""
    txt = t_el.text or ''
    nuevo = copy.deepcopy(run)
    for el in list(nuevo):
        if el.tag != W('rPr'):
            nuevo.remove(el)
    t2 = nuevo.makeelement(W('t'), {})
    t2.text = txt[corte:]
    t2.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
    nuevo.append(t2)
    t_el.text = txt[:corte]
    t_el.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
    run.addnext(nuevo)
    return nuevo


def resaltar_tramo(p_el, inicio, fin, color='yellow'):
    """Resalta los caracteres [inicio, fin) del párrafo sin cambiar el texto."""
    if fin <= inicio:
        return
    # partir en los bordes
    for borde in (fin, inicio):
        for r, t_el, a, b in _runs_con_texto(p_el):
            if a < borde < b:
                _partir_run(r, t_el, borde - a)
                break
    for r, t_el, a, b in _runs_con_texto(p_el):
        if a >= inicio and b <= fin and b > a:
            _set_highlight(r, color)


def rangos_protegidos(p_el):
    """Tramos [ini, fin) del texto que son resultado de un campo (citas, referencias, PAGEREF)."""
    rangos, pos, prof, inicio = [], 0, 0, None
    for el in p_el.iter():
        if el.tag == W('fldChar'):
            tipo = el.get(W('fldCharType'))
            if tipo == 'begin':
                if prof == 0:
                    inicio = pos
                prof += 1
            elif tipo == 'end' and prof:
                prof -= 1
                if prof == 0:
                    rangos.append((inicio, pos))
        elif el.tag == W('t'):
            pos += len(el.text or '')
        elif el.tag in (W('tab'), W('br'), W('cr')):
            pos += 1
    return rangos


def reemplazar_tramo(p_el, ini, fin, nuevo, color='cyan'):
    """Reemplaza los caracteres [ini, fin) del párrafo por `nuevo` (fin == ini inserta)."""
    for borde in (fin, ini):
        for r, t_el, a, b in _runs_con_texto(p_el):
            if a < borde < b:
                _partir_run(r, t_el, borde - a)
                break
    runs = _runs_con_texto(p_el)
    afectados = [(r, t_el) for r, t_el, a, b in runs if a >= ini and b <= fin and b > a]
    if not afectados:
        if not nuevo:
            return True
        # inserción: nuevo run después del que termina en `ini` (o antes del primero)
        previo = [x for x in runs if x[3] == ini and x[3] > x[2]]
        base, t_base = (previo[-1][0], previo[-1][1]) if previo else (runs[0][0], runs[0][1])
        nuevo_run = copy.deepcopy(base)
        for el in list(nuevo_run):
            if el.tag != W('rPr'):
                nuevo_run.remove(el)
        t2 = nuevo_run.makeelement(W('t'), {})
        t2.text = nuevo
        t2.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
        nuevo_run.append(t2)
        if color:
            _set_highlight(nuevo_run, color)
        if previo:
            base.addnext(nuevo_run)
        else:
            base.addprevious(nuevo_run)
        return True
    primero, t_primero = afectados[0]
    if nuevo:
        t_primero.text = nuevo
        t_primero.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
        if color:
            _set_highlight(primero, color)
        resto = afectados[1:]
    else:
        resto = afectados
    for r, t_el in resto:
        t_el.getparent().remove(t_el)
        if not any(c.tag in (W('t'), W('tab'), W('br'), W('drawing'), W('fldChar'), W('instrText')) for c in r) \
                and r.getparent() is not None:
            r.getparent().remove(r)
    return True


_RX_TOK = re.compile(r'\s+|\w+|[^\w\s]', re.UNICODE)


def aplicar_texto(p_el, nuevo, color='cyan', permitir_campos=False):
    """Lleva el párrafo a `nuevo` cambiando solo las palabras distintas (resaltadas).

    Las citas y demás campos de Word deben quedar idénticos en `nuevo`; si un
    cambio los toca, lanza ValueError y no modifica nada.
    Con `permitir_campos=True` se edita aunque el texto esté dentro del resultado
    de un campo (útil cuando el autor escribió texto propio dentro de una cita).
    Devuelve la lista de cambios [(antes, después)].
    """
    from difflib import SequenceMatcher
    viejo = texto(p_el)
    if viejo == nuevo:
        return []
    ta, tb = _RX_TOK.findall(viejo), _RX_TOK.findall(nuevo)
    oa = [0]
    for t in ta:
        oa.append(oa[-1] + len(t))
    ops = []
    for op, a1, a2, b1, b2 in SequenceMatcher(None, ta, tb, autojunk=False).get_opcodes():
        if op != 'equal':
            ops.append([oa[a1], oa[a2], ''.join(tb[b1:b2])])
    # unir cambios separados solo por un espacio para resaltar frases completas
    unidos = []
    for o in ops:
        if unidos and viejo[unidos[-1][1]:o[0]].isspace() and o[0] - unidos[-1][1] <= 1:
            unidos[-1] = [unidos[-1][0], o[1], unidos[-1][2] + viejo[unidos[-1][1]:o[0]] + o[2]]
        else:
            unidos.append(o)
    prot = [] if permitir_campos else [(a, b) for a, b in rangos_protegidos(p_el) if b > a]
    # una inserción justo al final de un campo quedaría dentro del resultado del campo:
    # se absorbe el carácter siguiente para que el texto nuevo vaya después del campo
    for o in unidos:
        if o[0] == o[1] and any(o[0] == pb for _, pb in prot) and o[1] < len(viejo):
            o[1] += 1
            o[2] = o[2] + viejo[o[0]]
    for a, b, _ in unidos:
        for pa, pb in prot:
            if (a < pb and b > pa) or (a == b and pa < a < pb):
                raise ValueError(f'el cambio toca un campo/cita: {viejo[pa:pb]!r}')
    for a, b, s in reversed(unidos):
        reemplazar_tramo(p_el, a, b, s, color=color if s.strip() else None)
    if texto(p_el) != nuevo:
        raise RuntimeError('el texto resultante no coincide con el esperado')
    return [(viejo[a:b], s) for a, b, s in unidos]


def reemplazar(p_el, viejo, nuevo, color='cyan', ocurrencia=0):
    """Reemplaza `viejo` por `nuevo` dentro del párrafo, aunque cruce varios runs.

    El texto nuevo hereda el formato del primer run afectado y queda resaltado
    con `color` (None para no resaltar). Devuelve True si hubo reemplazo.
    """
    t = texto(p_el)
    pos = -1
    for _ in range(ocurrencia + 1):
        pos = t.find(viejo, pos + 1)
        if pos < 0:
            return False
    ini, fin = pos, pos + len(viejo)
    for borde in (fin, ini):
        for r, t_el, a, b in _runs_con_texto(p_el):
            if a < borde < b:
                _partir_run(r, t_el, borde - a)
                break
    afectados = [(r, t_el) for r, t_el, a, b in _runs_con_texto(p_el) if a >= ini and b <= fin and b > a]
    if not afectados:
        return False
    primero, t_primero = afectados[0]
    t_primero.text = nuevo
    t_primero.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
    if color:
        _set_highlight(primero, color)
    for r, t_el in afectados[1:]:
        t_el.getparent().remove(t_el)
        if not any(c.tag == W('t') for c in r) and r.getparent() is not None:
            r.getparent().remove(r)
    return True


def reemplazar_parrafo(p_el, nuevo, color='cyan'):
    """Reemplaza todo el texto del párrafo conservando el formato del primer run."""
    t = texto(p_el)
    if not t:
        return False
    return reemplazar(p_el, t, nuevo, color=color)
