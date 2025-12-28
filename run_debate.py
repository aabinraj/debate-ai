import argparse
from langgraph.graph import StateGraph, END
from dotenv import load_dotenv

from utils.seed import set_seed
from nodes.user_input import user_input_node
from nodes.coordinator import coordinator_node, coordinator_router
from nodes.agent_a import agent_a_node
from nodes.agent_b import agent_b_node
from nodes.memory import memory_node
from nodes.logger import logger_node
from nodes.judge import judge_node

load_dotenv()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument("--log-path", default="debate_log.json")
    args = parser.parse_args()

    if args.seed is not None:
        set_seed(args.seed)
        print(f"[System] Seed set to {args.seed}")

    # Initial State
    initial_state = {
        "topic": None,
        "round": 1,
        "turn": "AgentA",
        "memory": {
            "turns": [],
            "summary": ""
        },
        "violations": [],
        "log_path": args.log_path,
        "done": False 
    }

    graph = StateGraph(dict)

    # Define Nodes
    graph.add_node("UserInput", user_input_node)
    graph.add_node("Coordinator", coordinator_node)
    graph.add_node("AgentA", agent_a_node)
    graph.add_node("AgentB", agent_b_node)
    graph.add_node("Memory", memory_node)
    graph.add_node("Logger", logger_node)
    graph.add_node("Judge", judge_node)

    # Set Entry Point
    graph.set_entry_point("UserInput")

    # Define Flow
    graph.add_edge("UserInput", "Coordinator")

    graph.add_conditional_edges(
        "Coordinator",
        coordinator_router,
        {
            "AgentA": "AgentA",
            "AgentB": "AgentB",
            "Judge": "Judge",
        }
    )

    graph.add_edge("AgentA", "Memory")
    graph.add_edge("AgentB", "Memory")
    graph.add_edge("Memory", "Logger")
    graph.add_edge("Logger", "Coordinator") # Returns to Coordinator to route next turn

    graph.add_edge("Judge", END)

    # Compile and Run
    app = graph.compile()
    
    # IMPORTANT: recursion_limit set to 50 to accommodate the 8 rounds of transitions
    app.invoke(initial_state, config={"recursion_limit": 50})

if __name__ == "__main__":
    main()