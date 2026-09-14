"""Rebuild the complete local print bundle and run its local checks."""
from pathlib import Path
import subprocess,sys
ROOT=Path(__file__).resolve().parent
steps=['make_assets.py','build.py','build_answers.py','build_teacher.py','export_paragraphs.py','validate.py']
for step in steps:
    print('\n==',step,'==',flush=True)
    subprocess.run([sys.executable,str(ROOT/step)],cwd=ROOT,check=True)
print('\nDone. Review the rendered PDFs after changes; local checks are not official release approval.')
