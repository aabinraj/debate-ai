import json
from datetime import datetime


def logger_node(state: dict) -> dict:
    if "log_path" not in state:
        raise RuntimeError("Logger received no log_path in state")

    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "round": state.get("round"),
        "turn": state.get("turn"),
        "last_message": state.get("last_message"),
        "violations": state.get("violations", []),
    }

    with open(state["log_path"], "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry) + "\n")

    return state  # ✅ DO NOT MODIFY STATE
