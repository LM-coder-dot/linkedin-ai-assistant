from dotenv import load_dotenv
load_dotenv()
from collector.linkedin_collector import LinkedInCollector
from analyzer.post_analyzer import analyze_post
from analyzer.relevance_scorer import relevance_score
from recommender.decision_engine import decide_action
from storage.db import init_db, save_post

def main():
    collector = LinkedInCollector()
    init_db()
    collector = LinkedInCollector()
    posts = collector.collect_feed()

    for post in posts:
        text = post.get("text", "")
        author = post.get("author")
        post_url = post.get("post_url")

        # 🔎 Relevanz-Scoring
        relevance, relevance_signals = relevance_score(text)

        # 🔬 Weitere Analyse (Sprache, Highlight etc.)
        analysis = analyze_post(text)
        analysis["relevance"] = relevance
        analysis["relevance_signals"] = relevance_signals

        # 🤖 Entscheidung
        decision, comment = decide_action(analysis)

        # 💾 Speichern
        save_post(
            text=text,
            relevance=relevance,
            highlight=analysis.get("highlight", 0),
            language=analysis.get("language", "de"),
            decision=decision,
            comment=comment,
            author=author,
            post_url=post_url
        )

    print("✅ Pipeline inkl. Relevanz-Scoring abgeschlossen.")


if __name__ == "__main__":
    main()
