TOPICS = {
    "ai": 2,
    "artificial intelligence": 2,
    "fintech": 2,
    "bank": 1,
    "banking": 1,
    "crypto": 1,
    "blockchain": 1,
    "digital": 1,
    "market": 1,
    "finance": 1,
}

BUZZWORDS = {
    "trend": 1,
    "future": 1,
    "transform": 1,
    "disrupt": 1,
    "innovation": 1,
    "growth": 1,
    "risk": 1,
    "opportunity": 1,
    "challenge": 1,
}

OPINION_MARKERS = {
    "i think": 1,
    "in my opinion": 1,
    "we need": 1,
    "should": 1,
    "must": 1,
    "important": 1,
    "critical": 1,
    "key": 1,
}

TIME_MARKERS = {
    "today": 1,
    "now": 1,
    "currently": 1,
    "2024": 1,
    "2025": 1,
    "this year": 1,
}

MAX_SCORE = 10


def relevance_score(text: str) -> tuple[int, dict]:
    text_lower = text.lower()
    score = 0
    signals = {
        "topics": [],
        "buzzwords": [],
        "opinions": [],
        "time": [],
        "length": 0,
    }

    # 1️⃣ Topics
    for word, weight in TOPICS.items():
        if word in text_lower:
            score += weight
            signals["topics"].append(word)

    # 2️⃣ Buzzwords
    for word, weight in BUZZWORDS.items():
        if word in text_lower:
            score += weight
            signals["buzzwords"].append(word)

    # 3️⃣ Meinung
    for phrase, weight in OPINION_MARKERS.items():
        if phrase in text_lower:
            score += weight
            signals["opinions"].append(phrase)

    # 4️⃣ Aktualität
    for phrase, weight in TIME_MARKERS.items():
        if phrase in text_lower:
            score += weight
            signals["time"].append(phrase)

    # 5️⃣ Textlänge
    word_count = len(text.split())
    if word_count >= 30:
        score += 2
        signals["length"] = 2
    elif word_count >= 12:
        score += 1
        signals["length"] = 1

    score = min(score, MAX_SCORE)

    return score, signals
