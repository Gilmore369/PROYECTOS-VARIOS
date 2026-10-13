# PROYECTOS-VARIOS — instrucciones para Claude

Responde siempre en español. Este repo se usa para redactar y corregir tesis.

## Skills
- Redacción desde cero: empezar por `orquestador-tesis` (usa la ficha, las
  reglas globales, las estructuras y los redactores).
- Corrección de un Word existente (Turnitin, jurado, formato): `correccion-tesis`.
- Bibliografía: solo de bases validadas, vía `buscador-cientifico`; verificar
  con `validador-referencias`.

## Archivos
- Cada trabajo en `trabajos/<nombre>/entrada/` y `trabajos/<nombre>/salida/`.
- El usuario sube los archivos por GitHub a la rama de trabajo; hacer
  `git pull` antes de buscarlos.
- Nunca sobrescribir el original. Entregables en `salida/`, con commit y push.

## Convenciones
- Todo cambio en el Word se resalta en cian, solo en lo modificado.
- Cada corrección va con su Excel de registro de cambios (`herramientas/comparar.py`).
- No inventar datos, citas ni DOI: `[[DATO REAL REQUERIDO]]` / `[[CITA REQUERIDA]]`.
- Word → PDF con `herramientas/docx_a_pdf.sh` (LibreOffice).
