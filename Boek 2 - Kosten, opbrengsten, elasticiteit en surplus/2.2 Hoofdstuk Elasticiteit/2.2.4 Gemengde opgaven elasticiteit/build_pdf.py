"""Thin §2.2.4 entrypoint; all source/rendering lives in the paired platform."""
from pathlib import Path
import subprocess
import sys

lesson_root = Path(__file__).resolve().parents[3]
builder = lesson_root.parent / "4veco-platform/build-scripts/content/book-2/b2_224.py"
if not builder.is_file():
    raise SystemExit(f"Paired platform builder not found: {builder}")
subprocess.run([sys.executable, str(builder), "--lesson-root", str(lesson_root),
                *sys.argv[1:]], check=True)
