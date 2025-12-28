import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise RuntimeError("OPENROUTER_API_KEY not found")

# Create OpenRouter client (OpenAI-compatible)
client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

# Simple test prompt
response = client.chat.completions.create(
    model="openai/gpt-4o-mini",  # free/cheap, widely available
    messages=[
        {"role": "user", "content": "Say hello in one short sentence."}
    ],
    temperature=0.5
)

print("OpenRouter response:")
print(response.choices[0].message.content)
