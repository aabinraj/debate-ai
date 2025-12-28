import os
from openai import OpenAI
from utils.repetition_check import is_repeated
from utils.coherence_check import is_coherent

MODEL_A = "openai/gpt-4o"   # or anthropic/claude-3-opus, mistralai/mixtral, etc.

def agent_a_node(state: dict) -> dict:
    if state.get("turn") != "AgentA":
     raise RuntimeError(f"AgentA called out of turn. State: {state}")


    with open("personas/scientist.txt") as f:
        persona = f.read()

    client = OpenAI(
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url="https://openrouter.ai/api/v1"
    )

    prompt = f"""
{persona}

Debate topic: {state['topic']}
Previous summary: {state['memory']['summary']}

Provide ONE new scientific argument.
"""

    response = client.chat.completions.create(
        model=MODEL_A,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=800

    )

    text = response.choices[0].message.content.strip()

    if is_repeated(text, state["memory"]["turns"]):
        raise RuntimeError("Repeated argument detected (Scientist)")

    if not is_coherent(text, state["topic"]):
        state["violations"].append("Coherence issue: Scientist")

    print(f"[Round {state['round']}] Scientist (OpenRouter): {text}\n")

    return {
    **state,                     # ✅ preserve EVERYTHING
    "last_message": text,
    "agent_model": MODEL_A,
}



