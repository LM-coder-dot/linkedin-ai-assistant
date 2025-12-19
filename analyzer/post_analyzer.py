from analyzer.relevance_scorer import relevance_score
from analyzer.language_detector import detect_language
from analyzer.highlight_scorer import highlight_score


def analyze_post(text: str) -> dict:
    if not text or not text.strip():
        return {
            "relevance": 0,
            "language": "unknown",
            "highlight": 0,
            "keywords": []
        }

    language = detect_language(text)
    relevance, keywords = relevance_score(text)
    highlight = highlight_score(text)

    return {
        "relevance": relevance,
        "language": language,
        "highlight": highlight,
        "keywords": keywords
    }
