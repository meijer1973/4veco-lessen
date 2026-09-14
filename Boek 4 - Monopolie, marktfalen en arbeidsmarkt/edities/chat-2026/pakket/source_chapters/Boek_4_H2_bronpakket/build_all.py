"""Rebuild and validate all chapter deliverables from the editable sources."""
from pathlib import Path
import argparse
import subprocess
import sys
R=Path(__file__).resolve().parent
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--regenerate-manuscripts',action='store_true',help='Regenerate Markdown/registry from author_*.py; overwrites direct Markdown edits.')
args=parser.parse_args()
steps=['author_chapter.py','author_answers.py','author_teacher.py'] if args.regenerate_manuscripts else []
steps+=['make_assets.py','build.py','validate.py','export_paragraphs.py']
for script in steps:
    print(f'>>> {script}',flush=True)
    subprocess.run([sys.executable,str(R/script)],cwd=R,check=True)
print('Built and validated all PDFs. Visual review is still required after any revision.')
