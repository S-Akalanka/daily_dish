from trail_pal.utils.load import load_text
from trail_pal.utils.parse import parse_faq
from trail_pal.tools.faqAgent import FaqAgent
from trail_pal.cli import run_chat

def main() -> None:

    # process the document
    texts = load_text()
    faq_pairs = parse_faq(texts)

    faq_questions = [pair["question"] for pair in faq_pairs]
    faq_answers = [pair["answer"] for pair in faq_pairs]

    faqAgent = FaqAgent(faq_questions, faq_answers)
    run_chat(faqAgent)
    

if __name__ == "__main__":
    main()
