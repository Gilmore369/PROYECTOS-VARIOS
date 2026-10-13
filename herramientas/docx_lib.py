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
