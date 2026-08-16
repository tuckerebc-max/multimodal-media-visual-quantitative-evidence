import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors = []
skill = ROOT / "SKILL.md"
text = skill.read_text(encoding="utf-8")
match = re.match(r"^---\s*\nname:\s*([^\n]+)\ndescription:\s*(.+?)\n---\s*\n", text, re.S)
if not match:
    errors.append("SKILL.md frontmatter is missing or malformed")
else:
    if match.group(1).strip() != ROOT.name:
        errors.append("frontmatter name does not match folder")
    if len(match.group(2).strip()) < 40:
        errors.append("description is too short")
for rel in ["agents/openai.yaml", "references/construct-and-source-ledger.md", "references/output-schema.json", "references/evaluation-fixtures.json", "shared/schemas/interoperability-artifact-envelope.schema.json", "tests/fixtures/representative-record.json", "catalog/release-manifest.json"]:
    if not (ROOT / rel).exists():
        errors.append(f"missing {rel}")
for rel in ["references/output-schema.json", "references/evaluation-fixtures.json", "shared/schemas/interoperability-artifact-envelope.schema.json", "tests/fixtures/representative-record.json", "catalog/release-manifest.json"]:
    p = ROOT / rel
    if p.exists():
        try:
            json.loads(p.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"invalid JSON {rel}: {exc}")
if "TODO" in text or "TBD" in text:
    errors.append("placeholder remains in SKILL.md")
if errors:
    print("FAIL")
    print("\n".join(f"- {e}" for e in errors))
    raise SystemExit(1)
print(f"PASS: {ROOT.name}")
