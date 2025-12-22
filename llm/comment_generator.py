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


def generate_comment(text: str, keywords: list[str], language: str) -> str:
    if language == "de":
        return (
            f"Spannender Punkt zu {', '.join(keywords[:2])}. "
            "Gerade in diesem Kontext ein wichtiges Thema – danke fürs Teilen!"
        )

    return (
        f"Interesting perspective on {', '.join(keywords[:2])}. "
        "This is becoming increasingly relevant – thanks for sharing!"
    )
