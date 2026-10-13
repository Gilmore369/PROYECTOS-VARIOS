"""Extrae los DOI y URL de la lista de referencias de un Word y verifica que respondan.

Uso:
    python herramientas/verificar_refs.py tesis.docx salida.xlsx
"""
import re
import sys

import docx
import requests
from openpyxl import Workbook

from docx_lib import parrafos

RX = re.compile(r'(https?://\S+|10\.\d{4,9}/\S+)')


def main(ruta, salida):
    pars = parrafos(docx.Document(ruta))
    inicio = next((k for k, p in enumerate(pars)
                   if re.fullmatch(r'(REFERENCIAS|Referencias|REFERENCIAS BIBLIOGRÁFICAS|Referencias bibliográficas)',
                                   p['texto'].strip())), None)
    refs = [p['texto'].strip() for p in pars[inicio + 1:] if p['texto'].strip()] if inicio is not None else []
    wb = Workbook()
    ws = wb.active
    ws.append(['N°', 'Referencia', 'Enlace', 'Estado HTTP', 'Resultado'])
    s = requests.Session()
    s.headers['User-Agent'] = 'Mozilla/5.0 (verificador de referencias)'
    for n, r in enumerate(refs, 1):
        m = RX.search(r)
        if not m:
            ws.append([n, r, '', '', 'sin DOI/URL'])
            continue
        url = m.group(1).rstrip('.,;)')
        if url.startswith('10.'):
            url = 'https://doi.org/' + url
        try:
            code = s.get(url, timeout=20, allow_redirects=True).status_code
        except requests.RequestException as e:
            code = type(e).__name__
        ok = code == 200 or code == 418 or code == 403
        ws.append([n, r, url, code, '✅' if code == 200 else ('⚠️ bloqueo de bot' if ok else '❌ revisar')])
    wb.save(salida)
    print(f'referencias {len(refs)} -> {salida}')


if __name__ == '__main__':
    main(*sys.argv[1:3])
