# Edge cases and status choices

## Public data exists but is not executed

Record canonical URLs, sizes/hashes when known, access state and exact next command. Use `SOURCE_READY`, not COMPLETE.

## Exact author data missing, public reconstruction possible

Separate author evidence from inferred transforms and reconstructed values. Use `APPROXIMATE_PUBLIC_RECONSTRUCTION`; do not present pixel similarity as scientific equivalence.

## Missing layer dominates the claim

If the unavailable layer defines the conclusion—such as the underlying statistic, alignment or model output—use `BLOCKED` or `ABANDON_NOT_SUITABLE`. A decorative approximation cannot rescue the claim.

## Reference image cannot be redistributed

Record its canonical source and local validation use, omit it from the public ZIP, and state how a maintainer can supply it for visual audit.

## Existing package has stale success and HTML

Treat all prior evidence as untrusted until current main/replay runs. Remove success before execution, regenerate plots and reports, then re-run all gates. Do not inherit a previous COMPLETE label.

## User requests a style adaptation

Keep author scientific values and semantic mappings frozen. Record the adapted elements as `USER_MODIFIED_BASELINE`, expose relevant display parameters and retain an author-style reference when lawful.
