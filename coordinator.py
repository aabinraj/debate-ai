MAX_ROUNDS = 8

def coordinator_node(state: dict) -> dict:
    """Pass-through node that does not mutate state."""
    return state

def coordinator_router(state: dict) -> str:
    """Determines the next step based on the 'done' flag or current 'turn'."""
    # The 'done' flag is set by the memory_node after round 8
    if state.get("done", False) or state.get("round", 0) > MAX_ROUNDS:
        return "Judge"
    
    # Otherwise, follow the turn set by memory_node
    return state["turn"]