from trail_pal.utils.load import load_text
from trail_pal.utils.parse import parse_faq
from trail_pal.tools.faqAgent import FaqAgent
from trail_pal.cli import run_chat
from trail_pal.utils.llm import ask_llm


def main() -> None:

    # process the document
    texts = load_text()
    faq_pairs = parse_faq(texts)

    faq_questions = [pair["question"] for pair in faq_pairs]
    faq_answers = [pair["answer"] for pair in faq_pairs]

    faqAgent = FaqAgent(faq_questions, faq_answers)

    while True:
        query = str(input("Enter: "))
        if query == "exit":
            break
        
        res = faqAgent.answer(query)

        if res == -1:
            print(ask_llm(query))
        else:
            print(res)


if __name__ == "__main__":
    main()
