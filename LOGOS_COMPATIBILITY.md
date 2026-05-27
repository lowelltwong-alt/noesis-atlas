# Logos Compatibility Contract

Noesis Atlas is built to work with Logos later, but remains separate from Logos.

## Boundary rule

> Noesis classifies worldview and authority structures. Logos interprets approved mappings under Christian theological authority.

## Authority direction (non-negotiable)

> Noesis may inform Logos. Noesis may never govern Logos.

Authority flows in exactly one direction and never returns:

`Noesis (classify) -> reviewed export -> Logos-side review -> Logos (decide under Christian authority)`

Concretely, Noesis and everything it produces:

- is **advisory and non-authoritative** to Logos. A Noesis classification, coherence score, branch ruling, lifecycle state, or constitutional rule never settles, gates, vetoes, promotes, or demotes anything in Logos.
- never becomes the **authority, source, or derivation basis** of a Logos doctrine, claim, ordering, weighting, or governance rule.
- carries **no binding force**. Logos reaches its own conclusion under its own authority and owes Noesis no deference.

Noesis governance has no jurisdiction over Logos. The Noesis constitution governs Noesis only. If a Noesis branch or reviewer ever attempts to bind Logos, that attempt is void by this contract.

## Every Logos export is advisory

Each object exported toward Logos must carry:

```yaml
authority_over_logos: none   # required, must always be "none"
```

An export that asserts, implies, or is configured with any value other than `none` is invalid and must not be released.

## Allowed Logos inputs

Logos may read only:

- `data/core/`
- `data/curated/`
- `data/logos_approved/`
- `branches/logos-bridge/`
- explicit files listed in `registry/logos-compatible-exports.json`

## Forbidden Logos inputs

Logos must not read by default:

- `data/community/`
- `data/quarantine/`
- `data/experimental/`
- branch proposals not approved for Logos;
- AI religion operational governance files unless explicitly marked `logos_reviewed`.

## Required fields for Logos export

Every Logos export must include:

- source object ID;
- branch profile ID;
- authority status;
- truth mode;
- evidence/provenance references;
- Logos crosswalk status;
- `authority_over_logos: none` (required; advisory only, never authoritative);
- risks: idolatry, false authority, human agency, dignity, power, formation;
- reviewer identity;
- audit event ID.

## Logos crosswalk statuses

- `compatible_reference`
- `public_reason_bridge`
- `contrastive_bridge`
- `boundary_case`
- `rival_authority`
- `not_for_logos`

## Non-negotiable

Noesis does not decide Christian doctrine for Logos. It supplies classified, reviewed, provenance-rich comparison objects.
