# Lessons learned from completed cases

## Cross-case lessons

- Source mapping before plotting prevents the most expensive rework.
- A small Figure-ready object is often the correct delivery boundary, not a compromise, if derivation and identity are explicit.
- File trees are role contracts. Empty docs, unnecessary preparation and whole notebooks reduce clarity.
- User parameters are valuable only when their scientific/display effect and invalidation scope are visible end to end.
- Current execution evidence and a last-written success marker are more reliable than narrative claims.
- HTML must be re-rendered and visually inspected after plot changes; otherwise it may preserve stale images or hide text.

## Projected velocity field pattern

The upstream processed H5AD was very large, while routine rendering needed a compact plot-ready H5AD containing identities, coordinates and projected fields. The successful package excluded the upstream matrix and acquisition code, documented exact upstream identity, and kept only the compact real input. Use this pattern when the scientific projection is already frozen and routine users only need display controls.

## Ternary probability pattern

Author inputs were multiple large H5AD files, but the Figure-ready probabilities were small. Because rebuilding those probabilities remained a legitimate user need, the package retained one preparation script while routine main/plot used only the compact TSV. Use this pattern when preparation is stable, documented and materially useful—not merely because a template has a prepare folder.

## Circular heatmap pattern

The final package removed preparation scripts and source CSVs that routine users did not need. Acceptance depended on label geometry more than approximate overall resemblance: outer genes needed upright tangential orientation; category labels needed curved/arc-centered placement; center overlap counts needed explicit coordinates; small font-weight details mattered. Repeated manual angle tweaks were inferior to explicit geometry and named per-sector offsets. The report also had to be regenerated after each figure update.

For circular plots:

- validate label orientation at multiple sectors;
- calculate arc midpoint and tangent direction;
- expose radii, font sizes, band limits and justified sector offsets;
- keep gene/category order frozen;
- inspect text bounding boxes and center overlaps at final export size;
- test the actual HTML, not only the PNG.

## Failed or superseded patterns

- Generic or scientifically inaccurate plot-family names create downstream confusion; use a semantic English name consistently across files and reports.
- A visually dense validation directory can collect browser profiles, caches and temporary screenshots; isolate temporary browser state and retain only evidence with an audit purpose.
- Reusing a previous HTML without re-knit produces a formally present but incorrect manual.
- Boilerplate six-field sections on every file make documentation longer without improving decisions; apply the checklist only to meaningful interfaces and inputs.
