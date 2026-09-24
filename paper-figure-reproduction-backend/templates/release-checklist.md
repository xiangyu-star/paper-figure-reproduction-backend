# Release checklist

## Identity and sources

- [ ] Paper, DOI, panel and corrections are current.
- [ ] Repository commit/tag and exact code objects are recorded.
- [ ] Every decisive object has one honest provenance class.
- [ ] Data identity, access and redistribution boundary are recorded.

## Scientific contract and input

- [ ] Schema, keys, order, transforms, statistics, mappings and randomness are explicit.
- [ ] Figure-ready input is real, compact, non-empty and traceable.
- [ ] `prepare/` exists only if routine users need upstream rebuilding.
- [ ] Hard-invalid inputs fail without synthetic fallback.

## Interface and execution

- [ ] One main and one stable plot backend exist.
- [ ] User parameters are grouped and traced end to end.
- [ ] Every parameter has an invalidation class.
- [ ] Current main run passes.
- [ ] Current CLI/config replay passes.
- [ ] Required evidence is current and non-empty.
- [ ] Stale success is removed before run; success is written last.

## Visual and reports

- [ ] Generated/reference full panels were compared at equal size.
- [ ] Claim-critical crops, text, legend, axes and layer order were checked.
- [ ] Scientific layer remained frozen during display-only fixes.
- [ ] CN/EN Rmd sections and content are mirrored.
- [ ] HTML was re-rendered after the final plot change.
- [ ] Both HTML files were browser-inspected for clipping, stale images and overflow.

## Release

- [ ] Static package audit passes.
- [ ] Fresh-copy/extraction run, replay and report render pass.
- [ ] No runtime, cache, notebook, absolute path, credential, stale or internal QA artifact remains.
- [ ] Final ZIP was created from the validated copy.
- [ ] ZIP SHA-256 and status were recorded.
- [ ] Every unrun gate is explicitly `not_run`; `COMPLETE` is used only if all required gates pass.
