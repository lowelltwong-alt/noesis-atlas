from __future__ import annotations
from pathlib import Path

forbidden = ['import socket', 'import requests', 'urllib', 'http.server', 'os.system', 'subprocess', 'open(']
errors = []
for path in Path('branches').rglob('*tarpit*.py'):
    txt = path.read_text(encoding='utf-8')
    for needle in forbidden:
        if needle in txt:
            errors.append(f'{path}: forbidden pattern {needle}')
if errors:
    print('\n'.join(errors))
    raise SystemExit(1)
print('Easter eggs safe')
