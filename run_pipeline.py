from collector.linkedin_collector import LinkedInCollector
from analyzer.post_analyzer import analyze_post
from llm.comment_generator import generate_comment
from storage.db import init_db, save_post

collector = LinkedInCollector()

init_db()

posts = collector.fetch_feed()

for post in posts:
    analysis = analyze_post(post)

    if analysis["relevance_score"] >= 4:
        decision = "comment"
        comment = generate_comment(post, analysis["language"])
    else:
        decision = "ignore"
        comment = None

    save_post(post, analysis, decision, comment)

print("Pipeline inkl. Kommentare abgeschlossen.")
