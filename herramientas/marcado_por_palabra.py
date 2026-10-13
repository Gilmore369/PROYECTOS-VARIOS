"""Alinea palabra por palabra el cuerpo del PDF de Turnitin con el Word.

Devuelve, para cada párrafo del Word, qué palabras están sombreadas y con qué
fuente. Es más robusto que buscar fragmento por fragmento porque Turnitin
parte las coincidencias en trozos de 1 o 2 palabras.

Uso:
    python herramientas/marcado_por_palabra.py tesis.docx reporte.pdf salida.json
"""
import json
import re
import sys
import unicodedata
from difflib import SequenceMatcher

import docx
import pymupdf

from docx_lib import parrafos
from turnitin_pdf import _es_etiqueta, _es_resumen, _es_tinte

RX_PAL = re.compile(r'\w+', re.UNICODE)


def _n(w):
    return unicodedata.normalize('NFKC', w).lower()


def palabras_pdf(ruta):
    out = []  # (palabra_normalizada, sombreada)
    for p in pymupdf.open(ruta):
        if _es_resumen(p.get_text()):
            continue
        tintes = [g['rect'] for g in p.get_drawings() if g.get('fill') and _es_tinte(g['fill'])]
        etiquetas = [g['rect'] for g in p.get_drawings() if g.get('fill') and _es_etiqueta(g['fill'])]
        for w in p.get_text('words'):
            c = pymupdf.Point((w[0] + w[2]) / 2, (w[1] + w[3]) / 2)
            if re.fullmatch(r'\d{1,3}', w[4]) and any(c in r for r in etiquetas):
                continue
            som = any(c in r for r in tintes)
            for t in RX_PAL.findall(w[4]):
                out.append((_n(t), som))
    return out


def main(ruta_docx, ruta_pdf, salida):
    pdf = palabras_pdf(ruta_pdf)
    pars = parrafos(docx.Document(ruta_docx))
    doc_tokens, dueño = [], []
    for k, p in enumerate(pars):
        for m in RX_PAL.finditer(p['texto']):
            doc_tokens.append(_n(m.group()))
            dueño.append((k, m.start(), m.end()))
    sm = SequenceMatcher(None, doc_tokens, [w for w, _ in pdf], autojunk=False)
    marca = [None] * len(doc_tokens)
    for a, b, n in sm.get_matching_blocks():
        for j in range(n):
            marca[a + j] = pdf[b + j][1]
    res = []
    for k, p in enumerate(pars):
        idx = [i for i, d in enumerate(dueño) if d[0] == k]
        if not idx:
            continue
        som = [i for i in idx if marca[i]]
        tramos = []
        for i in som:
            s, e = dueño[i][1], dueño[i][2]
            if tramos and s - tramos[-1][1] <= 2:
                tramos[-1][1] = e
            else:
                tramos.append([s, e])
        res.append({'i': p['i'], 'seccion': p['seccion'], 'en_tabla': p['en_tabla'], 'palabras': len(idx),
                    'sombreadas': len(som), 'alineadas': sum(1 for i in idx if marca[i] is not None),
                    'tramos': tramos, 'texto': p['texto']})
    tot = sum(r['palabras'] for r in res)
    som = sum(r['sombreadas'] for r in res)
    with open(salida, 'w', encoding='utf-8') as fh:
        json.dump(res, fh, ensure_ascii=False, indent=1)
    print(f'palabras Word {tot} | sombreadas {som} ({100 * som / max(1, tot):.1f}%) | '
          f'alineadas {sum(r["alineadas"] for r in res)} | párrafos con sombreado '
          f'{sum(1 for r in res if r["sombreadas"])} -> {salida}')


if __name__ == '__main__':
    main(*sys.argv[1:4])
