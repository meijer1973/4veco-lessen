"""Rebuild the complete standalone print package, then validate it.
No network access or repository write is required. Rendering relies on installed
system fonts; Lato and DejaVu reproduce the delivered typography.
"""
from pathlib import Path
import subprocess,sys
ROOT=Path(__file__).resolve().parent

def main():
    for script in ['make_assets.py','build.py','build_answers.py','build_teacher.py','export_paragraphs.py','validate.py']:
        print('\n=== '+script+' ===',flush=True)
        subprocess.run([sys.executable,str(ROOT/script)],cwd=ROOT,check=True)
if __name__=='__main__':main()
