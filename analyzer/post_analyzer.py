def analyze_post(text: str) -> dict:
    text_lower = text.lower()

    relevance = 0
    highlight = 0

    keywords = ["ai", "künstlich", "fintech", "crypto", "bank", "automation"]

    for kw in keywords:
        if kw in text_lower:
            relevance += 2
            highlight += 1

    relevance = min(relevance, 10)
    highlight = min(highlight, 10)

    language = "de"
    if any(word in text_lower for word in ["the", "and", "is"]):
        language = "en"

    return {
        "language": language,
        "relevance": relevance,
        "highlight": highlight
    }
