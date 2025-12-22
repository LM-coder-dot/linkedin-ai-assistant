def decide_post(analysis: dict) -> tuple[str, str]:
    relevance = int(analysis.get("relevance", 0))
    highlight = int(analysis.get("highlight", 0))
    keywords = analysis.get("keywords", [])
    language = analysis.get("language")

    keyword_set = {k.lower() for k in keywords}

    # Hard stops
    if relevance < 3:
        return "ignore", "Relevance < 3"

    if language not in ("de", "en"):
        return "ignore", f"Unsupported language: {language}"

    # Repost (high value only)
    if (
        relevance >= 7
        and highlight >= 7
        and keyword_set & {"ai", "strategy", "leadership", "innovation"}
    ):
        return "repost", "High relevance & highlight with strategic keywords"

    # Comment
    if relevance >= 5 and highlight >= 4:
        return "comment", "Good relevance & discussion potential"

    # Like
    if relevance >= 3:
        return "like", "Relevant but low discussion value"

    return "ignore", "Fallback"
