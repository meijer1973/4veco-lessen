"""Rebuild the full checked chapter, then renew all paragraph exports."""
from pathlib import Path
import subprocess,sys
root=Path(__file__).resolve().parents[2]
subprocess.run([sys.executable,str(root/'build_all.py')],check=True)
