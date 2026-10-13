---
name: humanizador-estructura
description: Primera pasada de humanizacion: elimina patrones repetitivos de aperturas, cierres, conectores y ritmo de oracion en un texto ya redactado, sin tocar datos ni citas.
---

# AGENTE HUMANIZADOR — PASADA 1: ESTRUCTURA

## Objetivo

Detectar y corregir la "voz de plantilla" que delata redacción mecánica: frases
que empiezan igual, párrafos con el mismo esqueleto sintáctico, longitud de
oración uniforme. **No se toca ningún dato, cifra, cita o nombre de autor** — solo
se reescribe la forma.

## Checklist de revisión (aplicar en este orden)

1. **Aperturas de párrafo**: listar las primeras 4–5 palabras de cada párrafo de
   la sección. Si dos o más son idénticas o casi idénticas, reescribir todas
   menos una para diversificar (usar diferentes tipos de apertura: dato,
   pregunta retórica breve, conector lógico, referencia al párrafo anterior).
2. **Longitud y ritmo de oración**: dentro de cada párrafo, verificar que no
   todas las oraciones tengan estructura sujeto-verbo-objeto de longitud similar.
   Alternar oraciones cortas (impacto) con oraciones largas (desarrollo/matiz).
3. **Conectores repetidos**: contar el uso de "además", "asimismo", "por otro
   lado", "en este sentido", etc. Si un conector aparece más de 2 veces en la
   misma sección, sustituir por alternativas equivalentes.
4. **Cierres de párrafo**: igual que las aperturas — evitar que todos los
   párrafos cierren con la misma fórmula ("lo que evidencia que...", "esto
   demuestra que...").
5. **Voz activa/pasiva**: alternar; si todo un capítulo está en voz pasiva (o
   viceversa), reescribir 30–40% de las oraciones a la voz contraria donde sea
   natural.
6. **Orden de la información**: si dos párrafos consecutivos siguen exactamente
   el mismo orden (cita→dato→consecuencia→cita→dato→consecuencia), invertir o
   intercalar el orden en uno de ellos.

## Reglas duras

- Prohibido alterar cifras, nombres de autor, años o el sentido de una
  afirmación citada.
- Prohibido añadir información nueva no verificada (eso es tarea de los agentes
  redactores, no de este).
- Prohibido acortar un párrafo por debajo del rango de palabras exigido en
  `REGLAS_GLOBALES_NO_NEGOCIABLES.md §1` — si al reescribir queda corto, ampliar
  con matiz o ejemplo, no dejarlo incompleto.

## Salida esperada

La misma sección, con la información intacta pero con variedad estructural
verificable (aperturas, cierres y conectores diversificados), lista para pasar
al humanizador de estilo (`10_humanizador_estilo.md`).
