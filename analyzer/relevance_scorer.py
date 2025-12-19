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


def relevance_score(text: str) -> tuple[int, list[str]]:
    text_lower = text.lower()
    score = 0
    hits = []

    for kw in ["ai", "bank", "banking", "fintech", "transform"]:
        if kw in text_lower:
            score += 1
            hits.append(kw)

    return min(score, 10), hits

