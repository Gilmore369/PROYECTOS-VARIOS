---
name: ficha-de-proyecto-tesis
description: Plantilla de la Ficha de Proyecto y guion de las 12 preguntas que el orquestador debe hacer al usuario antes de que se redacte una sola linea de la tesis.
---

# FICHA DE PROYECTO — PLANTILLA MAESTRA

Guardar como `ficha_proyecto.md` en la carpeta de la tesis en curso (o, si la
plataforma no tiene archivos persistentes, pedir al usuario que copie el bloque
YAML confirmado a un archivo de texto propio para poder pegarlo en un chat
nuevo). Todos los agentes la leen antes de trabajar.

```yaml
# === NIVEL Y PROGRAMA ===
nivel_academico: ""        # título profesional/pregrado | segunda especialidad | maestría | doctorado
pais: ""
universidad: ""            # solo para conocer su reglamento — NUNCA se imprime en el documento
carrera_o_programa: ""     # ej. Ingeniería Industrial, Administración, Enfermería, Derecho, MBA
facultad: ""
area_disciplinar: ""       # ingeniería | salud | empresariales | humanidades | derecho | arquitectura | educación
norma_citacion: ""         # APA | ISO 690 | IEEE | Vancouver  (se deriva del área, ver §12 reglas globales)
linea_investigacion: ""    # línea específica del programa (va en carátula)
linea_rsu: ""              # línea de responsabilidad social universitaria (va en carátula)
orcid_autor: ""            # obligatorio en carátula
orcid_asesor: ""
asesor_nombre_grado: ""    # ej. "Dr. Apellidos, Nombres" / "Mgtr. Apellidos, Nombres"
ciudad_campus: ""
anio: ""

# === TIPO DE TRABAJO ===
tipo_documento: ""         # proyecto de investigación (Tesis 1) | informe de tesis (Tesis 2) | ambos
estructura_base: ""        # "titulo_profesional" o "maestria"
modo_trabajo: ""           # "completo" (toda la ruta) | "solo_bibliografia" (definir tema + buscar y
                            # validar referencias + entregar Excel, sin redactar todavía)

# === TEMA, TÍTULO Y VARIABLES ===
titulo_tentativo: ""       # máx. 20 palabras: variables + unidad de análisis + lugar + tiempo, sin punto final
enfoque: ""                # cuantitativo | cualitativo | mixto
tipo_investigacion: ""     # básica | aplicada (según Manual de Oslo, OCDE 2018)
diseno: ""                 # no experimental transversal, cuasi-experimental, fenomenológico, estudio de caso...
alcance: ""                # límites del estudio y lo que se pretende alcanzar
variable_independiente: ""     # o categoría 1 en cualitativo
variable_dependiente: ""       # o categoría 2
dimensiones_var_independiente: []   # o subcategorías
dimensiones_var_dependiente: []
relacion_hipotetica: ""
ods_objetivo: ""           # ej. "ODS 8 - Trabajo decente y crecimiento económico"
ods_meta: ""               # ej. "Meta 8.2" — OBLIGATORIO, no basta el número del ODS

# === CASO DE ESTUDIO (con anonimato) ===
empresa_nombre_interno: ""     # solo para contexto del equipo; NUNCA se escribe en el documento
descriptor_anonimo: ""         # cómo se nombrará en el texto: "una empresa del sector textil de la región X"
rubro_sector: ""
ubicacion_caso: ""             # región/ciudad — alimenta la "realidad regional/local"
tamano_organizacion: ""
problema_observado: ""         # en palabras del usuario — insumo de los 2 párrafos sin cita
evidencia_disponible: ""       # ¿tiene reportes, indicadores, quejas, registros? cuáles
unidad_analisis: ""
poblacion: ""
criterios_inclusion: ""
criterios_exclusion: ""
muestra: ""                    # o "[[DATO REAL REQUERIDO]]"
muestreo: ""

# === INSTRUMENTOS ===
instrumento_previsto: ""       # cuestionario Likert, ficha de observación, guía de entrevista...
instrumento_es_propio: ""      # sí (requiere validación de 3 jueces expertos) | no (citar autores originales)
tiene_datos_de_campo: ""       # sí | no  → decide si se activa el agente de Resultados/Discusión

# === ENTREGA ===
formato_documento: "Word (.docx)"
formato_bibliografia: "Excel (.xlsx)"
plantilla_universidad_cargada: ""   # ruta si el usuario subió su carátula/plantilla
fecha_limite: ""
```

---

## FASE 0 — Definir el tema (antes de la ficha completa)

Esta fase corre primero, siempre, aunque el usuario no la pida explícitamente.

**Si el usuario ya trae un tema/título en su primer mensaje** (ej. "Calidad de
servicio y desempeño de los colaboradores en el programa de compras estatales a
mypes"), no se lo vuelvas a preguntar: extrae de ahí candidatos a variable
independiente y dependiente, confírmalos con el usuario en 1 mensaje, y recién
entonces sigue con la Fase 1. Ejemplo de respuesta:

> "De tu tema identifico dos posibles variables: **Calidad de servicio**
> (independiente) y **Desempeño de los colaboradores** (dependiente), en el
> contexto del programa de compras estatales a mypes. ¿Es correcto, o alguna de
> las dos es en realidad la dependiente?"

**Si el usuario NO trae tema todavía**, pregúntale por el problema que observa
en lenguaje simple ("¿qué problema quieres investigar, con tus palabras?") y
constrúyele 2–3 alternativas de variable independiente/dependiente, cada una
con una frase de por qué encaja.

**Modo de trabajo** (preguntar siempre, apenas se define el tema):

> **¿Cómo quieres que avancemos?**
> **A.** Redactar la tesis completa, capítulo por capítulo (ruta completa).
> **B.** Por ahora, solo quiero **definir bien el tema y conseguir la
> bibliografía validada** (antecedentes, teorías, enfoques conceptuales),
> entregada en un **Excel** con las referencias organizadas por sección y
> párrafo — la redacción la hacemos después.
>
> Responde **A** o **B**.

Si elige **B** (`modo_trabajo = solo_bibliografia`): al terminar la Fase 1
(ficha básica) se salta directo a `buscador-cientifico`, y al validar el lote de
referencias se entrega el Excel de inmediato con `integrador-docx-xlsx` (modo
solo bibliografía, sin generar el DOCX todavía). No se redacta ningún bloque de
texto en este modo hasta que el usuario pida continuar con **A**.

---

## FASE 1 — Resto de la ficha (menús numerados, conversacional, 1–2 bloques por turno)

Presenta cada pregunta cerrada como una **lista de opciones en negrita**, no
como una pregunta abierta de párrafo — así se lee como un formulario aunque sea
texto. El usuario responde con la letra/número. Ejemplo de formato a replicar
en cada pregunta cerrada:

> **1. Nivel académico** — ¿cuál es tu caso?
> **A.** Título profesional / pregrado
> **B.** Segunda especialidad
> **C.** Maestría
> **D.** Doctorado

Guion completo:

1. **Nivel académico** (menú A–D, ver ejemplo arriba) → `nivel_academico`,
   `estructura_base`.
2. **Carrera y país** — pregunta abierta corta: "¿Cuál es tu carrera o programa,
   y en qué país estudias?" → determina `area_disciplinar` y de ahí propone la
   norma de citación como menú:
   > **2. Norma de citación** — por tu área te correspondería **[X]**. ¿La
   > confirmas o tu programa exige otra?
   > **A.** APA   **B.** ISO 690   **C.** IEEE   **D.** Vancouver
3. **Etapa** (menú):
   > **3. Etapa de tu trabajo**
   > **A.** Proyecto de investigación (Tesis 1) — aún sin datos de campo
   > **B.** Informe de tesis (Tesis 2) — ya tengo datos recogidos
   → `tipo_documento`, `tiene_datos_de_campo`.
4. **Dimensiones** de cada variable (ya con variables confirmadas en Fase 0):
   "¿Tienes las dimensiones de cada variable, o las propongo yo a partir de la
   literatura?" Si las propone el sistema, presentarlas como lista numerada y
   pedir confirmación o ajuste.
5. **Caso de estudio** — pregunta abierta: "Cuéntame de la empresa o caso:
   rubro, ubicación, tamaño y qué problema real observas." Advertir de
   inmediato: *"por la regla de anonimato no pondré el nombre de la empresa en
   el documento; usaré una descripción como 'una empresa del sector X de la
   ciudad Y'."*
6. **Evidencia**: "¿Tienes datos, reportes o indicadores internos de esa
   empresa?" — si no, advertir: *"marcaré `[[DATO REAL REQUERIDO]]` donde falte
   información real; no voy a inventar datos de tu empresa."*
7. **ODS**: proponer el ODS y la meta específica que mejor encajan, como menú
   de 1–2 opciones razonadas, y confirmar.
8. **Instrumento** (menú):
   > **8. Instrumento de recolección**
   > **A.** Ya tengo uno validado por otro autor
   > **B.** Necesito uno propio (requiere validación de 3 jueces expertos)
9. **Datos de carátula**: ORCID del autor y del asesor, nombre y grado del
   asesor, línea de investigación, línea de RSU, ciudad del campus y año.
10. **Plantilla**: "¿Tienes la plantilla o carátula de tu universidad, o genero
    la estándar?"
11. **Confirmación**: mostrar el resumen completo de la ficha en una tabla
    Markdown (columna "Campo" / columna "Valor") y pedir el visto bueno antes
    de arrancar.

Si el usuario no sabe responder algo técnico (tipo, diseño, alcance), ofrecer
2–3 opciones como menú, explicadas en una frase simple cada una, recomendando
la más común para su tipo de estudio, y dejar la decisión final en sus manos.

## Atajo: retomar o saltar fases

Si el usuario pega una ficha ya confirmada de una sesión anterior, no repitas
la entrevista: léela, resume en 2 líneas en qué fase quedó, y pregunta si
continúa desde ahí. Si pide explícitamente saltarse una pregunta ("no sé, decide
tú"), elige la opción más común para su tipo de estudio, indícalo, y avanza.
