# Control evidence: [control or change]

| Field | Value |
|---|---|
| Owner | [team or person] |
| Environment | [development / staging / production] |
| Assessment window | [start and end] |
| Control version | [commit, policy version, or digest] |
| Related requirement | [verified framework identifier, if applicable] |

## Objective and scope

[Describe the risk, intended outcome, included systems, and explicit exclusions.]

## Preconditions

- [Required access, approvals, backups, and test data]
- [Expected baseline state]
- [Rollback owner and trigger]

## Validation procedure

1. [Static validation or policy parse]
2. [Expected allowed behavior]
3. [Expected denied behavior]
4. [Failure-path and rollback validation]

## Results

| Check | Expected | Observed | Result |
|---|---|---|---|
| [check] | [expected state] | [sanitized observation] | Pass / Fail / Not run |

## Evidence references

| Evidence | Protected location | Retention |
|---|---|---|
| [CI run, sanitized output, ticket, or assessment export] | [link or evidence-store ID] | [period] |

Do not place credentials, tokens, account IDs, private keys, unredacted resource identifiers, or sensitive logs in this file.

## Gaps and exceptions

| Gap or exception | Rationale | Compensating control | Owner | Review date |
|---|---|---|---|---|
| [item] | [reason] | [control] | [owner] | [date] |

## Rollback and recovery

[Document the rollback action, observed recovery result, and any remaining risk.]

## Reviewer statement

[State exactly what the evidence supports and what it does not establish.]

