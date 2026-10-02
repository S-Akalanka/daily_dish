from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

def llm(query:str):
    try:
        client = Groq()
        completion = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
            {
                "role": "user",
                "content": query
            }
            ],
            temperature=1,
            max_completion_tokens=2048,
            top_p=1,
            reasoning_effort="medium",
            stream=False,
            stop=None
        )

        return completion.choices[0].message.content

    except Exception as e:
        print(f"Unexpected: {e}")

def chat():
    print("Welcome to the chat! Type 'exit' to quit.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        res = llm(user_input)
        print(f"AI : {res or ""}")
