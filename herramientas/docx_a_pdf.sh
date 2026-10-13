#!/bin/bash
# Convierte uno o varios .docx a PDF con LibreOffice (equivale a ExportAsFixedFormat de Word).
# Uso: herramientas/docx_a_pdf.sh archivo.docx [otro.docx ...]
# El PDF queda junto a cada .docx. La paginación puede diferir ligeramente de Word.
set -euo pipefail
for f in "$@"; do
  soffice --headless --convert-to pdf --outdir "$(dirname "$f")" "$f" >/dev/null 2>&1
  echo "-> ${f%.docx}.pdf"
done
