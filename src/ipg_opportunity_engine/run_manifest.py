from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def write_manifest(run_dir: Path, payload: dict[str, Any]) -> Path:
    payload = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        **payload,
    }
    path = run_dir / "manifest.json"
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return path
