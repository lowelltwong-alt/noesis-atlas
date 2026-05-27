#!/usr/bin/env python3
"""Enforce the Noesis-side half of the Noesis-cannot-govern-Logos boundary.

Contract: LOGOS_COMPATIBILITY.md

Noesis may inform Logos but never govern it. Every object Noesis exports toward
Logos must be advisory: it must declare ``authority_over_logos: none`` and must
not assert authority, gating, veto, or promotion power over any Logos artifact.

This validator checks:
  1. registry/logos-compatible-exports.json carries the non-override rules.
  2. Every entry in approved_exports / pending_exports declares
     authority_over_logos == "none".
  3. No export entry contains an authority-asserting field set to a governing
     value (authoritative / binding / overrides / governs / gates / vetoes).

It is a tripwire: with no exports defined yet it passes trivially, and it fails
the first time an export is added without the advisory declaration.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry" / "logos-compatible-exports.json"

REQUIRED_RULE_FRAGMENT = "authority_over_logos: none"
FORBIDDEN_AUTHORITY_VALUES = {
    "authoritative", "binding", "overrides", "override", "governs",
    "governing", "gates", "gating", "vetoes", "veto", "promotes", "demotes",
}
AUTHORITY_KEYS = {"authority_over_logos", "logos_authority", "binding", "governs_logos"}


def is_governing(value) -> bool:
    if isinstance(value, bool):
        return value is True
    if isinstance(value, str):
        return value.strip().lower() in FORBIDDEN_AUTHORITY_VALUES
    return False


def main() -> int:
    failures: list[str] = []

    if not REGISTRY.exists():
        print(f"FAIL {REGISTRY.relative_to(ROOT)} not found")
        return 1

    try:
        data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"FAIL export registry is not valid JSON: {exc}")
        return 1

    rules = " ".join(str(r) for r in data.get("rules", []))
    if REQUIRED_RULE_FRAGMENT not in rules:
        failures.append(
            "export registry rules must state the non-override guarantee "
            f"('{REQUIRED_RULE_FRAGMENT}')"
        )

    for bucket in ("approved_exports", "pending_exports"):
        for entry in data.get(bucket, []):
            if not isinstance(entry, dict):
                continue
            eid = entry.get("export_id") or entry.get("id") or "<unnamed>"
            if entry.get("authority_over_logos") != "none":
                failures.append(
                    f"{bucket}: export '{eid}' must declare authority_over_logos: none"
                )
            for key in AUTHORITY_KEYS:
                if key in entry and is_governing(entry[key]):
                    failures.append(
                        f"{bucket}: export '{eid}' asserts governing authority via "
                        f"'{key}={entry[key]}' — Noesis may not govern Logos"
                    )

    if failures:
        for f in failures:
            print(f"FAIL {f}")
        print(
            f"\nLogos export safety violated: {len(failures)} issue(s). "
            "See LOGOS_COMPATIBILITY.md. Noesis may inform Logos but never govern it."
        )
        return 1

    print("Logos export safety OK: all exports are advisory (authority_over_logos: none).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
