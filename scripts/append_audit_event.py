from __future__ import annotations
import argparse, json
from pathlib import Path
from datetime import datetime, timezone

parser = argparse.ArgumentParser()
parser.add_argument('--event-type', required=True)
parser.add_argument('--actor-id', required=True)
parser.add_argument('--actor-role', required=True)
parser.add_argument('--branch-id', required=True)
parser.add_argument('--reason', required=True)
parser.add_argument('--object-id', action='append', default=[])
args = parser.parse_args()

now = datetime.now(timezone.utc).isoformat()
event = {
  'audit_event_id': 'audit:' + now.replace(':','').replace('+','Z'),
  'event_type': args.event_type,
  'timestamp': now,
  'actor_id': args.actor_id,
  'actor_role': args.actor_role,
  'object_ids': args.object_id,
  'branch_id': args.branch_id,
  'reason': args.reason,
  'validation_status': 'manual_entry'
}
path = Path('audit/events') / (now[:10] + '.jsonl')
path.parent.mkdir(parents=True, exist_ok=True)
with path.open('a', encoding='utf-8') as f:
    f.write(json.dumps(event, ensure_ascii=False) + '\n')
print(json.dumps(event, indent=2, ensure_ascii=False))
