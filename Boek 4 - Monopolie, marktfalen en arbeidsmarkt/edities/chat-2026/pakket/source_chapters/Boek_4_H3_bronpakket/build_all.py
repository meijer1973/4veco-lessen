"""Regenerate all source manuscripts, figures, PDFs, checks and paragraph cuts.

WARNING: author_*.py contain the authoring master. This command overwrites
Markdown edits. To render edited Markdown without regenerating it, use build.py.
"""
from pathlib import Path
import subprocess, sys
ROOT=Path(__file__).resolve().parent
for script in ['make_assets.py','author_chapter.py','author_answers.py','author_teacher.py','build.py','validate.py','export_paragraphs.py']:
    subprocess.run([sys.executable,str(ROOT/script)],cwd=ROOT,check=True)
