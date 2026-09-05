"""Thin §212 entrypoint; authored content and print logic live in platform."""
from pathlib import Path
import subprocess
import sys

lesson_root = Path(__file__).resolve().parents[3]
builder = lesson_root.parent / "4veco-platform/build-scripts/content/book-2/b2_212.py"
if not builder.is_file():
    raise SystemExit(f"Companion platform builder not found: {builder}")
subprocess.run([sys.executable, str(builder), "--lesson-root", str(lesson_root),
                *sys.argv[1:]], check=True)
