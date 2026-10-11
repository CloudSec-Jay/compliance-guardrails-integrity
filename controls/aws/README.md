# AWS guardrails

The examples are starting points for review and simulation, not drop-in production policies.

## Files

- `organization-guardrails.json` contains independent deny statements for leaving an organization, root activity, disabling CloudTrail, weakening S3 public-access blocks, launching instances without IMDSv2, and operating outside approved Regions.
- `developer-permission-boundary.json` limits a developer role to a small service set and explicitly denies common escalation and destructive paths.

## Deployment sequence

1. Parse and lint each JSON document.
2. Review every action, exception, condition key, global-service exclusion, and `NotAction` entry.
3. Simulate representative principals and requests where AWS supports it.
4. Attach the policy to a non-production organizational unit or test role.
5. Run positive and negative tests with break-glass access available.
6. Record the policy version, target, reviewer, observed behavior, and rollback result.
7. Expand scope only after the evidence is reviewed.

Service control policies set a permissions ceiling. Permission boundaries set the maximum permissions an identity policy can grant. Neither policy grants access by itself.

