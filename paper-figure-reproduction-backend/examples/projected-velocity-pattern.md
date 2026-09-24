# Example: compact plot-ready scientific object

## Input situation

The author workflow used a very large processed single-cell file, while routine rendering required only cell identities, coordinates and already-computed projected fields.

## Decision

The package kept a compact real plot-ready object, preserved the upstream file identity and author-code mapping in manifests, and excluded the large matrix, acquisition code and checkpoints.

## Reusable lesson

When accepted scientific projection results can be represented losslessly for the target panel, routine delivery may freeze them as a traceable Figure-ready input. This is valid only when the excluded computation and upstream identity are explicit. Display parameters remain rerender-only; changing projection science requires rebuilding the input.

## Do not copy

Do not generalize this case's H5AD schema, fields, cell count, checkpoint names or display defaults.
