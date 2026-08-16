import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
fixture = json.loads((root / "references/evaluation-fixtures.json").read_text(encoding="utf-8"))
record = json.loads((root / "tests/fixtures/representative-record.json").read_text(encoding="utf-8"))
assert fixture["fixtures"], "no evaluation fixture"
assert record["skill_id"] == fixture["skill_id"]
assert record.get("status")
assert record.get("next_action")
print(f"PASS: {root.name} fixture contract")
