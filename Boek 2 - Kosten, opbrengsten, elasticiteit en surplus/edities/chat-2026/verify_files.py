#!/usr/bin/env python3
"""Check the imported Book 2 delivery without rebuilding or changing any files."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import sys


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent,
                        help="Edition directory containing delivery-manifest.json")
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        manifest = json.loads((root / "delivery-manifest.json").read_text(encoding="utf-8"))
        records = manifest["files"]
        if not records:
            raise ValueError("The delivery manifest is empty")
    except (OSError, ValueError, KeyError) as error:
        print(f"ERROR: cannot read delivery manifest: {error}", file=sys.stderr)
        return 2
    failures = []
    for record in records:
        relative = Path(record["path"])
        path = (root / relative).resolve()
        if relative.is_absolute() or not path.is_relative_to(root):
            failures.append(f"Unsafe manifest path: {relative}")
            continue
        try:
            if path.stat().st_size != record["bytes"]:
                failures.append(f"Size differs: {relative}")
                continue
            digest = hashlib.sha256()
            with path.open("rb") as stream:
                for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                    digest.update(chunk)
            if digest.hexdigest() != record["sha256"]:
                failures.append(f"SHA-256 differs: {relative}")
        except OSError as error:
            failures.append(f"Missing/unreadable: {relative}: {error}")
    if failures:
        print("\n".join(failures), file=sys.stderr)
        print(f"FAILED: {len(failures)} file-integrity problem(s)", file=sys.stderr)
        return 1
    print(f"PASS: {len(records)} delivered files match their original bytes.")
    print("File integrity only; no content review, rebuild, or repository CI claim.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
