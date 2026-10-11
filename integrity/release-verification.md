# Release verification chain

## Build and publish

1. Pin workflow actions to reviewed commit SHAs and production dependencies to reviewed versions or immutable digests.
2. Build from a reviewed commit in an isolated CI identity with only the permissions needed for publication.
3. Scan source, dependencies, build output, and the final artifact.
4. Generate an SPDX or CycloneDX SBOM for the final immutable artifact.
5. Publish by digest, then sign that digest with short-lived OIDC identity.
6. Attach the SBOM and build provenance as digest-bound attestations.
7. Retain the workflow run, source commit, digest, scan result, SBOM, signature, and attestation references.

## Verify before deployment

```bash
cosign verify \
  ghcr.io/OWNER/IMAGE@sha256:DIGEST \
  --certificate-identity "https://github.com/OWNER/REPO/.github/workflows/release.yml@refs/heads/main" \
  --certificate-oidc-issuer "https://token.actions.githubusercontent.com"

cosign verify-attestation \
  ghcr.io/OWNER/IMAGE@sha256:DIGEST \
  --type spdxjson \
  --certificate-identity "https://github.com/OWNER/REPO/.github/workflows/release.yml@refs/heads/main" \
  --certificate-oidc-issuer "https://token.actions.githubusercontent.com"
```

Replace every placeholder with values taken from a verified release. Prefer the exact workflow identity over a broad regular expression.

## Failure handling

- Stop deployment when digest, signature identity, issuer, attestation, or policy checks fail.
- Preserve the rejected artifact metadata and verification output in the protected evidence store.
- Revoke or rotate compromised signing identities and rebuild from a reviewed source state.
- Re-scan retained SBOMs when new vulnerabilities are disclosed.
- Remember: a valid signature proves origin under a signing identity; it does not prove the code is safe.

