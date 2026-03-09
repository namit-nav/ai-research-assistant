import re


def clean_text(text):
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)

    # Remove very long numbers or codes
    text = re.sub(r'\b\d{10,}\b', '', text)

    # Limit text size
    text = text[:5000]

    return text