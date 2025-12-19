from analyzer.relevance_scorer import relevance_score
from analyzer.highlight_scorer import highlight_score
from analyzer.language_detector import detect_language

def analyze_post(text: str) -> dict:
    relevance, keywords = relevance_score(text)
    highlight = highlight_score(text)
    language = detect_language(text)

    return {
        "text": text,
        "relevance": relevance,
        "highlight": highlight,
        "keywords": keywords,
        "language": language,
    }
