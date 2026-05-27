#!/usr/bin/env python3
"""Validate that MANIFEST.json and the working tree agree.

Noesis treats MANIFEST.json as the declared map of the repository. This
validator fails loudly when the declared map and the files actually on disk
disagree, which is the single most common way a partial export, a bad zip, or
an interrupted branch build silently ships a broken repository.

Checks performed:
  1. Every ``path`` declared in MANIFEST.json exists on disk.
  2. (Advisory) Tracked content files on disk that are NOT declared in the
     manifest are reported as warnings, so the manifest does not silently
     fall behind the tree.

Exit status is non-zero only for missing declared files (hard failure).
Undeclared files are advisory and do not fail the build by default; pass
``--strict`` to treat them as failures too.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "MANIFEST.json"

# Files/dirs that are intentionally not declared in MANIFEST.json.
IGNORE_PREFIXES = (
    ".git/",
    ".github/",            # CI is declared separately / may be absent in MVP
    "scripts/__pycache__/",
    "tests/__pycache__/",
    ".pytest_cache/",
)
IGNORE_NAMES = {".gitignore", ".DS_Store"}


def declared_paths(manifest: dict) -> list[str]:
    found: list[str] = []

    def walk(obj):
        if isinstance(obj, dict):
            path = obj.get("path")
            if isinstance(path, str):
                found.append(path)
            for value in obj.values():
                walk(value)
        elif isinstance(obj, list):
            for item in obj:
                walk(item)

    walk(manifest)
    return sorted(set(found))


def tracked_files() -> list[str]:
    out: list[str] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT).as_posix()
        if rel.startswith(IGNORE_PREFIXES) or Path(rel).name in IGNORE_NAMES:
            continue
        out.append(rel)
    return sorted(out)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate MANIFEST.json against the working tree.")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat undeclared on-disk files as failures, not warnings.",
    )
    args = parser.parse_args()

    if not MANIFEST.exists():
        print("FAIL MANIFEST.json not found at repository root")
        return 1

    try:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"FAIL MANIFEST.json is not valid JSON: {exc}")
        return 1

    declared = declared_paths(manifest)
    if not declared:
        print("FAIL MANIFEST.json declares no file paths")
        return 1

    missing = [p for p in declared if not (ROOT / p).exists()]
    on_disk = set(tracked_files())
    undeclared = sorted(on_disk - set(declared))

    for path in missing:
        print(f"FAIL declared in MANIFEST.json but missing on disk: {path}")
    for path in undeclared:
        print(f"WARN on disk but not declared in MANIFEST.json: {path}")

    failures = len(missing) + (len(undeclared) if args.strict else 0)
    if failures:
        print(
            f"Manifest integrity FAILED: {len(missing)} missing"
            f"{f', {len(undeclared)} undeclared (strict)' if args.strict else ''}."
        )
        return 1

    note = f" ({len(undeclared)} undeclared, advisory)" if undeclared else ""
    print(f"Manifest integrity OK: {len(declared)} declared paths present{note}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
