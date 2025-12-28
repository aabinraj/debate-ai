import os
from langchain_openai import ChatOpenAI


def judge_node(state: dict) -> dict:
    llm = ChatOpenAI(
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url="https://openrouter.ai/api/v1",
        model="openai/gpt-4o-mini",
        temperature=0,
    )

    debate_text = "\n".join(
        f"{t['agent']}: {t['text']}" for t in state["memory"]["turns"]
    )

    prompt = f"""
You are a neutral judge evaluating a structured debate.

Debate topic:
{state['topic']}

Debate transcript:
{debate_text}

Your task:
1. Provide a concise debate summary
2. Declare a winner (AgentA or AgentB)
3. Give a clear, logical justification
"""

    response = llm.invoke(prompt)
    verdict = response.content

    print("\n[Judge Verdict]")
    print(verdict)

    # ✅ CRITICAL: return FULL state, not partial
    return {
        **state,
        "final_verdict": verdict,
    }
