def highlight_score(text: str) -> int:
    """
    Bewertet, wie 'diskussionswürdig' / repost-würdig ein Post ist.
    Skala: 0–10
    Offline, deterministisch.
    """

    text_lower = text.lower()
    score = 0

    # 1️⃣ Länge (0–3)
    word_count = len(text.split())
    if word_count >= 60:
        score += 3
    elif word_count >= 30:
        score += 2
    elif word_count >= 15:
        score += 1

    # 2️⃣ Fragen & Call-to-Action (0–3)
    if "?" in text:
        score += 2
    if any(p in text_lower for p in ["what do you think", "your thoughts", "meinung", "diskussion"]):
        score += 1

    # 3️⃣ Meinungsstärke (0–2)
    if any(w in text_lower for w in ["must", "should", "critical", "important", "entscheidend"]):
        score += 2

    # 4️⃣ Aktualität / Trend (0–2)
    if any(w in text_lower for w in ["future", "trend", "2024", "2025", "now", "currently"]):
        score += 2

    return min(score, 10)
