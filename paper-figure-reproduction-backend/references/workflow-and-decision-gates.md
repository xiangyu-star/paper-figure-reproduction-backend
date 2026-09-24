# Workflow and decision gates

Each stage uses `goal → input → operation → decision → output → check`. Do not advance through an unresolved hard gate.

## 1. Intake and identity

- Goal: identify exactly one paper panel and requested task.
- Input: title/DOI, figure label, reference image, user files, requested language/status.
- Operation: normalize DOI and panel; determine whether the target is one panel, a composite, or an author-modified image; check corrections/retractions.
- Decision: if panel identity or a claim-defining quantity is ambiguous, stop and request the missing fact. If only display details are uncertain, continue with the uncertainty recorded.
- Output: completed `templates/case-intake.md` and initial status.
- Check: paper, panel, source baseline, language, and task class appear consistently in README, manifest, contract, and report.

## 2. Source discovery

- Goal: locate authoritative code, data, and reference image.
- Input: official paper/correction, supplementary/Source Data, author repository, deposit.
- Operation: record URL, repository path, commit/tag, notebook cell/function, data object, file size/hash, access state, license/redistribution boundary.
- Decision: direct author source outranks derived or style sources; a visually similar implementation is not author exact.
- Output: `source_manifest.json`, `docs/SOURCE_MAP.md`.
- Check: every decisive plotted object has one provenance class and one package destination.

## 3. Scientific contract

- Goal: prevent visual reverse engineering from silently defining science.
- Input: author code, caption/method, source data, user-authorized modifications.
- Operation: specify schemas, keys, category and panel order, filters, transforms, normalization, statistics, coordinate construction, label/color semantics, randomness, and hard failures.
- Decision: conflicting sources stay explicit. Prefer the current official source only when it resolves the conflict; otherwise mark pending and lower status.
- Output: `docs/SCIENTIFIC_CONTRACT.md`, parameter candidate table.
- Check: a new executor could decide whether an input is valid without seeing the desired picture.

## 4. Figure-ready boundary

- Goal: minimize routine input without losing scientific honesty.
- Input: upstream objects and the scientific contract.
- Operation: preserve only fields required to render and audit; retain stable identifiers, orders, mappings, provenance and hash.
- Decision:
  - routine rendering does not need upstream matrices → exclude them;
  - users need to rebuild and the transformation is stable → keep a `prepare/` script;
  - preparation is only maintainer QA → keep it outside the ZIP;
  - derivation cannot be explained → do not label the compact input `AUTHOR_DERIVED`.
- Output: real `example_input/` plus README; optional `prepare/`.
- Check: no hidden synthetic fallback; missing/empty/wrong-schema data fails.

## 5. Implementation

- Goal: provide a simple user entry and stable backend.
- Input: scientific contract and Figure-ready input.
- Operation: main builds one config; plot validates, computes/loads scientific objects, renders, exports, writes evidence, verifies, then writes success.
- Decision: expose a parameter only if a user can reasonably choose it and its downstream effects are documented. Hard-code structural invariants with an explanation.
- Output: main, plot, backend contract.
- Check: all paths relative; one routine entry; no notebook-as-entry; no silent fallback.

## 6. Execution and visual repair

- Goal: prove current execution and match reference without corrupting science.
- Input: current code/input/config and best legal reference.
- Operation: run main and replay config; compare equal-size full panel and critical crops; classify differences as scientific, rendering, export, or reference uncertainty.
- Decision: scientific differences return to stages 2–4. Rendering differences may change geometry/font/color/layer parameters while the scientific layer is frozen. After two failed visual iterations, measure anchors/pixels.
- Output: current evidence and validation artifacts outside the release where appropriate.
- Check: identical scientific hashes during visual-only repair; success marker newest and last.

## 7. Reports and release

- Goal: make the backend understandable and portable.
- Input: current evidence only.
- Operation: adapt CN/EN Rmd, render HTML, browser-inspect, static-audit, fresh-copy replay, trim, ZIP, hash.
- Decision: a failed/omitted gate prevents `COMPLETE`. Remove any file that does not help run, understand, reproduce, or audit the backend.
- Output: one validated minimal ZIP and external maintainer validation record.
- Check: no runtime, cache, local path, token, stale candidate, browser profile, overlay, probe, or release ledger in the ZIP.
