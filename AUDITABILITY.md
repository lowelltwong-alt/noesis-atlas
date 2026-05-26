# Auditability Model

Noesis Atlas is audit-first.

## Auditable events

- node added;
- node revised;
- relationship added;
- profile card changed;
- branch governance changed;
- source root added;
- derivative lineage changed;
- promoted to curated;
- promoted to branch-approved;
- promoted to Logos-approved;
- downgraded;
- quarantined;
- deprecated;
- removed/tombstoned;
- release exported;
- Logos export generated;
- reviewer conflict declared;
- branch-head decision recorded.

## Audit event fields

Every audit event must include:

- event ID;
- timestamp;
- actor ID;
- actor role;
- changed object IDs;
- before/after hash where applicable;
- reason;
- evidence bundle IDs;
- branch profile;
- reviewer IDs;
- approval status;
- validation status;
- rollback/tombstone pointer if relevant.

## Audit storage

Use append-only JSONL in `audit/events/` for early MVP.

For later high-integrity release:

- canonicalize release manifests;
- hash artifacts;
- sign release manifests;
- optionally anchor release manifests in a transparency log or blockchain timestamp.

Blockchain may anchor a hash. It must not be treated as proof of truth.
