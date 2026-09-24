# Visual, report and release gates

## Visual audit

Compare generated and reference at equal pixel dimensions. Inspect full composition and claim-critical crops: axes/ticks, legends/color bars, labels, dense overlaps, annotation geometry and panel spacing. Record reference identity and whether comparison is exact, approximate or style-only.

Classify each mismatch:

- scientific: values, order, categories, filtering, statistics;
- rendering: color, glyph, line, font, label geometry, layer order;
- export: canvas, crop, DPI, padding, embedded font;
- reference uncertainty: crop, compression, publisher assembly, unavailable layer.

Scientific mismatch returns to source/contract/input. Rendering/export mismatch is repaired with the scientific layer frozen. After two unsuccessful eye-tuned iterations, calculate anchor positions, bounding boxes, angles, overlap or pixel distances.

Circular plots require dedicated checks: outer labels remain upright and tangent-consistent; category labels are centered at arc midpoints and follow the band; per-sector correction is a named parameter; center overlap labels use explicit geometry. Never alter gene/category order to create room.

## Report grammar

CN and EN must mirror title levels, section order, code positions and image order. Use the protected Heatmap grammar:

- title/subtitle/author/date;
- expanded floating TOC and numbered sections;
- introductory hero callout and four summary cards;
- task overview, source mapping, compact directory tree and input contract;
- real parameter groups and actual command/interface contract;
- output/evidence tables;
- generated figure before reference;
- compact intermediate tables;
- run instructions, dependencies/environment, randomness/fonts, follow-up integration and final checklist.

Case content replaces template prose. Preview 6–10 rows and about 4–8 audit-critical columns; keep full wide tables on disk. Rmd reads current evidence and must not rerun expensive acquisition/analysis. Use self-contained HTML when practical.

Knit success is not layout success. Open both HTML files and check the TOC, all text, wide tables, code blocks, generated/reference images, mobile width, stale image references, clipping and overlap. Fix report layout in Rmd/CSS; fix plot text in plotting code, not CSS.

## Release gates

1. Run current main.
2. Replay the serialized config through the backend.
3. Confirm required evidence and success-last.
4. Complete equal-size visual audit.
5. Render and browser-inspect CN/EN HTML.
6. Run static package audit.
7. Copy/extract to a fresh directory and repeat routine run, replay and report render.
8. Scan for runtime, cache, absolute paths, credentials, stale/internal artifacts and oversized unjustified files.
9. Build one ZIP from the validated copy and record SHA-256.

Any skipped gate is `not_run`. Public `COMPLETE` requires all gates. Store screenshots, overlays, comparison images, probes, audit output, browser profiles and fresh-extraction working copies in repository-level validation, not the end-user ZIP.
