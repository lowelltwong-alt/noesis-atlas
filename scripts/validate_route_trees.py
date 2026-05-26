from __future__ import annotations
from pathlib import Path
import sys
import yaml

errors: list[str] = []
required = {'tree_id', 'display_name', 'status', 'root_route', 'coherence_contract', 'nodes', 'edges'}
node_required = {'id', 'label', 'node_type', 'status'}
edge_required = {'from', 'to', 'rel_type'}

for path in Path('branches').rglob('route-tree.yaml'):
    data = yaml.safe_load(path.read_text(encoding='utf-8'))
    missing = required - set(data or {})
    if missing:
        errors.append(f'{path}: missing top-level keys {sorted(missing)}')
        continue
    node_ids = set()
    for node in data.get('nodes', []):
        miss = node_required - set(node or {})
        if miss:
            errors.append(f'{path}: node missing {sorted(miss)}: {node}')
        if node.get('id') in node_ids:
            errors.append(f'{path}: duplicate node id {node.get("id")}')
        node_ids.add(node.get('id'))
    for edge in data.get('edges', []):
        miss = edge_required - set(edge or {})
        if miss:
            errors.append(f'{path}: edge missing {sorted(miss)}: {edge}')
            continue
        if edge['from'] not in node_ids:
            errors.append(f'{path}: edge source not found {edge["from"]}')
        if edge['to'] not in node_ids:
            errors.append(f'{path}: edge target not found {edge["to"]}')
    coh = data.get('coherence_contract', {})
    for key in ['internal_required', 'external_required', 'minimum_band']:
        if key not in coh:
            errors.append(f'{path}: coherence_contract missing {key}')

if errors:
    print('\n'.join(errors))
    sys.exit(1)
print('Route trees OK')
