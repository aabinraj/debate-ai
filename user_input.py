def user_input_node(state: dict) -> dict:
    topic = input("Enter topic for debate: ").strip()

    if len(topic) < 3:
        raise ValueError("Topic too short")

    print(f"\nStarting debate on topic: {topic}\n")
    print("Debate will run for 8 rounds total.")
    print("AgentA (Scientist) will speak on rounds: 1, 3, 5, 7")
    print("AgentB (Philosopher) will speak on rounds: 2, 4, 6, 8")
    print("Judge will decide after round 8.\n")

    return {
        **state,
        "topic": topic,
        "round": 1,
        "turn": "AgentA",  # ← START with AgentA
        "memory": {
            "turns": [],
            "summary": ""
        },
        "violations": [],
        "done": False  # ← Add done flag
    }