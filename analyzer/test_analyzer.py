from post_analyzer import PostAnalyzer

analyzer = PostAnalyzer()

test_post = "FinTech und AI verändern die Banking-Welt massiv."
result = analyzer.analyze_post(test_post)

print("Analyseergebnis:", result)
