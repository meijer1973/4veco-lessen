"""Thin paired §232 native delegate; all author gates remain mandatory."""
from pathlib import Path
import subprocess
import sys
root=Path(__file__).resolve().parents[3]
if any(a=="--lesson-root" or a.startswith("--lesson-root=") for a in sys.argv[1:]):
    raise SystemExit("Duplicate lesson-root override forbidden")
builder=root.parent/"4veco-platform/build-scripts/content/book-2/b2_232.py"
raise SystemExit(subprocess.call([sys.executable,str(builder),"--lesson-root",str(root),*sys.argv[1:]],cwd=builder.parents[3]))
