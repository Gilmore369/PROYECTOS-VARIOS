---
name: reglas-globales-tesis
description: Reglas no negociables de todo el sistema de tesis: arquitectura de capitulos, persona y tiempo verbal, extension de parrafos, antecedentes, teorias, registro maestro de citas anti-repeticion, bases de datos permitidas, cantidad minima de referencias, norma de citacion por especialidad, formato fisico, humanizacion, etica y checklist final. TODO agente debe consultarla antes de escribir.
---

# REGLAS GLOBALES NO NEGOCIABLES DEL SISTEMA

Aplican a **cualquier** agente, en **cualquier** plataforma (Claude Code, Claude
web, ChatGPT/Codex, Antigravity). Fuente única de verdad. Si un skill específico
contradice esto, gana este documento.

---

## 0. PRINCIPIO RECTOR Y CADENA DE PRODUCCIÓN

```
FICHA DE PROYECTO (orquestador)
   → BÚSQUEDA Y VALIDACIÓN DE REFERENCIAS (buscador + validador)
   → REDACCIÓN POR BLOQUE — cada agente sólo redacta con referencias YA
     validadas y registradas
   → HUMANIZACIÓN (2 pasadas)
   → FORMATO DE CITACIÓN + VERIFICACIÓN CITA↔REFERENCIA
   → INTEGRACIÓN FINAL (DOCX + XLSX)
```

Ningún agente puede citar un autor que no exista en el **Registro Maestro de
Citas** (§7). Ningún agente puede inventar una cita, un dato estadístico, un DOI
o un resultado. Si falta información real de la empresa/caso, se escribe
literalmente `[[DATO REAL REQUERIDO]]` y se continúa — jamás se rellena con
datos inventados.

---

## 1. ⚠️ ARQUITECTURA DEL DOCUMENTO — LA REGLA QUE MÁS SE INCUMPLE

**No existen capítulos separados de "Marco teórico", "Antecedentes", "Marco
conceptual" ni "Hipótesis y variables".** La estructura oficial es:

```
I. Introducción · II. Metodología · III. Aspectos administrativos   (proyecto)
I. Introducción · II. Metodología · III. Resultados · IV. Discusión ·
V. Conclusiones · VI. Recomendaciones                                (informe final)
```

Los antecedentes, las teorías, los enfoques conceptuales y las hipótesis van
**DENTRO del Capítulo I (Introducción)**, en **prosa continua, sin subtítulos,
sin viñetas, sin guiones y sin negrita**.

Los agentes redactores producen bloques temáticos; el agente integrador los
**fusiona en un capítulo corrido**. Ver `ESTRUCTURA_TITULO_PROFESIONAL.md` o
`ESTRUCTURA_MAESTRIA.md` según corresponda.

---

## 2. PERSONA GRAMATICAL Y TIEMPO VERBAL POR CAPÍTULO (obligatorio)

| Capítulo | Persona | Tiempo verbal |
|---|---|---|
| I. Introducción | Tercera persona | **Pasado** del modo indicativo (excepción: los objetivos, en infinitivo) |
| II. Metodología — proyecto (Tesis 1) | Tercera persona | **Futuro** del modo indicativo |
| II. Metodología — informe (Tesis 2) | Tercera persona | **Pasado** del modo indicativo |
| III. Resultados | Tercera persona | **Pasado** del modo indicativo |
| IV. Discusión | Tercera persona | **Presente** |
| V. Conclusiones | Tercera persona | **Pasado** del modo indicativo |
| VI. Recomendaciones | Tercera persona | **Presente** |

Prohibido en Introducción, Metodología y Resultados: viñetas, guiones, negritas
y subtítulos internos. Todo va en prosa corrida.

---

## 3. EXTENSIÓN DE PÁRRAFOS Y DENSIDAD DE CITAS

| Tipo de párrafo | Palabras | Citas mínimas |
|---|---|---|
| Párrafo académico estándar (teorías, enfoques conceptuales, metodología, discusión) | **150–190** | Mínimo 1 autor; ideal 2–3 autores distintos combinados |
| Antecedente (cada uno de los 12) | Hasta **200** máx. | El autor/equipo del propio estudio |
| Realidad problemática (global, sudamericana, nacional, regional) | 150–190 | 1–2 autores o fuentes institucionales |
| Contexto problemático de la empresa/caso | 150–190 | **Sin citas** (ver §4) |
| Párrafo ODS | 150–190 | 1 fuente oficial (ONU/PNUD/CEPAL) |
| Definición del marco/enfoque conceptual | 100–130 | 1 autor distinto |

**Verificación obligatoria** antes de entregar cualquier párrafo: contar
palabras (`len(texto.split())`). Fuera de rango → ampliar con detalle o
condensar. Nunca entregar fuera de rango.

**Todo párrafo que afirme un hecho, dato, cifra o definición debe llevar cita.**
Si no hay cita, el dato no se incluye. Única excepción: los 2 párrafos de
contexto de la empresa.

---

## 4. REALIDAD PROBLEMÁTICA — ORDEN OBLIGATORIO

Dentro del Capítulo I, en prosa continua:

1. **Párrafo ODS** (citado) — nombra el ODS **y su(s) meta(s) específica(s)**
   (ej. "ODS 8, meta 8.2"), no basta con mencionar el número del ODS.
2. **Realidad global/internacional** (1–2 párrafos, citados, con estadísticas).
3. **Realidad sudamericana** (1 párrafo, citado).
4. **Realidad nacional** (1 párrafo, citado — organismo estadístico oficial,
   ministerio sectorial, gremio del país del usuario).
5. **Realidad regional/local** (1 párrafo, citado, del departamento/ciudad).
6. **Contexto problemático de la empresa/caso — exactamente 2 párrafos, SIN
   citas.** Diagnóstico observacional de la situación real. Si falta un dato
   concreto, `[[DATO REAL REQUERIDO]]` en el punto exacto.
7. **Cierre de brecha** que enlaza con la formulación del problema.

Luego siguen, en el mismo capítulo y sin subtítulos: problema de investigación
en **modo interrogativo** (general + específicos), justificación, objetivos
(general + específicos, en infinitivo), antecedentes, teorías, enfoques
conceptuales, e hipótesis.

**Criterios para identificar la problemática** (usar al menos uno para
argumentar el vacío que justifica el estudio): vacíos de conocimiento;
inconsistencias teóricas; desactualización teórica; limitaciones metodológicas
de los estudios previos; falta de contextualización; aplicación inadecuada de
teorías; fragmentación del conocimiento; ausencia de enfoques comparativos;
sesgos en la evidencia; falta de claridad conceptual; escasa aplicabilidad
práctica.

---

## 5. ANTECEDENTES — REGLA EXACTA

- **12 antecedentes** (supera el mínimo oficial de 6 internacionales +
  nacionales). Distribución sugerida: 4–5 internacionales, 4–5 nacionales, 2–4
  locales. Si no hay locales confiables, redistribuir — nunca inventar.
- Provenientes de artículos indexados en **Scopus, Web of Science o SciELO**, de
  revistas presentes en el **SJR de Scimago**.
- Todos comparten metodología (o compatible), rubro/sector análogo y aplicación
  de variables equivalente.
- **Máximo 200 palabras cada uno.** Prosa continua, **en pasado**.
- Contenido obligatorio: Autor(es) (Año) → Objetivo → Metodología (tipo, diseño,
  muestra, instrumentos) → Resultados estadísticos puntuales con cifras exactas
  → Conclusiones (con contrastación de hipótesis si el estudio la tuvo) →
  **Aporte a la investigación actual, máximo 2 líneas**.
- Ningún antecedente repite autor con otro antecedente ni con ninguna otra parte
  del documento (§7).

---

## 6. TEORÍAS Y ENFOQUES CONCEPTUALES (dentro del Cap. I)

Aunque no lleven subtítulo, el contenido debe cubrir:

1. **Definición de cada variable** — 2 párrafos, **4 a 6 autores distintos**
   combinados entre ambos.
2. **Teorías que sustentan la variable** — 2 párrafos, **4 autores distintos**.
3. **Dimensiones e indicadores** — por cada dimensión, **2 párrafos**: uno que
   define la dimensión y cómo se mide, otro que explica sus indicadores y su
   cálculo. **2 autores distintos por párrafo.** Ej.: 3 dimensiones → 6 párrafos.
4. **Enfoques conceptuales / marco conceptual** — 8–12 términos clave, 100–130
   palabras cada uno, cada uno con su cita y autor no repetido.

---

## 7. REGISTRO MAESTRO DE CITAS — REGLA ANTI-REPETICIÓN

Mantener `registro_citas.csv` con: `apellido_autor | año | bloque donde se usó |
tipo de cita | DOI o URL | base de datos | estado de verificación | página/
sección de la fuente de donde se extrajo la idea`.

**Un mismo autor no se cita dos veces en todo el documento**, salvo excepción
justificada por escrito en el registro (máx. 1 repetición, solo si es la
referencia seminal ineludible del tema). Antes de escribir cualquier cita nueva,
leer el registro; si el apellido ya aparece, elegir otro autor.

Excepción legítima: la **Discusión** retoma autores ya citados en antecedentes y
teorías — eso es su función, no cuenta como repetición de cita nueva.

---

## 8. METODOLOGÍA — SEIS SECCIONES EN PROSA (sin subtítulos)

1. **Tipo, enfoque, diseño y alcance** — tipo básica o aplicada **según el
   Manual de Oslo de la OCDE (2018)**; enfoque; diseño acorde; alcance.
2. **Variables o categorías** — definición conceptual de variables y dimensiones
   (cuantitativo) o categorías y subcategorías (cualitativo). La tabla de
   operacionalización/categorización va en **anexos**.
3. **Unidad de análisis** — unidad, población, criterios de inclusión/exclusión,
   tamaño de muestra y muestreo. Cálculos del tamaño muestral en anexos.
4. **Técnicas e instrumentos** — instrumento estandarizado → citar autores en
   ficha técnica + autorización; instrumento propio → **validación con mínimo
   3 jueces expertos** (fichas firmadas en anexos) + análisis de consistencia
   interna interpretado.
5. **Métodos para el análisis de datos** — técnicas descriptivas e inferenciales.
6. **Aspectos éticos** — integridad científica, consentimiento/asentimiento
   informado, autorización institucional, confidencialidad de la entidad.

Cada concepto metodológico se **define y cita**; nunca se afirma sin sustento.
Párrafos de 150–190 palabras.

### 8.1 Metodólogos prohibidos por defecto

No citar: *Hernández-Sampieri, Fernández y Baptista (2014)*, *Arias (2012)*,
*Tamayo y Tamayo (2003)*, *Carrasco Díaz (2005)*, *Valderrama Mendoza (2015)*,
*Bernal (2010)*, *Kerlinger y Lee (2002)*, *Behar Rivero (2008)*, *Vara Horna
(2012)*, *Hurtado de Barrera (2010)*, *Ñaupas et al. (2018)*.

Excepción única: si la rúbrica exige Sampieri → **Hernández-Sampieri & Mendoza
Torres (2023, 2.ª ed.)**, nunca la de 2014.

Un metodólogo **nunca** define un concepto del tema/variable (calidad,
productividad, clima laboral, OEE): eso se cita con literatura del dominio
2022–2026. Máximo 3–4 fuentes metodológicas en todo el documento, sin repetir.

---

## 9. BASES DE DATOS ACEPTADAS

| Tipo | Bases |
|---|---|
| Núcleo exigido por las guías | **Scopus, Web of Science (WoS), SciELO** — de revistas presentes en el **SJR de Scimago** |
| Otras internacionales indexadas | ScienceDirect, IEEE Xplore, Springer Link, Taylor & Francis, Wiley, PubMed/PMC |
| Open access arbitrado | MDPI (revistas con revisión por pares), Frontiers, PLoS ONE |
| Iberoamericanas | Redalyc, Dialnet, EBSCO, Latindex |
| Libros | Editorial académica con ISBN verificable, edición reciente |
| Propiedad intelectual | Patentes, software registrado, modelos de utilidad |
| Institucionales | Organismos oficiales nacionales y supranacionales (ONU, OMS/OPS, CEPAL, BID, OIT, Banco Mundial, ISO, institutos de estadística y ministerios del país) |

**CERO TOLERANCIA:** repositorios de tesis de pregrado de cualquier universidad,
**repositorios agregadores nacionales de tesis** (ej. ALICIA/CONCYTEC,
RENATI/SUNEDU en Perú, y sus equivalentes en otros países), monografías/tesinas
no publicadas, blogs, Wikipedia, ResearchGate/Academia.edu/SlideShare como
fuente primaria, enlaces rotos sin alternativa verificada. Toda búsqueda debe
restringirse con operador `site:` a las bases permitidas — nunca una búsqueda
web genérica sin restricción de dominio (ver `01_buscador_cientifico.md`).

---

## 10. CANTIDAD Y COMPOSICIÓN DE REFERENCIAS

| Nivel | Mínimo | % indexadas (Scopus/WoS/SciELO en SJR) | % en idioma extranjero | Antigüedad máx. |
|---|---|---|---|---|
| Título profesional / pregrado | **30** | **70%** | **30%** | **5 años** |
| Maestría | **40** | **80%** | **40%** | **5 años** |
| Doctorado (referencial) | ≥60 | ≥80% (priorizar Q1–Q2) | ≥40% | 5 años |

Excepción de antigüedad: solo si el autor la sustenta debidamente (obra seminal
insustituible). Se recomienda usar gestor bibliográfico (Mendeley/Zotero).

## 11. VALIDACIÓN DE URL — OBLIGATORIA PARA CADA REFERENCIA

```
1. WebFetch/WebSearch a la URL o DOI propuesto.
2. Verificar HTTP 200 (o 418 = bloqueo de bot, aceptable si el dato es
   verificable por otra vía).
3. Confirmar que título, autores y año coinciden con lo indexado.
4. Si 403/404 → alternativa en PMC, SciELO, Redalyc o el DOI resuelto en doi.org.
5. Registrar estado final: ✅ 200 | ⚠️ 418 | ❌ error sin alternativa (no se usa).
6. Anotar la página o sección exacta de la fuente de donde se extrae la idea.
```

## 12. NORMA DE CITACIÓN SEGÚN ESPECIALIDAD

| Área | Norma |
|---|---|
| Ingeniería | **ISO 690** o **IEEE** |
| Ciencias empresariales, humanidades, arquitectura, psicología | **APA** |
| Ciencias de la salud | **Vancouver** |

Un solo documento usa una única norma de inicio a fin. Detalle completo en
`11_formato_citas.md`. El orquestador confirma la norma con el usuario antes de
que se redacte la primera línea.

## 13. TÍTULO, RESUMEN Y ANONIMATO

- **Título**: máximo **20 palabras**, sin abreviaturas, **sin punto final**,
  incluye variables (o categorías), unidad de análisis, lugar y tiempo.
- **Anonimato institucional obligatorio**: no incluir la razón social de la
  empresa/institución, y garantizar que no se pueda deducir cuál es.
- **Resumen**: hasta **200 palabras en un único párrafo**; precisa el **ODS** al
  que aporta, el objetivo, el método, los principales resultados, las
  conclusiones y las recomendaciones. Debajo, **3 a 5 palabras clave** de un
  tesauro reconocido (UNESCO, DeCS, Corte IDH).
- **Abstract**: traducción fiel del resumen y las palabras clave. Resumen +
  abstract no exceden una página.

## 14. FORMATO FÍSICO

A4 · Arial 12 · interlineado 1,5 · alineación justificada · márgenes 2,54 cm en
los cuatro lados. Numeración: romanos (ii) desde la segunda página en el margen
inferior derecho; arábigos desde la Introducción hasta Referencias; anexos sin
numerar. Índice de contenidos y de tablas con carácter de relleno "...".
Dedicatoria y agradecimiento con sangría izquierda de 7,5 cm, máx. 1 página c/u.

## 15. HUMANIZACIÓN Y ANTIPLAGIO

- Nunca transcribir literalmente un abstract o fragmento fuente.
- Nunca cambiar solo sinónimos manteniendo la sintaxis del original.
- Variar longitud y estructura de oraciones, alternar voz activa/pasiva,
  diversificar conectores, aperturas y cierres de párrafo.
- Se aplican **ambas pasadas de humanización, en orden**:
  `09_humanizador_estructura.md` → `10_humanizador_estilo.md`.
- Respetar la normativa de originalidad y de uso de inteligencia artificial de la
  universidad del usuario; el orquestador debe recordárselo al inicio.

## 16. INTEGRIDAD Y ÉTICA (innegociable)

- **No falsificar** datos empíricos, encuestas, entrevistas ni resultados de una
  empresa/caso no estudiado realmente → `[[DATO REAL REQUERIDO]]`.
- **No suplantar** al estudiante en sustentaciones ni evaluaciones.
- Herramienta de apoyo a la redacción; el estudiante es responsable de
  comprender, defender y declarar el uso de IA conforme al reglamento de
  integridad académica de su universidad.

## 17. CHECKLIST FINAL

- [ ] Estructura de capítulos correcta (sin capítulos inventados; antecedentes y
      teorías **dentro** de la Introducción, en prosa sin subtítulos).
- [ ] Persona y tiempo verbal correctos en cada capítulo (§2).
- [ ] Título ≤20 palabras, con anonimato institucional, sin punto final.
- [ ] Resumen ≤200 palabras en un párrafo con ODS + objetivo + método +
      resultados + conclusiones; 3–5 palabras clave de tesauro; abstract traducido.
- [ ] 12 antecedentes, ≤200 palabras, sin autores repetidos.
- [ ] Teorías y enfoques conceptuales con el conteo de párrafos y autores de §6.
- [ ] Ningún autor repetido en todo el documento (registro limpio).
- [ ] Todos los párrafos dentro del rango de palabras de §3.
- [ ] Referencias: cantidad mínima, % de indexadas y % en idioma extranjero
      según nivel (§10); todas verificadas ✅ 200 o ⚠️ 418, ninguna ❌.
- [ ] Norma de citación única y consistente según especialidad (§12).
- [ ] Dos pasadas de humanización aplicadas.
- [ ] Extensiones mínimas por capítulo cumplidas (ver archivo de estructura).
- [ ] Anexos en el orden establecido (13 anexos, excluyendo los no aplicables).
- [ ] DOCX final con formato físico de §14.
- [ ] XLSX de referencias con trazabilidad: autor, año, título, revista, DOI/URL,
      base, estado, sección citada y **página/sección de origen de la idea**.
