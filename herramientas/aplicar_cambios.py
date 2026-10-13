"""Aplica un diccionario {índice de párrafo: texto nuevo} sobre una copia del Word.

Solo cambia las palabras distintas y las resalta en cian; respeta las citas
(campos de Word). Estima la similitud restante usando el marcado de Turnitin.

Uso:
    python herramientas/aplicar_cambios.py entrada.docx cambios.py salida.docx [marcado.json]
El archivo cambios.py define NUEVOS = {indice: 'texto'} y opcionalmente
CAMPOS_EDITABLES = {indices} (párrafos con texto propio dentro de una cita).
"""
import json
import re
import runpy
import sys

import docx

from docx_lib import aplicar_texto, parrafos


def estimar(marcado, nuevos, total_extra=0):
    """Palabras sombreadas que quedan si se reescriben los párrafos de `nuevos`."""
    tok = re.compile(r'\w+')
    quedan = total = 0
    for r in marcado:
        total += r['palabras']
        if r['i'] not in nuevos:
            quedan += r['sombreadas']
            continue
        nuevo = nuevos[r['i']].lower()
        # un tramo sombreado sigue contando si al menos 4 palabras seguidas siguen iguales
        for a, b in r['tramos']:
            w = tok.findall(r['texto'][a:b].lower())
            for k in range(len(w)):
                for n in range(len(w) - k, 3, -1):
                    if ' '.join(w[k:k + n]) in ' '.join(tok.findall(nuevo)):
                        quedan += 1
                        break
                else:
                    continue
    return quedan, total


def main(entrada, ruta_cambios, salida, ruta_marcado=None):
    cfg = runpy.run_path(ruta_cambios)
    nuevos = cfg['NUEVOS']
    editables = cfg.get('CAMPOS_EDITABLES', set())
    d = docx.Document(entrada)
    pars = {p['i']: p for p in parrafos(d)}
    errores, n = [], 0
    for i, t in sorted(nuevos.items()):
        try:
            if aplicar_texto(pars[i]['el'], t, permitir_campos=i in editables):
                n += 1
        except (ValueError, RuntimeError, KeyError) as e:
            errores.append((i, str(e)))
    d.save(salida)
    print(f'párrafos cambiados {n} | errores {len(errores)} -> {salida}')
    for i, e in errores:
        print(f'  P{i}: {e}')
    if ruta_marcado:
        marcado = json.load(open(ruta_marcado, encoding='utf-8'))
        q, tot = estimar(marcado, {k: v for k, v in nuevos.items() if k not in dict(errores)})
        s0 = sum(r['sombreadas'] for r in marcado)
        print(f'sombreado antes {s0} ({100 * s0 / tot:.1f}%) | estimado después {q} ({100 * q / tot:.1f}%)')


if __name__ == '__main__':
    main(*sys.argv[1:5])
