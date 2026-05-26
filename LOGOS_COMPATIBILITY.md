# Logos Compatibility Contract

Noesis Atlas is built to work with Logos later, but remains separate from Logos.

## Boundary rule

> Noesis classifies worldview and authority structures. Logos interprets approved mappings under Christian theological authority.

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
