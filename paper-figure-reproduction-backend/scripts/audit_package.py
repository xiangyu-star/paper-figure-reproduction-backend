#!/usr/bin/env python3
"""Static release audit; it does not claim scientific or execution success."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


FORBIDDEN_PARTS = {
    "runtime", "__pycache__", ".pytest_cache", ".git", ".venv", "venv",
    "node_modules", "browser_profile", "user-data-dir",
}
FORBIDDEN_SUFFIXES = {".pyc", ".pyo", ".tmp", ".bak", ".zip"}
TEXT_SUFFIXES = {".md", ".py", ".r", ".rmd", ".json", ".txt", ".toml", ".yaml", ".yml", ".css", ".html"}
ABSOLUTE_PATTERNS = [
    re.compile(r"[A-Za-z]:[\\/](?:Users|Documents and Settings)[\\/]", re.I),
    re.compile(r"/(?:home|Users)/[^/]+/"),
]
SECRET_PATTERNS = [
    re.compile(r"github_pat_[A-Za-z0-9_]+"),
    re.compile(r"ghp_[A-Za-z0-9]+"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
]
PLACEHOLDER = re.compile(r"__[A-Z][A-Z0-9_]+__")


def add(findings: list[dict], severity: str, code: str, path: str, detail: str = "") -> None:
    findings.append({"severity": severity, "code": code, "path": path, "detail": detail})


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("package", type=Path)
    parser.add_argument("--max-file-mb", type=float, default=100.0)
    args = parser.parse_args()
    root = args.package.resolve()
    findings: list[dict] = []
    if not root.is_dir():
        add(findings, "ERROR", "missing_package", str(root))
    else:
        required = ["README.md", "backend_contract.json", "source_manifest.json", "example_input", "example_output"]
        for name in required:
            if not (root / name).exists():
                add(findings, "ERROR", "missing_required", name)
        mains = [p for p in (root / "main.py", root / "main.R") if p.is_file()]
        plots = [p for p in (root / "plot.py", root / "plot.R") if p.is_file()]
        if len(mains) != 1:
            add(findings, "ERROR", "entrypoint_count", ".", f"found {len(mains)}")
        if len(plots) != 1:
            add(findings, "ERROR", "backend_count", ".", f"found {len(plots)}")
        if not list(root.glob("*_cn.Rmd")) or not list(root.glob("*_en.Rmd")):
            add(findings, "ERROR", "missing_bilingual_rmd", ".")
        if not list(root.glob("*_cn.html")) or not list(root.glob("*_en.html")):
            add(findings, "ERROR", "missing_bilingual_html", ".")

        for path in root.rglob("*"):
            rel = path.relative_to(root).as_posix()
            if any(part.lower() in FORBIDDEN_PARTS for part in path.parts):
                add(findings, "ERROR", "forbidden_artifact", rel)
            if not path.is_file():
                continue
            if path.suffix.lower() in FORBIDDEN_SUFFIXES:
                add(findings, "ERROR", "forbidden_suffix", rel)
            size_mb = path.stat().st_size / (1024 * 1024)
            if size_mb > args.max_file_mb:
                add(findings, "WARNING", "large_file_review", rel, f"{size_mb:.1f} MiB")
            if path.suffix.lower() not in TEXT_SUFFIXES:
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            if PLACEHOLDER.search(text):
                add(findings, "ERROR", "unresolved_placeholder", rel)
            if any(pattern.search(text) for pattern in ABSOLUTE_PATTERNS):
                add(findings, "ERROR", "absolute_path", rel)
            if any(pattern.search(text) for pattern in SECRET_PATTERNS):
                add(findings, "ERROR", "possible_secret", rel)

    passed = not any(item["severity"] == "ERROR" for item in findings)
    result = {"audit_version": "2.0.0", "package": str(root), "passed": passed, "findings": findings}
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
