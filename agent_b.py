import os
from dotenv import load_dotenv
import google.genai as genai
from utils.repetition_check import is_repeated
from utils.coherence_check import is_coherent

load_dotenv()

MODEL_B = "gemini-2.5-flash"

def agent_b_node(state: dict) -> dict:
    if state["turn"] != "AgentB":
        raise RuntimeError("AgentB called out of turn")

    with open("personas/philosopher.txt") as f:
        persona = f.read()

    client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

    prompt = f"""
{persona}

Debate topic: {state['topic']}
Previous summary: {state['memory']['summary']}

Respond philosophically with ONE new argument.
"""

    response = client.models.generate_content(
        model=MODEL_B,
        contents=prompt
    )

    text = response.text.strip()

    if is_repeated(text, state["memory"]["turns"]):
        raise RuntimeError("Repeated argument detected (Philosopher)")

    if not is_coherent(text, state["topic"]):
        state["violations"].append("Coherence issue: Philosopher")

    print(f"[Round {state['round']}] Philosopher (Gemini): {text}\n")

    return {
    **state,                     # ✅ preserve EVERYTHING
    "last_message": text,
    "agent_model": MODEL_B,
}


