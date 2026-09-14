"""Rebuild from editable Markdown; do not rerun authoring scripts implicitly."""
from pathlib import Path
import subprocess,sys
ROOT=Path(__file__).resolve().parent
for script in ['make_assets.py','make_revision_assets.py','build.py','validate.py','export_paragraphs.py']:
    subprocess.run([sys.executable,str(ROOT/script)],cwd=ROOT,check=True)
