"""Rebuild native Book 2 sources through the owning platform workflow."""
from pathlib import Path
import subprocess,sys
lessons=Path(__file__).resolve().parents[7]
builder=lessons.parent/'4veco-platform/build-scripts/books/rebuild_book2_signed.py'
subprocess.run([sys.executable,'-X','utf8',str(builder),'--lesson-root',str(lessons),'--all'],check=True)
