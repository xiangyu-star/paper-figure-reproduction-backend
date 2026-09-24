#!/usr/bin/env python3
"""Create or verify the protected-template SHA-256 manifest."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


MANIFEST = "PROTECTED_TEMPLATE_MANIFEST.json"


def hashes(root: Path) -> dict[str, str]:
    return {
        path.relative_to(root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(root.rglob("*"))
        if path.is_file() and path.name != MANIFEST
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["write", "verify"])
    parser.add_argument("template", type=Path)
    args = parser.parse_args()
    root = args.template.resolve()
    manifest = root / MANIFEST
    current = {"schema_version": 1, "files": hashes(root)}
    if args.mode == "write":
        manifest.write_text(json.dumps(current, indent=2) + "\n", encoding="utf-8")
        print(manifest)
        return 0
    if not manifest.is_file():
        raise SystemExit("Protected manifest is missing")
    expected = json.loads(manifest.read_text(encoding="utf-8"))
    if expected != current:
        print(json.dumps({"passed": False, "expected": expected, "current": current}, indent=2))
        return 1
    print(json.dumps({"passed": True, "files": len(current["files"])}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
