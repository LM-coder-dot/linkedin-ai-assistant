import re

# Gewichtete Keywords (einfach erweiterbar)
KEYWORDS = {
    # High impact
    "ai": 3,
    "artificial intelligence": 3,
    "machine learning": 3,
    "fintech": 3,
    "banking": 2,
    "finance": 2,
    "risk": 2,
    "automation": 2,

    # Medium impact
    "startup": 1,
    "digital": 1,
    "innovation": 1,
    "data": 1,
    "growth": 1,
    "platform": 1,
}

CTA_KEYWORDS = [
    "what do you think",
    "your thoughts",
    "agree",
    "discuss",
    "comment",
    "opinion"
]


def relevance_score(text: str) -> tuple[int, list[str]]:
    text_lower = text.lower()

    score = 0
    matched_keywords = []

    # 1️⃣ Keyword scoring
    for keyword, weight in KEYWORDS.items():
        if keyword in text_lower:
            score += weight
            matched_keywords.append(keyword)

    # 2️⃣ Length bonus (Substanz)
    word_count = len(re.findall(r"\w+", text))
    if word_count > 40:
        score += 1
    if word_count > 80:
        score += 1

    # 3️⃣ Engagement / CTA Bonus
    for cta in CTA_KEYWORDS:
        if cta in text_lower:
            score += 1
            break

    # 4️⃣ Clamp auf 0–10
    score = max(0, min(score, 10))

    return score, matched_keywords
