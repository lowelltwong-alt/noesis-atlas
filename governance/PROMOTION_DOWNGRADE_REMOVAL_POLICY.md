# Promotion, Downgrade, and Removal Policy

## Lifecycle states

`proposed -> experimental -> active -> deprecated -> retired -> archived`

Quarantine and removed/tombstoned are special states.

## Promotion requirements

- evidence bundle;
- branch scope;
- reviewer approval;
- passing schema validation;
- audit event;
- no unresolved high-risk conflict.

## Downgrade triggers

- failed truth test;
- source discredited;
- provenance missing;
- branch reviewer objection;
- poisoning signal;
- Logos boundary violation.

## Removal rule

Prefer deprecation/tombstone over deletion. If removal is required, preserve a tombstone with replacement pointer and audit event.
