"""Rebuild graphics, chapter, answer/teacher books, paragraph exports and checks.

Run from any working directory: python build_all.py
Root Markdown manuscripts remain the editable source; author_*.py are not run.
"""
from pathlib import Path
import subprocess,sys
ROOT=Path(__file__).resolve().parent

def main()->None:
    for script in ('make_assets.py','build.py','export_paragraphs.py','validate.py'):
        subprocess.run([sys.executable,str(ROOT/script)],cwd=ROOT,check=True)
    print('Built and validated. Inspect rendered PDFs after every substantive edit.')
if __name__=='__main__':main()
