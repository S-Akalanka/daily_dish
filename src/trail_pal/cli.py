# from pathlib import Path

from trail_pal.utils.llm import ask_llm
from trail_pal.tools.faqAgent import FaqAgent
from trail_pal.tools.memoryAgent import MemoryAgent
from trail_pal.tools.weather import WeatherAgent

# PATH = Path(__file__).resolve().parents[2]/"docs"/"logs.txt"

WELCOME = """
Assistant: Hi! I'm the Trail Pal assistant. I can help with:
  - Tours, prices, booking and what to bring
  - Today's weather for your tour (try: "Is it raining right now?"), today only, no forecasts
  - Cancellation and refund policies

Type 'exit' to quit.
"""

LOCATION = "Nuwara Eliya"

weather_keywords = [
        "weather", "rain", "raining", "forecast",
        "temperature", "hot", "cold", "humidity"
]

memory_agent = MemoryAgent()
weather_agent = WeatherAgent(memory_agent)


def route_query(user_input: str) -> str:
    if any(word in user_input.lower() for word in weather_keywords):
        weather_info = weather_agent.answer(LOCATION)
        user_input = f"{user_input}\n\n{weather_info})"
        print(f"Assistant : {ask_llm(user_input, memory_agent)}")

    else:
        print(f"Assistant : {ask_llm(user_input, memory_agent)}")


def run_chat(faqAgent: FaqAgent) -> None:
    print(WELCOME)

    while True:
        user_input = input("You       : ")
        if user_input.strip().lower() == "exit":
            # with open(PATH, 'w', encoding="utf-8") as file:
            #     file.write(str(memory_agent.recall("history")))
            break

        res = faqAgent.answer(user_input)

        if res == -1:
            route_query(user_input)
        else:
            print(f"Assistant : {res}")
            memory_agent.store_chat({"role": "user", "content": user_input})
            memory_agent.store_chat({"role": "assistant", "content": res})
