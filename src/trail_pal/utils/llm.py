from dotenv import load_dotenv
from groq import Groq
from pathlib import Path

load_dotenv()
ROOT = Path(__file__).resolve().parents[3]

MODEL = "openai/gpt-oss-20b"
INSTRUCTIONS = (ROOT/ "docs" / "instructions.md").read_text(encoding="utf-8")

def ask_llm(query: str):
    try:
        client = Groq()
        completion = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": INSTRUCTIONS},
                {"role": "user", "content": query}
            ],
            temperature=1,
            max_completion_tokens=2048,
            top_p=1,
            reasoning_effort="medium",
            stream=False,
            stop=None,
        )
        return completion.choices[0].message.content or ""

    except Exception as e:
        print(f"Error: {e}\n")
        return
