from trail_pal.utils.llm import ask_llm
from trail_pal.tools.faqAgent import FaqAgent


WELCOME = """
Assistant: Hi! I'm the Trail Pal assistant. I can help with:
  - Tours, prices, booking and what to bring
  - Weather forecasts for your tour day (try: "Will it rain on my hike tomorrow?")
  - Cancellation and refund policies

Type 'exit' to quit.
"""

def run_chat(faqAgent: FaqAgent) -> None:
    print(WELCOME)

    while True:
        user_input = input("You       : ")
        if user_input.strip().lower() == "exit":
            break
        res = faqAgent.answer(user_input)

        if res == -1:
            print(f"Assistant : {ask_llm(user_input)}")
        else:
            print(f"Assistant : {res}")
