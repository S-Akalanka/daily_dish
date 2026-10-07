from dotenv import load_dotenv
from groq import Groq
from pathlib import Path
from trail_pal.tools.memoryAgent import MemoryAgent

import re

load_dotenv()
ROOT = Path(__file__).resolve().parents[3]

MODEL = "openai/gpt-oss-20b"
INSTRUCTIONS = (ROOT/ "docs" / "instructions.md").read_text(encoding="utf-8")

def ask_llm(prompt: str, memory:MemoryAgent):
    try:
        client = Groq()
        history = get_history(memory)

        completion = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": INSTRUCTIONS},
                *history,
                {"role": "user", "content": prompt}
            ],
            temperature=1,
            max_completion_tokens=1024,
            top_p=1,
            reasoning_effort="medium",
            stream=False,
            stop=None,
        )
        response = completion.choices[0].message.content or ""

        filtered = filter_prompt(prompt)
        memory.store_chat({"role": "user", "content": filtered})
        memory.store_chat({"role": "assistant", "content": response})
        return response

    except Exception as e:
        print(f"Error: {e}\n")
        return


def filter_prompt(prompt:str)->str:
    pattern = r"\{'role':\s*'system',\s*'content':\s*'.*?'\}"

    if re.search(pattern, prompt):
        prompt = re.sub(pattern, "",prompt)
    return prompt


def get_history(memory:MemoryAgent):
    history = memory.recall("history")
    return history
