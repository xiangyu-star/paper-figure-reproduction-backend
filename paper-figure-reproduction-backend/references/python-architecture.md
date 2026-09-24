# Python architecture

Use the author's Python ecosystem where available; do not translate merely for template consistency.

## main.py

- Resolve project root from `__file__`.
- Put user-editable constants or a single `PARAMS` mapping at the top.
- Group parameters by semantic role and construct a JSON-serializable config.
- Call exactly one backend function and propagate its exit code.
- Avoid data acquisition, notebook state and hidden environment assumptions.

## plot.py

Preferred order:

```text
read/receive config
→ resolve project-relative paths
→ remove stale success
→ validate config and input
→ compute/load scientific plot objects
→ render
→ export PNG/PDF
→ write resolved parameters, plot data/statistics, validation, log and run manifest
→ verify required non-empty outputs
→ write success marker last
```

Provide `--config` replay even when normal users run `main.py`. Write text/JSON evidence atomically where feasible. Explicitly close figures and use deterministic seeds for every stochastic step. Return non-zero on hard failure.

Configuration paths are relative to package root in serialized evidence. Resolve them only at runtime; do not write absolute local paths back into deliverables.

Separate functions for validation, scientific computation, rendering, export and evidence when that separation improves testing. Do not split tiny one-use operations into performative abstractions.

## Test expectations

- invalid schema/domain/category/order fails;
- missing or empty input fails;
- invalid colors/ranges fail;
- main and config replay produce equivalent scientific evidence;
- failed run has no current success marker;
- required outputs are non-empty;
- run manifest hashes identify current inputs/code/outputs when feasible.
