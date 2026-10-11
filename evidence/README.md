# Evidence engineering

Compliance work is credible only when a control, test, observation, and retained record can be connected without overstating the result.

## Evidence rules

- Record the system, environment, owner, test window, expected result, observed result, and reviewer.
- Preserve the immutable policy, artifact digest, workflow run, commit, or configuration version that was assessed.
- Test the allowed path, denied path, and rollback or recovery path.
- Keep raw exports and sensitive logs in an approved protected store, not this repository.
- Treat a framework mapping as context. It is not a certification or proof of operating effectiveness.
- Record gaps and exceptions with owners and review dates instead of marking them as passing.

Use [`control-evidence-template.md`](control-evidence-template.md) for assessments and [`nist-800-53-map.md`](nist-800-53-map.md) for the current evidence map.

