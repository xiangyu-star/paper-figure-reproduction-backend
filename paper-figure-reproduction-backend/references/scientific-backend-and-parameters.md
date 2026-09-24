# Scientific backend and parameterization

## Scientific contract

Write the contract before implementation. It must define:

- input files, schema, types, units, keys and uniqueness;
- required identities, categories, order and row-count rules;
- filtering, transforms, normalization, statistics and coordinate construction;
- mapping from values to panels, layers, labels, sizes, colors and legends;
- randomness source, seed and whether it changes science or display;
- expected outputs and hard failure conditions;
- upstream identity and the derivation of every `AUTHOR_DERIVED` object.

Invalid domain, non-finite required values, missing categories, duplicate keys, unexplained order change, identity/hash mismatch, or empty input must fail rather than silently degrade.

## Parameter candidate audit

Review these groups; expose only useful choices:

1. paths and stable names;
2. scientific/data transformations;
3. selection and ordering;
4. layers and semantic colors;
5. geometry, axes and scales;
6. labels, legends and fonts;
7. canvas/export and randomness.

For each public parameter record: exact name, type, default, allowed/range, units, meaning, source basis, invalidation (`rerender_only`, `recompute_science`, `rebuild_figure_ready`), validation, and all downstream locations.

Trace rule:

```text
main default → config/CLI → backend use → resolved parameters
→ backend contract → CN manual → EN manual
```

If any link is missing, the parameter is not complete. Do not expose knobs that the backend ignores.

## Color policy

Preserve author semantic colors for an exact reproduction. Use PlotXY soft colors only when the user authorizes a palette adaptation and record it as `USER_MODIFIED_BASELINE`; scientific values and categories remain unchanged. Available swatches include `#F7CCCD`, `#F6DBAE`, `#DCE79C`, `#96CFF0`, `#B8DA9B`, `#9DD0F0`, `#65D1CF`, `#B4DCE1`. Validate all color strings; `#65D1CP` is invalid.

## Routine architecture

`main` is the user-facing entry: parameters at top, no expensive acquisition, one config, one backend call, clear exit code. `plot` is the stable adapter: resolve paths, validate config/input, obtain scientific plot objects, render, export, write evidence atomically, verify required outputs and write success last.

Remove any stale success marker before work starts. On failure, return non-zero and retain diagnostics without writing success.

## Scientific freeze during visual repair

Record hashes or summaries of accepted plot data. Display-only changes may alter font, label radius, canvas, spacing, line width, color presentation and export padding, but not values, IDs, filters, order, categories or scientific mappings. If those change, reopen scientific validation.
