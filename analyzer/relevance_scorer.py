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

def relevance_score(text: str):
    text_lower = text.lower()
    score = 0
    hits = set()

    # 1️⃣ Topics
    for t in TOPICS:
        if t in text_lower:
            hits.add(t)
    if len(hits) >= 2:
        score += 2
    elif len(hits) == 1:
        score += 1

    # 2️⃣ Buzzwords
    buzz_hits = set()
    for b in BUZZWORDS:
        if b in text_lower:
            buzz_hits.add(b)
    hits |= buzz_hits
    if len(buzz_hits) >= 2:
        score += 2
    elif len(buzz_hits) == 1:
        score += 1

    # 3️⃣ Textlänge
    wc = len(text.split())
    if wc >= 30:
        score += 2
    elif wc >= 12:
        score += 1

    # 4️⃣ Meinung
    opinion_hits = set()
    for o in OPINION_MARKERS:
        if o in text_lower:
            opinion_hits.add(o)
    hits |= opinion_hits
    if len(opinion_hits) >= 2:
        score += 2
    elif len(opinion_hits) == 1:
        score += 1

    # 5️⃣ Zeit
    time_hits = set()
    for t in TIME_MARKERS:
        if t in text_lower:
            time_hits.add(t)
    hits |= time_hits
    if len(time_hits) >= 2:
        score += 2
    elif len(time_hits) == 1:
        score += 1

    return min(score, 10), sorted(hits)


