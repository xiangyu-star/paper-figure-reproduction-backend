# Source and evidence model

## Discovery priority

1. Official article page, correction, erratum, retraction and caption/method.
2. Publisher Source Data and supplementary files.
3. Author repository, release, notebook, script or package documentation at a locked commit/tag.
4. Author-designated or institutional data deposit.
5. Public reconstruction and style references, clearly separated from author evidence.

Record access date, canonical URL, version/commit, exact path/cell/function/object, file size and SHA-256 when local bytes are decisive. Record failed access and authentication boundaries; do not infer file contents from a landing page.

## Provenance classes

- `AUTHOR_EXACT`: the authors' exact paper, code, data object, mapping or output.
- `AUTHOR_DERIVED`: a compact object deterministically derived from author material with documented transformation and identity.
- `PUBLIC_RECONSTRUCTION`: a defensible non-author reconstruction based on public evidence.
- `STYLE_REFERENCE`: used only for layout or appearance; never for scientific values.
- `USER_MODIFIED_BASELINE`: a user-authorized departure such as PlotXY palette or revised annotation.

Classify per object, not once per project. A package may combine author-exact code, author-derived input and user-modified colors.

## Evidence vocabulary

Use exact statements:

- `found`: existence verified.
- `downloaded`: bytes obtained.
- `hash_verified`: identity checked.
- `mapped`: panel-to-code/object relation recorded.
- `generated`: current command created the artifact.
- `PASS`: named current-version check passed.
- `not_run`: check was not executed.
- `unavailable`: source could not be accessed.

Never turn `found` into `executed`, `downloaded` into `author exact`, or an old PASS into a current PASS.

## Required source map questions

- Which exact code determines each panel/layer?
- Which object supplies plotted values, order, labels and categories?
- Which transformations occur before routine plotting?
- Does a correction affect identity, values, labels or only metadata?
- Which file may legally be redistributed?
- What is unavailable, and does it dominate the claim?

## Conflict handling

List the conflicting claims and their dates/versions. Prefer a newer official correction only when it addresses the conflict. Prefer executable author code over a prose paraphrase for implementation details, while retaining caption/method constraints. If the conflict remains unresolved, preserve both, state the operational choice, and lower status. Never manufacture a hybrid source.

## Status vocabulary

- `COMPLETE`
- `VISUAL_REVIEW_NEEDED`
- `APPROXIMATE_PUBLIC_RECONSTRUCTION`
- `SOURCE_READY`
- `BLOCKED`
- `ABANDON_NOT_SUITABLE`

Legacy labels may be documented during repair but new output uses only these statuses.
