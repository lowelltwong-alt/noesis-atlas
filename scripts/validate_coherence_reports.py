from __future__ import annotations
from pathlib import Path
import json
import sys

errors: list[str] = []
for path in Path('examples/coherence-reports').glob('*.json'):
    data = json.loads(path.read_text(encoding='utf-8'))
    for key in ['report_id','target_id','target_type','internal','external','overall_score','band','audit']:
        if key not in data:
            errors.append(f'{path}: missing {key}')
    if not (0 <= data.get('overall_score', -1) <= 1):
        errors.append(f'{path}: overall_score out of range')
    if data.get('band') not in {'green','yellow','orange','red'}:
        errors.append(f'{path}: invalid band {data.get("band")}')
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print('Coherence reports OK')
