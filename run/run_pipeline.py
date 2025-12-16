from collector.linkedin_collector import LinkedInCollector
from analyzer.post_analyzer import analyze_post
from llm.comment_generator import generate_comment
from storage.db import init_db, save_post
from recommender.decision_engine import decide_action


collector = LinkedInCollector()

init_db()

posts = collector.collect_feed()

for post in posts:
    text = post["text"]
    author = post.get("author")
    post_url = post.get("post_url")

    analysis = analyze_post(text)
    decision, comment = decide_action(analysis)

    save_post(
        text=text,
        relevance=analysis.get("relevance", 0),
        highlight=analysis.get("highlight", 0),
        language=analysis.get("language", "de"),

        decision=decision,
        comment=comment,
        author=author,
        post_url=post_url
    )


print("Pipeline inkl. Kommentare abgeschlossen.")
