from __future__ import annotations
from pathlib import Path

required = ['README.md', 'profile-card.yaml', 'branch-governance.yaml', 'CONTRIBUTING.md']
errors = []
scanned = 0
for profile in Path('branches').rglob('profile-card.yaml'):
    scanned += 1
    branch_dir = profile.parent
    for name in required:
        if not (branch_dir / name).exists():
            errors.append(f'{branch_dir}: missing {name}')
    text = profile.read_text(encoding='utf-8')
    for key in ['profile_id:', 'authority_structure:', 'favored_sources:', 'question_priorities:', 'provenance:']:
        if key not in text:
            errors.append(f'{profile}: missing {key}')

if errors:
    print('\n'.join(errors))
    raise SystemExit(1)
print(f'Branch profiles OK ({scanned} profile-card.yaml scanned)')
