# PROYECTOS-VARIOS

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
