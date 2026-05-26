from __future__ import annotations
import json
from pathlib import Path

errors = []
for path in Path('.').rglob('*.json'):
    if '.git' in path.parts:
        continue
    try:
        json.loads(path.read_text(encoding='utf-8'))
    except Exception as exc:
        errors.append(f'{path}: {exc}')

if errors:
    print('\n'.join(errors))
    raise SystemExit(1)
print('JSON syntax OK')
