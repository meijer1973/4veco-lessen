"""Build the edited manuscripts, figures, QA report and paragraph views.

Run from any folder: python path/to/Boek_4_H1_bronpakket/build_all.py
The author_*.py recipes are NOT run: direct manuscript edits are preserved.
"""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent

def main() -> None:
    for script in ('make_assets.py', 'build.py', 'validate.py', 'export_paragraphs.py'):
        print(f'\n=== {script} ===', flush=True)
        subprocess.run([sys.executable, str(ROOT/script)], cwd=ROOT, check=True)
    print('\nFinal PDFs are in output/. Page-preserving paragraph views are in paragrafen/.')
    print('After content edits, render and visually inspect the PDFs before publication.')

if __name__ == '__main__':
    main()
