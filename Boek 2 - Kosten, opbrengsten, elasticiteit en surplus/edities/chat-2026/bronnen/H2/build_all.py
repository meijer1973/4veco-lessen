"""Rebuild every deliverable and fail immediately if a step or check fails."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
STEPS = ('make_assets.py', 'build.py', 'build_answers.py', 'build_teacher.py',
         'export_paragraphs.py', 'validate.py')

def main() -> None:
    for step in STEPS:
        print(f'\n=== {step} ===', flush=True)
        subprocess.run([sys.executable, str(ROOT / step)], cwd=ROOT, check=True)

if __name__ == '__main__':
    try:
        main()
    except subprocess.CalledProcessError as exc:
        print(f'Build stopped: {exc.cmd} returned {exc.returncode}', file=sys.stderr)
        raise SystemExit(exc.returncode)
