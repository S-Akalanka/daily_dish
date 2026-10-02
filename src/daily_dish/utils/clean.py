import re

def clean_text(text:str) -> str:
    cleaned_text = re.sub(r"\s+"," ",text)

    return cleaned_text.strip()