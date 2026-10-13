"""Lee un reporte de similitud de Turnitin en PDF y extrae los fragmentos sombreados.

Para cada fragmento devuelve: página, número de fuente (la etiqueta de color
que pone Turnitin), color del sombreado y texto. También intenta leer la lista
de fuentes (número, tipo, nombre y porcentaje).

Uso:
    python herramientas/turnitin_pdf.py reporte.pdf salida.json
"""
import json
import re
import sys

import pymupdf

PORTADA = ('Descripción general de integridad', 'Integrity Overview', 'Detalles del documento',
           'Document Details', 'Fuentes principales', 'Top Sources', 'Bloques de texto excluidos')


def _es_tinte(f):
    """Color claro de sombreado (no blanco ni gris)."""
    return f and min(f) > 0.55 and not (min(f) > 0.96) and (max(f) - min(f)) > 0.05


def _es_etiqueta(f):
    """Color saturado de las etiquetas numeradas de fuente."""
    return f and max(f) - min(f) > 0.3 and min(f) < 0.55


def _hex(f):
    return '#%02x%02x%02x' % tuple(int(round(c * 255)) for c in f[:3])


def _cerca(c1, c2):
    """¿El tinte claro c1 corresponde al color saturado c2? (mismo matiz)"""
    def norm(c):
        m = max(c) - min(c) or 1
        return [(x - min(c)) / m for x in c]
    a, b = norm(c1), norm(c2)
    return sum(abs(x - y) for x, y in zip(a, b)) < 0.9


TIPOS = ('Internet', 'Publicación', 'Trabajos del estudiante', 'Publication', 'Student papers', 'Submitted works')


def _es_lista_fuentes(txt):
    lineas = [ln.strip() for ln in txt.split('\n') if ln.strip()]
    n = sum(1 for k in range(len(lineas) - 1) if re.fullmatch(r'\d{1,3}', lineas[k]) and lineas[k + 1] in TIPOS)
    return n >= 3


def leer_fuentes(doc):
    """Lista de fuentes del resumen inicial: [{n, tipo, nombre, porcentaje}]."""
    fuentes = {}
    tipos = TIPOS
    for p in doc:
        lineas = [ln.strip() for ln in p.get_text().split('\n') if ln.strip()]
        for k, ln in enumerate(lineas):
            if re.fullmatch(r'\d{1,3}', ln) and k + 2 < len(lineas) and lineas[k + 1] in tipos:
                nombre, pct = [], ''
                for x in lineas[k + 2:k + 7]:
                    if re.fullmatch(r'<?\d+%', x):
                        pct = x
                        break
                    nombre.append(x)
                fuentes.setdefault(int(ln), {'n': int(ln), 'tipo': lineas[k + 1],
                                             'nombre': ' '.join(nombre), 'porcentaje': pct})
    return [fuentes[k] for k in sorted(fuentes)]


def extraer(ruta):
    doc = pymupdf.open(ruta)
    fragmentos = []
    total_palabras = marcadas = 0
    for np, p in enumerate(doc):
        txt = p.get_text()
        if (any(m in txt for m in PORTADA) and np < 5) or _es_lista_fuentes(txt):
            continue
        tintes, etiquetas = [], []
        for g in p.get_drawings():
            f = g.get('fill')
            if not f or g['rect'].is_empty:
                continue
            if _es_tinte(f):
                tintes.append((g['rect'], tuple(f)))
            elif _es_etiqueta(f):
                etiquetas.append((g['rect'], tuple(f)))
        palabras = p.get_text('words')  # x0,y0,x1,y1,palabra,bloque,linea,n
        # etiquetas numeradas: un número dentro de un recuadro saturado
        nums = []
        for w in palabras:
            if re.fullmatch(r'\d{1,3}', w[4]):
                c = pymupdf.Point((w[0] + w[2]) / 2, (w[1] + w[3]) / 2)
                for r, f in etiquetas:
                    if c in r:
                        nums.append((w, f))
                        break
        ids_num = {id(w) for w, _ in nums}
        actual = None
        for w in palabras:
            if id(w) in ids_num:
                continue
            total_palabras += 1
            c = pymupdf.Point((w[0] + w[2]) / 2, (w[1] + w[3]) / 2)
            color = next((f for r, f in tintes if c in r), None)
            if color is None:
                actual = None
                continue
            marcadas += 1
            if actual and actual['_color'] == color:
                actual['texto'] += ' ' + w[4]
                continue
            # fuente: etiqueta más cercana antes de la palabra con el mismo matiz
            fuente = None
            mejor = None
            for nw, nf in nums:
                if not _cerca(color, nf):
                    continue
                dy = w[1] - nw[1]
                if abs(dy) < 4:  # misma línea
                    dy = 0
                d = dy * 1000 + (w[0] - nw[0])
                if d >= -5 and (mejor is None or d < mejor):
                    mejor, fuente = d, int(nw[4])
            actual = {'pagina': np + 1, 'fuente': fuente, 'color': _hex(color), '_color': color, 'texto': w[4]}
            fragmentos.append(actual)
    for f in fragmentos:
        f.pop('_color', None)
        f['palabras'] = len(f['texto'].split())
    # propagar fuente a fragmentos sin etiqueta del mismo color en la misma página o siguiente
    ultimo = {}
    for f in fragmentos:
        if f['fuente'] is not None:
            ultimo[f['color']] = f['fuente']
        elif f['color'] in ultimo:
            f['fuente'] = ultimo[f['color']]
    return {'archivo': ruta, 'paginas': doc.page_count, 'palabras': total_palabras,
            'palabras_marcadas': marcadas, 'fuentes': leer_fuentes(doc), 'fragmentos': fragmentos}


if __name__ == '__main__':
    res = extraer(sys.argv[1])
    salida = sys.argv[2] if len(sys.argv) > 2 else re.sub(r'\.pdf$', '', sys.argv[1]) + '_turnitin.json'
    with open(salida, 'w', encoding='utf-8') as fh:
        json.dump(res, fh, ensure_ascii=False, indent=1)
    print(f"páginas {res['paginas']} | palabras marcadas {res['palabras_marcadas']} de {res['palabras']}"
          f" | fragmentos {len(res['fragmentos'])} | fuentes listadas {len(res['fuentes'])} -> {salida}")
