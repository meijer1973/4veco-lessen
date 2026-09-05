"""Thin entry point to the paired, governed §223 builder."""
import runpy
import sys
from pathlib import Path

LESSONS = Path(__file__).resolve().parents[3]
BUILDER = LESSONS.parent / "4veco-platform/build-scripts/content/book-2/b2_223.py"
sys.path.insert(0, str(BUILDER.parent))
sys.argv = [str(BUILDER), "--lesson-root", str(LESSONS), *sys.argv[1:]]
runpy.run_path(str(BUILDER), run_name="__main__")
