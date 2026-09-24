#!/usr/bin/env python3
"""Copy the protected case scaffold and replace identity placeholders."""

from __future__ import annotations

import argparse
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("destination", type=Path)
    parser.add_argument("--paper", required=True)
    parser.add_argument("--doi", required=True)
    parser.add_argument("--panel", required=True)
    parser.add_argument("--plot-family", required=True)
    parser.add_argument("--language", choices=["Python", "R"], required=True)
    parser.add_argument("--status", default="SOURCE_READY")
    parser.add_argument("--figure-ready-file", default="figure_ready.tsv")
    args = parser.parse_args()

    source = Path(__file__).resolve().parents[1] / "assets" / "protected-template"
    destination = args.destination.resolve()
    if destination.exists():
        raise SystemExit(f"Destination already exists: {destination}")
    if not source.is_dir():
        raise SystemExit(f"Protected template missing: {source}")

    destination.mkdir(parents=True)
    for directory in ("docs", "example_input", "example_output", "figure_ref"):
        (destination / directory).mkdir()

    main_file = "main.py" if args.language == "Python" else "main.R"
    backend_file = "plot.py" if args.language == "Python" else "plot.R"
    runner = "python" if args.language == "Python" else "Rscript"
    replacements = {
        "__PAPER_IDENTITY__": args.paper,
        "__DOI__": args.doi,
        "__FIGURE_PANEL__": args.panel,
        "__PLOT_FAMILY__": args.plot_family,
        "__LANGUAGE__": args.language,
        "__STATUS__": args.status,
        "__FIGURE_READY_FILE__": args.figure_ready_file,
        "__MAIN_FILE__": main_file,
        "__BACKEND_FILE__": backend_file,
        "__MAIN_COMMAND__": f"{runner} {main_file}",
        "__CLI_COMMAND__": f"{runner} {backend_file} --config example_output/preview.config.json",
        "__CHECK_DATE__": "UNRESOLVED",
        "__PAPER_URL__": "UNRESOLVED",
        "__CODE_URL__": "UNRESOLVED",
        "__CODE_CLASS__": "UNRESOLVED",
        "__COMMIT__": "UNRESOLVED",
        "__VERSION__": "UNRESOLVED",
        "__DATA_URL__": "UNRESOLVED",
        "__DATA_IDENTITY__": "UNRESOLVED",
        "__ACCESS_STATE__": "UNRESOLVED",
        "__PANEL_CODE__": "UNRESOLVED",
        "__REQUIRED_COLUMNS__": "UNRESOLVED",
        "__ROW_RULES__": "UNRESOLVED",
        "__CATEGORY_RULES__": "UNRESOLVED",
        "__TRANSFORMS__": "UNRESOLVED",
        "__METHOD__": "UNRESOLVED",
        "__MAPPINGS__": "UNRESOLVED",
        "__RANDOMNESS__": "UNRESOLVED",
    }
    mappings = {
        "README.md.template": "README.md",
        "backend_contract.json.template": "backend_contract.json",
        "source_manifest.json.template": "source_manifest.json",
        "package_list.txt.template": "package_list.txt",
        "sessionInfo.txt.template": "sessionInfo.txt",
        "SOURCE_MAP.md.template": "docs/SOURCE_MAP.md",
        "SCIENTIFIC_CONTRACT.md.template": "docs/SCIENTIFIC_CONTRACT.md",
        "METHOD.md.template": "docs/METHOD.md",
        "REPRODUCTION_NOTES.md.template": "docs/REPRODUCTION_NOTES.md",
        "example_input.README.md.template": "example_input/README.md",
        "Report_cn.Rmd.template": f"{args.plot_family}_cn.Rmd",
        "Report_en.Rmd.template": f"{args.plot_family}_en.Rmd",
        "report_style.css": "report_style.css",
    }
    if args.language == "Python":
        mappings.update({"main.py.template": "main.py", "plot.py.template": "plot.py"})
    else:
        mappings.update({"main.R.template": "main.R", "plot.R.template": "plot.R"})

    for template_name, relative_output in mappings.items():
        content = (source / template_name).read_text(encoding="utf-8")
        for old, new in replacements.items():
            content = content.replace(old, new)
        (destination / relative_output).write_text(content, encoding="utf-8")

    print(destination)
    print("Adapt every placeholder and case-specific contract before execution.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
