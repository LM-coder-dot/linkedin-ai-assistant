def decide_action(analysis: dict):
    relevance = analysis.get("relevance", 0)
    highlight = analysis.get("highlight", 0)
    language = analysis.get("language", "de")

    decision = "ignore"
    comment = None

    if relevance >= 8 and highlight >= 7:
        decision = "repost"

    elif relevance >= 6:
        decision = "comment"
        if language == "de":
            comment = (
                "Sehr spannender Beitrag – besonders im Hinblick auf die "
                "aktuellen Entwicklungen in Technologie und Marktumfeld."
            )
        else:
            comment = (
                "Interesting post, especially considering current trends "
                "in technology and market dynamics."
            )

    elif relevance >= 4:
        decision = "like"

    return decision, comment
