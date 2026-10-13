#!/bin/bash
# Instala lo necesario para leer/editar Word, PDF de Turnitin y Excel en sesiones en la nube.
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "$CLAUDE_PROJECT_DIR"
pip install -q --root-user-action=ignore -r requirements.txt

# LibreOffice convierte .docx a .pdf (reemplaza la automatizacion de Word en Windows)
if ! command -v soffice >/dev/null 2>&1; then
  (apt-get update -qq && apt-get install -y -qq libreoffice-writer >/dev/null) || echo "aviso: no se pudo instalar LibreOffice" >&2
fi

echo "export PYTHONPATH=\"$CLAUDE_PROJECT_DIR/herramientas:\${PYTHONPATH:-}\"" >> "${CLAUDE_ENV_FILE:-/dev/null}"
