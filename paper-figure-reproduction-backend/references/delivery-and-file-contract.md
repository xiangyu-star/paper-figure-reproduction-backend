# Delivery and file contract

## Default role tree

```text
<plot-family>_<year>_<journal>_Fig<panel>_<language>/
├── README.md
├── main.py | main.R
├── plot.py | plot.R
├── backend_contract.json
├── source_manifest.json
├── <PlotFamily>_cn.Rmd / .html
├── <PlotFamily>_en.Rmd / .html
├── report_style.css
├── package_list.txt
├── sessionInfo.txt
├── docs/
│   ├── SOURCE_MAP.md
│   ├── SCIENTIFIC_CONTRACT.md
│   ├── METHOD.md
│   └── REPRODUCTION_NOTES.md
├── example_input/
├── example_output/
├── figure_ref/
└── prepare/                  # conditional
```

This is a role catalog, not a file-count target. Docs may merge only if no information is lost and links/contracts stay clear. `prepare/` is conditional.

## File contracts

| Role | Required content | Validation | Forbidden | Omission |
|---|---|---|---|---|
| README | identity/status, quick run, input/output boundary, limitations | commands and names match code/contracts | development diary, inflated COMPLETE | never |
| main | top editable parameters, config construction, one backend call | current routine run | notebook dump, hidden analysis | never |
| plot | validation, science/load, render, export, evidence, failure behavior | main + CLI replay | silent fallback, synthetic substitute | never |
| backend contract | identity, input schema, parameter type/default/allowed/effect, outputs, success | exact code/resolved parity | unimplemented CLI/output | never |
| source manifest | DOI/panel, source classes, URLs, commit/object/hash/access | decisive object traceable | generic bibliography only | never |
| example input | smallest real Figure-ready object plus role/schema | non-empty and hard checks | unrelated large matrices, hidden synthetic rows | never for runnable package |
| example output | current config/resolved/plot data or stats/validation/run manifest/log/PNG/PDF/success as applicable | current and non-empty | old candidates, fake preview | never for COMPLETE |
| CN/EN Rmd+HTML | current case manual with mirrored structure | Knit and browser inspection | boilerplate, expensive analysis | never for COMPLETE |
| CSS | protected Heatmap grammar plus narrow recorded overrides | responsive page/TOC/table/code/image check | compensating plot fonts in CSS | never for COMPLETE |
| figure reference | legal best comparison source and role | identity and visual use recorded | edited target presented as original | omit if unavailable or redistribution forbidden |
| prepare | stable, needed upstream-to-Figure-ready transformation | command and output identity documented | maintainer-only QA | omit by default |

The six-field checklist—role, author mapping, required fields, validation, forbidden items, omission—is applied only where a meaningful user-facing contract exists. Do not pad every file with identical headings.

## Required current-run evidence

At minimum: serialized config, resolved parameters, validation result, run manifest, PNG, PDF and success marker. Add plot data or compact statistics when needed to audit the claim. Add a log when it captures actual execution. Each run manifest identifies code/input/config/output hashes where practical.

## Release exclusions

Exclude runtime, environments, caches, notebooks, whole upstream datasets, absolute paths, credentials, stale candidates, debug dumps, browser profiles, screenshots, overlays, probes, audit scripts/results, release ledgers, extracted test copies and temporary Knit artifacts. Maintainer validation belongs outside the end-user ZIP.
