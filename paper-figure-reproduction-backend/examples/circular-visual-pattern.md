# Example: circular label geometry and release trimming

## Input situation

The scientific table was small and author-derived. Early renders looked broadly similar but failed on outer label orientation, curved category labels, center overlap counts, font scale and small typography. An early package also carried preparation/source files not needed for routine plotting.

## Decision

The final backend used explicit polar geometry, curved text support, named radii/font/angle parameters and a few justified sector corrections. It removed unnecessary preparation, regenerated HTML after plot changes and kept only main, plot, compact input, evidence, reports and contracts.

## Reusable lesson

For circular figures, visual acceptance requires geometric checks, not general resemblance. Keep order and values frozen; parameterize causal display geometry; after repeated misses measure angles/anchors/bounds. Re-render and inspect HTML after every accepted figure update.

## Failure indicators

- labels flip or read inward unexpectedly;
- category text is centered by eye rather than arc midpoint;
- increasing font size creates overlap without adjusting radius/canvas;
- center counts are positioned with unexplained nudges;
- HTML still embeds the previous PNG;
- preparation exists only because an earlier template contained it.
