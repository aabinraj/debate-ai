Multi-Agent Debate System (LangGraph)
Project Summary

This project implements a deterministic, multi-agent debate framework using LangGraph, where two AI agents engage in a structured, turn-based debate on a user-defined topic, followed by an automated judge verdict.

The system demonstrates state-driven agent orchestration, controlled turn sequencing, and multi-LLM integration across providers (OpenRouter + Gemini), making it suitable as a reference implementation for advanced agent workflows.

Key Capabilities

Deterministic multi-agent execution using seed control

Strict round-based debate orchestration (no infinite loops)

Cross-provider LLM integration (OpenRouter + Google Gemini)

Explicit state propagation and immutability discipline

Automatic debate memory aggregation and judging

CLI-driven execution with reproducible results

Debate Design
Agents
Role	Identity	Responsibility
AgentA	Scientist	Empirical, research-backed arguments
AgentB	Philosopher	Ethical, societal, and conceptual critique
Judge	Neutral Evaluator	Summarizes, selects winner, justifies decision
Rules

Total Rounds: 8

Turn Order:

Rounds 1, 3, 5, 7 → Scientist (AgentA)

Rounds 2, 4, 6, 8 → Philosopher (AgentB)

Judge executes only after round 8

One response per round, enforced by coordinator logic

Architecture Overview
UserInput
   ↓
Coordinator ──► AgentA / AgentB
                    ↓
                 Memory
                    ↓
                 Logger
                    ↓
               Coordinator
                    ↓
                  Judge

Design Notes

Coordinator controls flow only, not content

Agents are stateless beyond provided state

Memory node aggregates debate history

Judge evaluates complete transcript only once

Models Used
Component	Model	Provider
AgentA	GPT-4o-mini	OpenRouter
AgentB	Gemini-Pro	Google GenAI
Judge	GPT-4o-mini	OpenRouter
Installation
Clone Repository
git clone https://github.com/abinraj01/debate-ai.git
cd debate-langgraph

Install Dependencies
pip install -r requirements.txt

Environment Setup

Create a .env file:

OPENROUTER_API_KEY=your_openrouter_key
GOOGLE_API_KEY=your_google_api_key


.env is ignored via .gitignore and should never be committed.

Running the System
python run_debate.py --seed 42


You will be prompted for a debate topic:

Enter topic for debate: online education

Example Output (Condensed)
Debate will run for 8 rounds total.
AgentA speaks on odd rounds.
AgentB speaks on even rounds.
Judge will decide after round 8.

[Round 1] Scientist: ...
[Round 2] Philosopher: ...
...
[Judge Verdict]
Winner: AgentB
Justification: ...

Project Structure
.
├── run_debate.py
├── nodes/
│   ├── agent_a.py
│   ├── agent_b.py
│   ├── coordinator.py
│   ├── memory.py
│   ├── logger.py
│   ├── judge.py
│   └── user_input.py
├── utils/
│   └── seed.py
├── requirements.txt
├── .gitignore
└── README.md

Why This Project Matters

This project demonstrates:

Practical LangGraph usage beyond toy examples

Safe agent coordination without recursion failures

Real-world state handling patterns for agent systems

Multi-model orchestration in a single workflow

Engineering discipline in AI system design

It is directly applicable to:

Agentic AI systems

Debate / reasoning frameworks

Evaluation pipelines

AI research prototypes
