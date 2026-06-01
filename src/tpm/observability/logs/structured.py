import json
from datetime import datetime, timezone
from typing import Any, Dict


class StructuredLogger:
    @staticmethod
    def log(level: str, message: str, context: Dict[str, Any] = None) -> None:
        log_entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": level.upper(),
            "message": message,
            "context": context or {},
        }
        # Dump em JSON nativo para STDOUT (preparado para collectors tipo ELK/Datadog)
        print(json.dumps(log_entry))
