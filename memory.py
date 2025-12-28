MAX_ROUNDS = 8 

def memory_node(state: dict) -> dict:
    # 1. Save the current message to history
    entry = {
        "round": state["round"],
        "agent": state["turn"],
        "text": state["last_message"],
        "model": state.get("agent_model"),
    }

    memory = state["memory"]
    memory["turns"].append(entry)

    # Update summary (keeping the last 1500 characters)
    memory["summary"] = " ".join(
        t["text"] for t in memory["turns"]
    )[-1500:]

    # 2. Logic to advance the debate state
    current_round = state["round"]
    next_round = current_round + 1
    
    # Debate ends AFTER AgentB finishes round 8
    is_done = next_round > MAX_ROUNDS
    
    # Only alternate turn if the debate is continuing
    if not is_done:
        next_turn = "AgentB" if state["turn"] == "AgentA" else "AgentA"
    else:
        # Keep turn as is, router will send to Judge because done=True
        next_turn = state["turn"] 
    
    print(f"[Memory] Round {current_round} complete. Next Round: {next_round}, Next Turn: {next_turn}, Done: {is_done}")

    return {
        **state,
        "memory": memory,
        "round": next_round,
        "turn": next_turn,
        "done": is_done
    }