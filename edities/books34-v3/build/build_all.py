"""Thin entry point for the current platform-owned exercise-route revision.

The received build sequence remains in platform's immutable staged package.
See SOURCE_OWNERSHIP.md and ROUTE-REVISION-2026-09-21.md for current evidence.
"""
from pathlib import Path
import subprocess
import sys

lessons = Path(__file__).resolve().parents[3]
builder = lessons.parent / "4veco-platform/build-scripts/books/rebuild_exercise_routes.py"
if not builder.is_file():
    raise SystemExit("The adjacent 4veco-platform checkout is required.")
subprocess.run([sys.executable, "-X", "utf8", str(builder), "--lesson-root", str(lessons), "--books", "34"], check=True)
