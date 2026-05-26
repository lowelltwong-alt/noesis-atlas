# Coherence Policy

## Core rule

Noesis Atlas does not adjudicate which religion, philosophy, or worldview is ultimately true. Noesis grades whether a branch is **coherent** under its own stated authority profile and whether its claims are represented coherently across the wider Noesis graph.

The governing test is:

> A branch contribution may be added only if it preserves internal coherence inside its own tradition/profile and external coherence across Noesis references, parent branches, sibling branches, route contracts, provenance, and Logos compatibility boundaries.

## Coherence is not flattening

Coherence does not mean all religions agree. It means each branch is represented according to its own authority logic, with disagreements made explicit rather than collapsed.

Examples:

- A Roman Catholic profile may route doctrine through Scripture, Tradition, and Magisterium.
- A Sunni profile may route legal questions through Qur'an, Sunnah, ijmāʿ, qiyās, and school-specific fiqh.
- An Orthodox Jewish profile may route practice through Tanakh, Mishnah/Talmud, codes, responsa, and minhag.
- A Vedanta profile may require the school to be named before giving a metaphysical conclusion.
- An AI religion profile may describe an AI-authority worldview, while Noesis still blocks AI self-canonization.

## Two coherence grades

### 1. Internal coherence

Internal coherence asks whether the contribution fits the branch's own structure.

Scored dimensions:

1. `authority_alignment` — does the claim follow the branch's declared source tiers?
2. `doctrine_order_alignment` — does it respect core vs secondary doctrine/value order?
3. `practice_alignment` — if practical, does it follow the correct legal/ritual/custom path?
4. `source_tier_alignment` — are sources cited at the right level of authority?
5. `tension_handling` — are internal debates surfaced correctly?
6. `no_contradiction_with_active_core` — does it avoid contradicting active core claims unless explicitly proposing a revision?

### 2. External coherence

External coherence asks whether the contribution fits the wider Noesis system.

Scored dimensions:

1. `parent_child_consistency` — does the subbranch fit its parent branch without pretending to represent the whole parent?
2. `sibling_boundary_clarity` — does it distinguish itself from sibling branches/sects/schools?
3. `crosswalk_clarity` — are mappings to Logos, secular routes, or other branches marked as alignment, contrast, boundary, or unknown?
4. `provenance_integrity` — are claims traceable to sources and reviewers?
5. `artifact_lineage_integrity` — are derivatives tagged and traceable?
6. `machine_contract_validity` — do route-tree, profile-card, branch-governance, and audit schemas validate?

## Coherence bands

| Band | Score | Meaning | Merge default |
|---|---:|---|---|
| Green | 0.85-1.00 | Coherent enough for active/curated use | Allowed if review requirements pass |
| Yellow | 0.65-0.84 | Coherent enough for experimental use, but needs review | Experimental or community only |
| Orange | 0.45-0.64 | Material gaps or unresolved tension | Quarantine or revision required |
| Red | 0.00-0.44 | Contradictory, unsupported, or wrong branch authority | Reject or quarantine |

## Critical fail conditions

A contribution fails regardless of numeric score if it:

- claims to represent an entire religion while only representing a sect/school;
- treats a lower-tier source as if it overrides a higher-tier branch authority;
- collapses known internal pluralism into one answer without a branch policy;
- routes branch-specific authority into Logos as if Logos endorsed it;
- lets AI-generated claims become primary authority;
- cites no provenance for a normative claim;
- changes a branch's authority structure without branch-head review.

## Output requirement

Every non-trivial branch contribution must produce a `CoherenceReport`:

```text
internal_score
external_score
overall_score
band
blocking_failures
warnings
review_required
recommended_lifecycle_state
```
