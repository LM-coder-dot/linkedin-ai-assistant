import random

GERMAN_TEMPLATES = [
    "Spannender Beitrag! Gerade im Kontext von {topic} ein sehr relevanter Punkt.",
    "Danke fürs Teilen – {topic} wird aktuell oft unterschätzt.",
    "Sehr interessanter Gedanke. Besonders mit Blick auf {topic}.",
]

ENGLISH_TEMPLATES = [
    "Very interesting perspective – especially in the context of {topic}.",
    "Great insight! {topic} is becoming more important than many realize.",
    "Thanks for sharing – this adds valuable context around {topic}.",
]


def detect_topic(text: str) -> str:
    text = text.lower()

    if "fintech" in text:
        return "FinTech"
    if "ai" in text or "artificial intelligence" in text:
        return "AI"
    if "bank" in text or "banking" in text:
        return "banking"
    if "crypto" in text:
        return "cryptocurrencies"
    if "digital" in text or "market" in text:
        return "digital markets"

    return "this topic"

def generate_comment(
    text: str,
    decision: str,
    relevance: int,
    keywords: list[str] | None = None,
) -> str:

    keywords_hint = ""
    if keywords:
        keywords_hint = f" Themen: {', '.join(keywords)}."

    return (
        f"Spannender Beitrag zum Thema {decision}. "
        f"Gerade im Kontext von Relevanz {relevance}/10 sehr interessant."
        f"{keywords_hint}"
    )
