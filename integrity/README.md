# Artifact integrity

Integrity controls answer four different questions:

1. **Byte identity** — does the file match an independently obtained checksum?
2. **Inventory** — which packages and components are in the artifact?
3. **Provenance** — which trusted workflow and identity produced it?
4. **Risk state** — do current scans and reviews identify unacceptable vulnerabilities or behavior?

No single artifact answers all four. See [`release-verification.md`](release-verification.md) for the complete chain and [`checksum/`](checksum/) for a small local verifier.

