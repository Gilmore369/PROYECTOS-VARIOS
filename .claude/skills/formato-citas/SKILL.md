---
name: formato-citas
description: Aplica la norma de citacion que corresponde a la especialidad del usuario (APA, ISO 690, IEEE o Vancouver) a todas las citas en texto y a la lista de referencias, de forma consistente en todo el documento.
---

# AGENTE FORMATEADOR DE CITAS Y REFERENCIAS

## Selección de norma según especialidad

| Área del programa | Norma |
|---|---|
| **Ingeniería** | ISO 690 o IEEE (confirmar cuál exige el programa) |
| **Ciencias empresariales, humanidades, arquitectura, psicología** | APA |
| **Ciencias de la salud** | Vancouver |

Un solo documento usa **una única norma** de inicio a fin. Nunca mezclar.
Recomendar al usuario gestionar la bibliografía con Mendeley o Zotero.

---

## MODO APA

### Citas en texto
- 1 autor: `(Apellido, año)` o `Apellido (año)`
- 2 autores: `(Apellido1 y Apellido2, año)`
- 3 o más: `(Apellido1 et al., año)` desde la primera mención
- Institucional: `(Sigla, año)`
- Textual corta (<40 palabras): comillas + `(Autor, año, p. X)`
- Textual larga (≥40 palabras): bloque con sangría 1,27 cm, sin comillas +
  `(Autor, año, p. X)`
- Paráfrasis: sin comillas, `(Autor, año)`

### Lista de referencias (orden alfabético)
```
Artículo:  Apellido, I. (año). Título del artículo en minúsculas. Nombre de la
           Revista en Cursiva, Volumen(Número), páginas. https://doi.org/xxxxx
Libro:     Apellido, I. (año). Título del libro en cursiva (N.ª ed.). Editorial.
Institucional: Organización. (año). Título del documento en cursiva. https://URL
```
Hasta 20 autores se listan todos con `, &` antes del último; más de 20 →
primeros 19, `...`, último autor. DOI siempre como `https://doi.org/`.

---

## MODO ISO 690 (numérico)

### Citas en texto
`[N]` en orden de aparición. Una misma referencia conserva siempre su número.

### Lista de referencias (orden numérico de aparición, no alfabético)
```
Artículo: [N] APELLIDO, Nombre; APELLIDO2, Nombre2. Título del artículo. Nombre
          de la Revista [en línea]. año, vol. XX, no. X, pp. X-X
          [consultado: DD mes AAAA]. DOI: https://doi.org/xxxxxx. ISSN XXXX-XXXX.
Libro:    [N] APELLIDO, Nombre. Título del libro. N.ª ed. Ciudad: Editorial, año.
          ISBN XXX-XX-XXXX-XXX-X.
Norma:    [N] ORGANISMO. Código:Año. Título de la norma. Ciudad: Organismo, año.
Informe:  [N] ORGANIZACIÓN. Título del informe [en línea]. Ciudad: Organismo, año
          [consultado: DD mes AAAA]. Disponible en: https://URL.
```

---

## MODO IEEE (numérico, ingeniería)

### Citas en texto
`[1]`, `[2]`, `[1], [3]`, `[1]-[4]` en orden de aparición.

### Lista de referencias
```
Artículo: [N] I. Apellido, I. Apellido2, y I. Apellido3, "Título del artículo en
          minúsculas entre comillas," Nombre Abreviado de la Revista en Cursiva,
          vol. X, no. X, pp. X-X, mes año, doi: 10.xxxx/xxxxx.
Libro:    [N] I. Apellido, Título del Libro en Cursiva, N.ª ed. Ciudad, País:
          Editorial, año.
Congreso: [N] I. Apellido, "Título de la ponencia," en Nombre del Congreso,
          Ciudad, País, año, pp. X-X.
Norma:    [N] Título de la norma, Código de la norma, año.
```
Iniciales del nombre **antes** del apellido. Hasta 6 autores; con más, se listan
los tres primeros seguidos de *et al.*

---

## MODO VANCOUVER (numérico, salud)

### Citas en texto
Números arábigos entre paréntesis o superíndice, en orden de aparición: `(1)`,
`(1,3)`, `(1-4)`. Coherente en todo el documento.

### Lista de referencias (orden numérico de aparición)
```
Artículo: N. Apellido IN, Apellido2 IN, Apellido3 IN. Título del artículo.
          Abreviatura de la Revista. año;volumen(número):páginas.
          doi: 10.xxxx/xxxxx
Libro:    N. Apellido IN. Título del libro. N.ª ed. Ciudad: Editorial; año.
Capítulo: N. Apellido IN. Título del capítulo. En: Editor AB, editor. Título del
          libro. Ciudad: Editorial; año. p. X-XX.
Web:      N. Organización. Título [Internet]. Ciudad: Organización; año
          [citado DD mmm AAAA]. Disponible en: https://URL
```
Se listan los **6 primeros autores** y luego *et al.* Apellido seguido de las
iniciales sin puntos. Nombre de revista abreviado según el Index Medicus.

---

## Verificación cruzada obligatoria (todos los modos)

- Cada cita en texto coincide exactamente con su entrada en la lista.
- Ninguna entrada de la lista queda sin ser citada en el texto.
- Todas las URL verificadas (delegado a `01_buscador_cientifico`, confirmado por
  `13_validador_referencias`).
- Se cumplen los mínimos cuantitativos de REGLAS_GLOBALES §10 (cantidad total,
  % de indexadas en Scopus/WoS/SciELO del SJR de Scimago, % en idioma
  extranjero, antigüedad máxima de 5 años).

## Salida esperada

Documento con citas y referencias 100% consistentes en la norma elegida, más un
reporte de cumplimiento de los mínimos cuantitativos de referencias.
