from analyzer.relevance_scorer import relevance_score

def test_relevance_basic():
    score, hits = relevance_score("AI is transforming banking")

    assert isinstance(score, int)
    assert score > 0
    assert "ai" in hits
