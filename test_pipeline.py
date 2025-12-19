import os
import pytest

if not os.getenv("LINKEDIN_COOKIE"):
    pytest.skip("LINKEDIN_COOKIE not set", allow_module_level=True)

from collector.linkedin_collector import LinkedInCollector
from analyzer.post_analyzer import PostAnalyzer
from recommender.interaction_recommender import InteractionRecommender
from recommender.comment_generator import CommentGenerator

collector = LinkedInCollector()
analyzer = PostAnalyzer()
recommender = InteractionRecommender()
comment_generator = CommentGenerator()

feed = collector.fetch_feed()

for post in feed:
    analysis = analyzer.analyze_post(post)
    decision = recommender.decide({
        "post": post,
        "analysis": analysis
    })

    print("\nPOST:", post)
    print("ANALYSE:", analysis)
    print("ENTSCHEIDUNG:", decision)

    if decision == "comment":
        comment = comment_generator.generate(post, analysis["language"])
        print("KOMMENTAR:", comment)
