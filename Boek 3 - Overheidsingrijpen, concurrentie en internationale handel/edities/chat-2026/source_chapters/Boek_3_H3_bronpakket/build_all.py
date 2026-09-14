"""Rebuild the chapter from editable Markdown; then extract and validate.

Author scripts restore the first authored manuscripts and are deliberately NOT
called here. This prevents a rebuild from overwriting later editorial changes.
"""
from pathlib import Path
import subprocess, sys
ROOT=Path(__file__).resolve().parent
for name in ('make_assets.py','build.py','export_paragraphs.py','validate.py'):
    subprocess.run([sys.executable,str(ROOT/name)],cwd=ROOT,check=True)
print('All PDFs, paragraph exports and validation records rebuilt.')
