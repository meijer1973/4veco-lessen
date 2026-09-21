"""Rebuild this current edition through the platform-owned route."""
from pathlib import Path
import subprocess
import sys
lessons = Path(__file__).resolve().parents[7]
builder = lessons.parent / "4veco-platform/build-scripts/books/rebuild_exercise_routes.py"
subprocess.run([sys.executable, "-X", "utf8", str(builder), "--lesson-root", str(lessons), "--books", "2"], check=True)
