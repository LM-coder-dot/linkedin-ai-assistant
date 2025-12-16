import random

def analyze_post(post_text: str):
    """
    Dummy-Analyse für Testing:
    - Sprache: "de" oder "en"
    - Relevanzscore 0–10
    - Highlightscore 0–10
    """
    
    # Sprache erkennen
    if any(word in post_text.lower() for word in ["the", "and", "is", "ai", "bank"]):
        language = "en"
    else:
        language = "de"
    
    # zufällige Scores
    relevance_score = random.randint(0, 10)
    highlight_score = random.randint(0, 10)
    
    return {
        "language": language,
        "relevance_score": relevance_score,
        "highlight_score": highlight_score
    }
