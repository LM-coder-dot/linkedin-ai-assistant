import random

GERMAN_TEMPLATES = [
    "Spannende Perspektive! Gerade im Kontext von {topic} sieht man aktuell viel Bewegung.",
    "Sehr relevanter Punkt – besonders wenn man die Entwicklungen in {topic} betrachtet.",
    "Das Thema {topic} wird definitiv unterschätzt. Danke fürs Teilen!"
]

ENGLISH_TEMPLATES = [
    "Very interesting perspective! Especially in the context of {topic}.",
    "Great point – we see a lot of momentum around {topic} right now.",
    "This is a highly relevant topic, particularly when looking at {topic} trends."
]


def detect_topic(text: str) -> str:
    text = text.lower()

    if "fintech" in text:
        return "FinTech"
    if "ai" in text or "artificial intelligence" in text:
        return "AI in Finance"
    if "bank" in text or "banking" in text:
        return "Banking"
    if "digital" in text or "market" in text:
        return "Digital Markets"

    return "the financial sector"


def generate_comment(post_text: str, language: str) -> str:
    topic = detect_topic(post_text)

    if language == "de":
        template = random.choice(GERMAN_TEMPLATES)
    else:
        template = random.choice(ENGLISH_TEMPLATES)

    return template.format(topic=topic)
