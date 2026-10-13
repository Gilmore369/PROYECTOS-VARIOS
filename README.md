# PROYECTOS-VARIOS

## Cómo trabajar una corrección

1. Sube a GitHub, en la rama de trabajo, la carpeta `trabajos/<nombre>/entrada/`
   con el `.docx`, el PDF de Turnitin y, si hay, el informe del jurado
   (Add file → Upload files).
2. En la sesión de Claude pide, por ejemplo: *"corrige la tesis de
   trabajos/<nombre>"*.
3. Los resultados quedan en `trabajos/<nombre>/salida/`: el Word con los
   cambios en cian, su PDF y el Excel de registro de cambios.

Herramientas en `herramientas/`:

| Script | Qué hace |
|---|---|
| `turnitin_pdf.py` | Lee el PDF de Turnitin: fragmentos sombreados, color, N° de fuente y lista de fuentes |
| `mapear_turnitin.py` | Pasa ese sombreado al Word y genera el Excel de coincidencias |
| `docx_lib.py` | Edita el Word sin perder formato y resalta los cambios en cian |
| `comparar.py` | Excel de registro de cambios entre dos versiones |
| `docx_a_pdf.sh` | Word → PDF con LibreOffice |
| `verificar_refs.py` | Verifica que los DOI/URL de las referencias respondan |

El hook `.claude/hooks/session-start.sh` instala todo al iniciar cada sesión en la nube.

## Sistema de skills para tesis

Las skills están en `.claude/skills/`, así Claude Code las carga automáticamente
al abrir este repositorio. Cada carpeta contiene un `SKILL.md`.

Punto de entrada: **`orquestador-tesis`** (entrevista, arma la ficha y decide el orden).

| Orden | Skill | Función |
|---|---|---|
| 0 | `orquestador-tesis` | Dirige todo el proceso |
| 0 | `ficha-de-proyecto-tesis` | Plantilla de la ficha y guion de preguntas |
| 0 | `reglas-globales-tesis` | Reglas no negociables que todo agente consulta |
| 0 | `estructura-titulo-profesional` | Estructura oficial de pregrado |
| 0 | `estructura-maestria` | Estructura oficial de maestría |
| 01 | `buscador-cientifico` | Busca y valida referencias en bases indexadas |
| 02 | `redactor-realidad-problematica` | ODS, realidad internacional → local, contexto del caso |
| 03 | `redactor-objetivos-justificacion` | Problema, objetivos y justificación |
| 04 | `redactor-antecedentes` | Los 12 antecedentes |
| 05 | `redactor-teorias-conceptos` | Teorías, variables, dimensiones e indicadores |
| 06 | `redactor-hipotesis-variables` | Enfoques conceptuales, hipótesis y operacionalización |
| 07 | `redactor-metodologia` | Capítulo II |
| 08 | `redactor-resultados-discusion` | Capítulos III–VI (solo con datos reales) |
| 09 | `humanizador-estructura` | Pasada 1: variedad estructural |
| 10 | `humanizador-estilo` | Pasada 2: estilo y paráfrasis |
| 11 | `formato-citas` | APA / ISO 690 / IEEE / Vancouver |
| 13 | `validador-referencias` | Control de calidad final |
| 12 | `integrador-docx-xlsx` | DOCX final + XLSX de bibliografía |
| 14 | `aspectos-administrativos` | Capítulo III del proyecto |
| — | `correccion-tesis` | Corrección de un Word con reporte Turnitin y/o informe del jurado |
