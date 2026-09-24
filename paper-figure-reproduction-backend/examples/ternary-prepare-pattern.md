# Example: conditional preparation retained

## Input situation

Exact author inputs were multiple multi-gigabyte H5AD files. Routine plotting needed a small table of three state probabilities, panel identities and stable cell identifiers.

## Decision

The release used the compact table for main/plot and retained one preparation script because regenerating probabilities from authoritative large sources was a real user-facing capability.

## Reusable lesson

Keep `prepare/` only when all are true: the transformation is understood and stable; authoritative upstream identity is recorded; users may reasonably need to rebuild; the script's output contract is testable; routine plotting does not silently invoke the expensive step.

## Do not copy

Do not reuse the case's KDE bandwidth, sampling cap, panel order, state names or palette as scientific defaults for another ternary figure.
