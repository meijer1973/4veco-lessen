"""HOW TO ADAPT: thin §231 wrapper; all content and print logic lives in platform."""
from pathlib import Path
import subprocess
import sys
lesson_root = Path(__file__).resolve().parents[3]
builder = lesson_root.parent / "4veco-platform/build-scripts/content/book-2/b2_231.py"
if not builder.is_file():
    raise FileNotFoundError(f"Paired §231 platform builder not found: {builder}")
if "--lesson-root" in sys.argv[1:]:
    raise ValueError("The wrapper supplies its exact lesson root; do not duplicate it")
subprocess.run([sys.executable, str(builder), "--lesson-root", str(lesson_root), *sys.argv[1:]], check=True)
