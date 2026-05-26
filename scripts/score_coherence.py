from __future__ import annotations
import argparse
import json
from pathlib import Path

INTERNAL_WEIGHTS = {
    'authority_alignment': 0.25,
    'doctrine_order_alignment': 0.20,
    'practice_alignment': 0.15,
    'source_tier_alignment': 0.15,
    'tension_handling': 0.15,
    'no_contradiction_with_active_core': 0.10,
}
EXTERNAL_WEIGHTS = {
    'parent_child_consistency': 0.20,
    'sibling_boundary_clarity': 0.15,
    'crosswalk_clarity': 0.20,
    'provenance_integrity': 0.20,
    'machine_contract_validity': 0.15,
    'lifecycle_fit': 0.10,
}

def weighted_score(dimensions: dict[str, float], weights: dict[str, float]) -> float:
    missing = set(weights) - set(dimensions)
    if missing:
        raise ValueError(f'missing dimensions: {sorted(missing)}')
    return sum(float(dimensions[k]) * weights[k] for k in weights)

def band(score: float) -> str:
    if score >= 0.85: return 'green'
    if score >= 0.65: return 'yellow'
    if score >= 0.45: return 'orange'
    return 'red'

def main() -> int:
    parser = argparse.ArgumentParser(description='Score a Noesis coherence report or dimension file.')
    parser.add_argument('path', help='JSON file containing internal.dimensions and external.dimensions')
    args = parser.parse_args()
    data = json.loads(Path(args.path).read_text(encoding='utf-8'))
    internal = data.get('internal', {}).get('dimensions', data.get('internal_dimensions', {}))
    external = data.get('external', {}).get('dimensions', data.get('external_dimensions', {}))
    i = weighted_score(internal, INTERNAL_WEIGHTS)
    e = weighted_score(external, EXTERNAL_WEIGHTS)
    overall = 0.6 * i + 0.4 * e
    print(json.dumps({'internal_score': round(i,3), 'external_score': round(e,3), 'overall_score': round(overall,3), 'band': band(overall)}, indent=2))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
