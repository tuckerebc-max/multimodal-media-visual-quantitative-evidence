import hashlib
import json
from pathlib import Path
root = Path(__file__).resolve().parents[1]
checksums = {}
for p in sorted(root.rglob("*")):
    if p.is_file() and "__pycache__" not in p.parts and p.name != "checksums.json":
        checksums[str(p.relative_to(root)).replace("\\", "/")] = hashlib.sha256(p.read_bytes()).hexdigest()
(root / "catalog/checksums.json").write_text(json.dumps(checksums, indent=2) + "\n", encoding="utf-8")
print(f"WROTE {len(checksums)} checksums")
