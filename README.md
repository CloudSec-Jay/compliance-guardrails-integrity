# Compliance Guardrails & Integrity

> **Field Project 04 of the [Cloud Operations Engineering](https://github.com/CloudSec-Jay/cloud-ops-engineering) system.** Each project lives in its own repository and links back to the hub. [Portfolio site](https://cloudsec-jay.github.io/cloud-ops-engineering/) · [Project site](https://cloudsec-jay.github.io/compliance-guardrails-integrity/)

Evidence-centered security engineering for cloud policy, deployment admission, benchmark remediation, and software supply-chain integrity.

This repository turns requirements into reviewable controls and connects each control to a validation method. It is a portfolio project, not a claim that any organization or workload is compliant.

## Control areas

| Area | Artifacts | Outcome |
|---|---|---|
| AWS guardrails | [`controls/aws/`](controls/aws/) | Prevent high-risk organization, logging, storage, Region, metadata, and IAM actions. |
| Kubernetes admission | [`controls/kubernetes/`](controls/kubernetes/) | Reject privileged Pods with an OPA policy and table-driven tests. |
| Evidence engineering | [`evidence/`](evidence/) | Map selected NIST SP 800-53 controls and record validation without storing sensitive exports. |
| Artifact integrity | [`integrity/`](integrity/) | Verify downloads, retain SBOMs, bind signatures to immutable digests, and check signer identity. |

## Control lifecycle

1. **Interpret** — identify the risk and the exact behavior to constrain.
2. **Enforce** — place a preventive or detective control at the narrowest useful boundary.
3. **Verify** — test allowed, denied, and failure-path behavior in a non-production scope.
4. **Record** — retain sanitized evidence tied to an immutable artifact, change, or assessment.
5. **Reassess** — review exceptions, drift, and newly disclosed vulnerabilities on a defined schedule.

## Validation

```bash
python3 -m unittest discover -s integrity/checksum/tests -v
python3 -m json.tool controls/aws/organization-guardrails.json >/dev/null
opa check controls/kubernetes/
opa test controls/kubernetes/
```

The CI workflow runs the checks available without cloud credentials. AWS policy simulation and organization rollout remain explicit operator steps.

## Field evidence reviewed

This project consolidates patterns proven or documented across the portfolio while keeping workload-specific implementation in its owning repository:

- [Cloud Operations Engineering](https://github.com/CloudSec-Jay/cloud-ops-engineering): AWS policies, OPA, evidence templates, CIS remediation, SBOM and signing workflows.
- [Hardened AWS Workload (Dragonwilds on AWS)](https://github.com/CloudSec-Jay/dragonwilds-aws): workload-specific CIS audit and hardening decisions.
- [Kubernetes SecOps Platform](https://github.com/CloudSec-Jay/k8s-secops-platform): file-integrity evidence and CIS assessment content.
- [AI/ML Security](https://github.com/CloudSec-Jay/ai-ml-security): model and MCP package integrity boundaries.

Archived repositories were reviewed as source material only and were not modified.

## Safety notes

- SCPs and permission boundaries do not grant access; evaluate the full AWS authorization path.
- Test deny policies in a non-production organizational unit with reviewed break-glass access.
- A signature establishes provenance, not safety. An SBOM establishes inventory, not vulnerability status.
- Do not commit credentials, account IDs, private evidence, raw assessment exports, or unredacted logs.

## Project site

[View the GitHub Pages case study](https://cloudsec-jay.github.io/compliance-guardrails-integrity/).

