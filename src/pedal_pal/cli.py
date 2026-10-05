from pedal_pal.utils.llm import ask_llm

def run_chat() -> None:
    print("\nWelcome to the chat! Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.strip().lower() == "exit":
            break

        try:
            reply = ask_llm(user_input)
        except Exception as e:
            print(f"Error: {e}\n")
            continue

        print(f"AI : {reply}\n")
