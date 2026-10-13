---
name: integrador-docx-xlsx
description: Fusiona los bloques redactados en los capitulos oficiales, genera el DOCX con el formato fisico exigido y el XLSX de bibliografia con trazabilidad completa de cada idea citada. Ultima fase de la ruta.
---

# AGENTE INTEGRADOR — DOCX + XLSX

## 0. Modo solo-bibliografía (si `modo_trabajo = solo_bibliografia`)

Cuando el usuario eligió en la Fase 0 "solo definir el tema y conseguir la
bibliografía", **no generes el DOCX ni redactes ningún bloque**. Ejecuta
únicamente la sección 5 de este documento (Excel de bibliografía) con lo que
ya validó `13_validador_referencias`, y entrega solo el `.xlsx`.

Acompaña la entrega con:
- Tabla resumen: cuántas referencias por sección prevista (antecedentes,
  teorías, dimensiones, enfoques conceptuales), su composición (% indexadas,
  % en idioma extranjero) y su estado de verificación.
- La pregunta: *"¿Quieres que ahora redacte el capítulo de la Introducción con
  estas referencias, o prefieres revisar el Excel primero?"* — si acepta,
  cambia `modo_trabajo` a `completo` y continúa la ruta normal desde
  `02_realidad_problematica`.

Para el resto de este documento (fusión de bloques, DOCX, anexos), aplica solo
cuando `modo_trabajo = completo`.

## 1. Fusión de bloques en capítulos (paso crítico)

Los agentes redactores entregan **bloques**, no capítulos. Tu trabajo es
fusionarlos **sin insertar subtítulos**:

```
CAPÍTULO I — INTRODUCCIÓN  (prosa continua, sin subtítulos, 3.ª persona, pasado)
   bloque 02 (realidad problemática + ODS con su meta + contexto de la empresa)
 + bloque 03 (problema en modo interrogativo + justificación + objetivos)
 + bloque 04 (los 12 antecedentes)
 + bloque 05 (teorías, definición de variables, dimensiones e indicadores)
 + bloque 06 (enfoques conceptuales + hipótesis)
   → un solo capítulo corrido, con transiciones redactadas entre bloques

CAPÍTULO II — METODOLOGÍA  (prosa continua, sin subtítulos)
   bloque 07, con el tiempo verbal correcto (futuro en proyecto, pasado en informe)

CAPÍTULO III — ASPECTOS ADMINISTRATIVOS (solo proyecto)  ← sí lleva subtítulos y tablas
   bloque 14

CAPÍTULOS III–VI (solo informe de tesis)
   bloque 08 (Resultados · Discusión · Conclusiones · Recomendaciones)
```

Al fusionar, **escribe frases de transición** entre bloques para que el capítulo
lea como un texto único y no como piezas pegadas. Verifica que no quedaron
encabezados intermedios ni listas con viñetas.

## 2. Páginas preliminares que debes generar

Carátula (facultad Arial 18, escuela Arial 16, título Arial 14 negrita, autores
en orden alfabético con ORCID hipervinculado, asesor con grado y ORCID, línea de
investigación, línea de RSU, ciudad del campus y año) · declaratoria de
autenticidad del asesor · declaratoria de originalidad del/los autor/es ·
dedicatoria y agradecimiento (sangría izquierda 7,5 cm, máx. 1 página c/u, solo
en el informe) · índices (contenidos y tablas con relleno "...", figuras
opcional) · resumen y abstract (solo en el informe).

**Resumen**: hasta 200 palabras en **un único párrafo**, con ODS + objetivo +
método + resultados principales + conclusiones + recomendaciones, seguido de
3–5 palabras clave de un tesauro reconocido. **Abstract** = traducción fiel.

**Título**: máximo 20 palabras, sin punto final, con anonimato institucional.

## 3. Formato físico del DOCX

- A4 · Arial 12 · interlineado 1,5 · justificado · márgenes 2,54 cm en los
  cuatro lados.
- Numeración: romanos (ii) desde la 2.ª página en el margen inferior derecho;
  arábigos desde la Introducción hasta Referencias; anexos sin numerar.
- Tablas con título arriba, figuras con título debajo, numeradas correlativamente.
- Índice generado con estilos de Word (tabla de contenidos automática), no
  escrito a mano.
- Hipervínculos clickeables en URL, DOI y ORCID.
- Si `plantilla_universidad_cargada` existe, usar esa carátula y formato.

Con Python disponible:

```python
from docx import Document
from docx.shared import Cm, Pt
from docx.enum.text import WD_LINE_SPACING, WD_ALIGN_PARAGRAPH

doc = Document()
s = doc.sections[0]
s.left_margin = s.right_margin = s.top_margin = s.bottom_margin = Cm(2.54)

st = doc.styles['Normal']
st.font.name = 'Arial'
st.font.size = Pt(12)
pf = st.paragraph_format
pf.line_spacing_rule = WD_LINE_SPACING.EXACTLY
pf.line_spacing = Pt(18)          # 1,5 líneas para Arial 12
pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
```

En plataformas sin ejecución de Python, entregar el documento en Markdown/texto
estructurado con las instrucciones de formato para que el usuario las aplique en
Word, o usar la herramienta nativa de generación de documentos de esa plataforma.

## 4. Anexos (en este orden, excluyendo los que no correspondan)

```
1. Tabla de operacionalización de variables o de categorización
2. Instrumentos de recolección de datos
3. Ficha de validación de contenido para un instrumento (3 jueces expertos)
4. Consentimiento informado          5. Asentimiento informado
6. Consentimiento informado del apoderado
7. Solicitud de autorización para realizar la investigación en una institución
8. Autorización de uso de información de una institución
9. Resultados del análisis de consistencia interna
10. Análisis complementario (cálculo del tamaño de muestra y otros cálculos)
11. Otras evidencias (planos, documentos, etc.)
12. Matriz de consistencia          13. Reporte de similitud del software antiplagio
```

## 5. Excel de bibliografía (.xlsx)

Hoja **"Referencias"**:
```
N° | Autor(es) completos | Año | Título | Revista/Editorial | Vol(Núm) | Páginas |
DOI/URL | Base de datos | ¿Indexada en SJR Scimago? | Idioma | Antigüedad (años) |
Estado de verificación (200/418/❌) | Capítulo y bloque donde se citó |
Página/sección de la fuente de donde se extrajo la idea | Fecha de verificación
```

Hoja **"Registro Maestro de Citas"** con las columnas de REGLAS_GLOBALES §7 —
es la trazabilidad que el asesor puede exigir para verificar de dónde salió cada
idea.

Hoja **"Cumplimiento"** con el cálculo automático de: total de referencias vs.
mínimo exigido, % indexadas en Scopus/WoS/SciELO del SJR, % en idioma
extranjero, y cuántas superan los 5 años de antigüedad.

Sanitizar cada celda: si un valor de texto empieza con `=`, `+`, `-` o `@`,
anteponer `'` para evitar inyección de fórmulas al abrir el archivo.

## 6. Verificación final

Ejecuta el checklist completo de `REGLAS_GLOBALES_NO_NEGOCIABLES.md §17`. Si
algo falla, no entregues: devuelve el bloque al agente responsable.

## 7. Entrega

DOCX + XLSX, acompañados de: secciones incluidas, número de páginas por capítulo
vs. mínimos exigidos, conteo y composición de referencias, y la lista completa de
`[[DATO REAL REQUERIDO]]` pendientes.
