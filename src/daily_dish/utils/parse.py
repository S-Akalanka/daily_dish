import re
from daily_dish.utils.clean import clean_text

def parse_faq(text:str)-> object:
    faq_pairs = []

    pattern = r"Q:\s*(.*?)\s*A:\s*(.*?)(?=\n\s*\d+\.\s*Q:|\Z)"

    matches = re.findall(pattern, text, re.DOTALL)

    for q,a in matches:
        faq_pairs.append({
            "question": clean_text(q.lower()),
            "answer": clean_text(a)
        })
    return faq_pairs
