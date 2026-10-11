# NIST SP 800-53 Rev. 5 evidence map

This working map connects repository artifacts to selected control context. It does not establish compliance or prove operating effectiveness. Control identifiers should be revalidated against the authoritative NIST publication before an assessment.

| Control | Repository artifact | Evidence relationship | Current gap |
|---|---|---|---|
| AC-3 Access Enforcement | `controls/aws/`, `controls/kubernetes/` | Preventive policies constrain cloud and workload actions. | Target-environment decisions and denial tests are not stored here. |
| AC-6 Least Privilege | `controls/aws/developer-permission-boundary.json` | Boundary limits service and pass-role scope and denies common escalation paths. | Requires identity-policy and resource-policy evaluation in the target account. |
| AU-12 Audit Record Generation | `controls/aws/organization-guardrails.json` | SCP protects CloudTrail configuration from most principals. | Does not prove trails exist, cover all Regions, or deliver usable records. |
| CA-7 Continuous Monitoring | `evidence/control-evidence-template.md` | Template records repeated observations and follow-up. | Monitoring cadence and owners are environment-specific. |
| CM-6 Configuration Settings | `controls/kubernetes/deny_privileged.rego` | Admission policy expresses a secure workload setting. | Admission-controller integration is not implemented in this repository. |
| RA-5 Vulnerability Monitoring and Scanning | `integrity/release-verification.md` | Release flow includes source, dependency, SBOM, and artifact scanning. | Scanner configuration and remediation SLAs are workload-specific. |
| SA-10 Developer Configuration Management | `.github/workflows/validate.yml` | CI parses policies and tests code on change. | Branch rules and reviewer enforcement must be verified on GitHub. |
| SI-7 Software, Firmware, and Information Integrity | `integrity/checksum/`, `integrity/release-verification.md` | Hash verification, signatures, and attestations detect unexpected artifact changes. | Publisher trust and deployment verification remain external decisions. |
| SR-4 Provenance | `integrity/release-verification.md` | Digest-bound signatures and attestations preserve build identity. | No artifact is published by this documentation repository. |

## Maintenance

- Review after material policy, architecture, or workflow changes.
- Link claims to immutable evidence before describing a control as implemented.
- Keep control owners, assessment dates, exceptions, and protected evidence outside public source when sensitive.

