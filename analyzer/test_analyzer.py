from analyzer.post_analyzer import analyze_post

def test_analyze_post_basic():
    text = "AI is transforming banking. What do you think?"
    result = analyze_post(text)

    assert "relevance" in result
    assert "highlight" in result
    assert isinstance(result["relevance"], int)
    assert isinstance(result["highlight"], int)
