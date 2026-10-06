import os

from trail_pal.utils.llm import ask_llm
from trail_pal.tools.faqAgent import FaqAgent
from trail_pal.tools.memoryAgent import MemoryAgent
from trail_pal.tools.weather import WeatherAgent


WELCOME = """
Assistant: Hi! I'm the Trail Pal assistant. I can help with:
  - Tours, prices, booking and what to bring
  - Today's weather for your tour (try: "Is it raining right now?") — today only, no forecasts
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
        print(f"Assistant : {ask_llm(user_input)}")

    else:
        print(f"Assistant : {ask_llm(user_input)}")


def run_chat(faqAgent: FaqAgent) -> None:
    print(WELCOME)

    while True:
        user_input = input("You       : ")
        if user_input.strip().lower() == "exit":
            break
        res = faqAgent.answer(user_input)

        if res == -1:
            route_query(user_input)
        else:
            print(f"Assistant : {res}")
