from dotenv import load_dotenv
from groq import Groq

load_dotenv()

MODEL = "openai/gpt-oss-20b"


def ask_llm(query: str) -> str:
    """Send a single user message to the LLM and return its reply."""
    client = Groq()
    completion = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": query}],
        temperature=1,
        max_completion_tokens=2048,
        top_p=1,
        reasoning_effort="medium",
        stream=False,
        stop=None,
    )
    return completion.choices[0].message.content or ""
