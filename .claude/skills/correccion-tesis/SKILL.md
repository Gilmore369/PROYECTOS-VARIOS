---
name: correccion-tesis
description: Corrige una tesis en Word a partir de su reporte de similitud Turnitin (PDF sombreado) y/o del informe del jurado. Pasa el sombreado del PDF al Word, ubica cada coincidencia con su fuente, corrige citas y parafraseo, recorta párrafos sobreexplicados, marca cada cambio en cian y entrega el Word corregido, su PDF y el Excel de registro de cambios. Usalo cuando el usuario suba un .docx con su reporte Turnitin o con observaciones del jurado y pida corregir, mejorar o levantar observaciones.
---

# CORRECCIÓN DE TESIS (Word + Turnitin + jurado)

Herramientas en `herramientas/` (el hook de inicio ya instala pymupdf,
python-docx, openpyxl y LibreOffice, y agrega la carpeta al `PYTHONPATH`).

## 0. Archivos de trabajo

Cada trabajo vive en `trabajos/<nombre>/`:

```
trabajos/<nombre>/entrada/   ← .docx original, PDF Turnitin, informe del jurado, plantilla
trabajos/<nombre>/salida/    ← lo que se entrega
```

Si el usuario no subió los archivos, pídele que los suba a esa carpeta del repo
(GitHub → Add file → Upload files, en la rama de trabajo) y luego haz `git pull`.
Nunca trabajes sobre el original: copia a `salida/` con otro nombre.

## 1. Diagnóstico (siempre antes de editar)

```bash
python herramientas/turnitin_pdf.py entrada/reporte.pdf salida/turnitin.json
python herramientas/mapear_turnitin.py entrada/tesis.docx entrada/reporte.pdf salida/<nombre>
python herramientas/marcado_por_palabra.py entrada/tesis.docx entrada/reporte.pdf salida/marcado.json
```

`marcado_por_palabra.py` alinea palabra por palabra el PDF con el Word: da el
% sombreado de cada párrafo (debe coincidir con el % de Turnitin) y es la base
para estimar cuánto baja la similitud. Úsalo para repartir el esfuerzo:
referencias, títulos, índices y cronograma no se parafrasean (sugerir excluir
bibliografía y coincidencias pequeñas en la configuración de Turnitin).

- `<nombre>_sombreado.docx`: el Word con cada coincidencia resaltada (un color
  por fuente) — es el "PDF Turnitin pasado a Word".
- `<nombre>_coincidencias.xlsx`: párrafo, sección, fuente, tipo de fuente,
  texto coincidente y % del párrafo afectado. Hoja "No ubicados" = fragmentos
  del PDF que no se hallaron en el Word (revisarlos a mano).

Para ver colores o la maquetación de una página concreta del PDF, renderízala
a PNG con pymupdf (`page.get_pixmap(dpi=110).save(...)`) y léela con Read.

Resume al usuario: % total, fuentes principales, secciones más afectadas y
qué coincidencias son legítimas (ver §2).

## 2. Qué hacer con cada coincidencia

| Caso | Acción |
|---|---|
| Definición, dato o idea tomada de un autor **ya citado** | Parafrasear con estructura propia (no solo sinónimos), conservar la cita. |
| Idea de un autor **sin cita** | Agregar la cita al autor original (verificada con `buscador-cientifico`) y parafrasear. Si no se puede identificar la fuente, marcar `[[CITA REQUERIDA]]` y avisar. |
| Coincidencia con otra tesis o "trabajos del estudiante" | Reescribir desde cero con la fuente primaria correcta. |
| Títulos, nombres de variables, instrumentos, frases técnicas fijas, referencias, citas textuales entre comillas | No tocar: se excluyen en la configuración de Turnitin. Indícalo al usuario. |
| Párrafo sobreexplicado o redundante | Condensar: quitar repeticiones y relleno, sin perder datos ni citas. |

Reglas duras:
- No cambiar el sentido de objetivos, hipótesis, variables, resultados, cifras,
  años, autores ni la matriz de consistencia.
- No inventar datos, citas, DOI ni autores (`reglas-globales-tesis` §0).
- Seguir `humanizador-estructura` y `humanizador-estilo` para la redacción.
- No usar trucos para engañar a los detectores: caracteres invisibles,
  letras de otro alfabeto, texto blanco, texto como imagen o similares.
  El objetivo es que el texto quede bien escrito y bien citado.

## 3. Edición del Word

Forma recomendada: escribir `trabajos/<nombre>/cambios.py` con
`NUEVOS = {índice: 'párrafo nuevo completo'}` y aplicarlo:

```bash
python herramientas/aplicar_cambios.py entrada/tesis.docx cambios.py salida/<nombre>_corregido.docx salida/marcado.json
```

Solo se resaltan en cian las palabras que cambian, las citas de Word (campos)
no se tocan (si un cambio las toca, da error y no se aplica) y al final estima
la similitud restante. Antes de redactar, lista los campos de cada párrafo con
`rangos_protegidos()` para dejar las citas idénticas. Los párrafos con texto
propio escrito dentro de una cita van en `CAMPOS_EDITABLES`.

Edición puntual directa:

```python
import docx
from docx_lib import parrafos, reemplazar, reemplazar_parrafo
d = docx.Document('salida/<nombre>_corregido.docx')
P = parrafos(d)                        # i, el, texto, estilo, en_tabla, seccion
reemplazar(P[k]['el'], 'fragmento viejo', 'fragmento nuevo')   # resalta en cian
reemplazar_parrafo(P[k]['el'], 'párrafo nuevo completo')       # resalta en cian
d.save(...)
```

- **Todo cambio queda resaltado en cian, puntualmente** (solo lo cambiado).
- Se conserva el formato del run original (fuente, tamaño, negrita).
- Trabajar por secciones y mostrar al usuario el antes/después de los primeros
  párrafos para que valide el estilo antes de seguir con el resto.

## 4. Observaciones del jurado

Leer el informe (PDF/Word) con pymupdf o python-docx, listar cada observación
y levantarlas una por una en el documento (en cian). Luego armar el Excel de
levantamiento: N°, componente, observación del jurado, acción realizada,
ubicación en la tesis, N° de cambios, estado.

## 5. Verificación y entrega

```bash
python herramientas/comparar.py entrada/tesis.docx salida/<nombre>_corregido.docx salida/<nombre>_registro_cambios.xlsx
herramientas/docx_a_pdf.sh salida/<nombre>_corregido.docx
python herramientas/verificar_refs.py salida/<nombre>_corregido.docx salida/<nombre>_referencias.xlsx
```

Comprobar en el PDF: índices y numeración de tablas/figuras, referencias
cruzadas ("ver Tabla N"), páginas del índice. LibreOffice puede paginar
ligeramente distinto que Word: avisar si el índice depende de eso.

Entregar: `<nombre>_corregido.docx`, su PDF, el registro de cambios y, si
aplica, el Excel de levantamiento. Hacer commit y push de `salida/` y decir
al usuario la ruta. Recordarle que pase de nuevo el documento por Turnitin
y que revise los cambios en cian antes de entregarlo.
