from dotenv import load_dotenv
load_dotenv()
from collector.linkedin_collector import LinkedInCollector
from analyzer.post_analyzer import analyze_post
from analyzer.relevance_scorer import relevance_score
from recommender.decision_engine import decide_action
from storage.db import save_post
from llm.comment_generator import generate_comment
from analyzer.decision_engine import decide_post

decision, decision_reason = decide_post(analysis)

analysis["decision"] = decision
analysis["decision_reason"] = decision_reason

if decision == "comment":
    analysis["comment"] = generate_comment(
        text=text,
        keywords=analysis["keywords"],
        language=analysis["language"],
    )

def main():
    collector = LinkedInCollector()
    collector = LinkedInCollector()
    posts = collector.collect_feed()

    for post in posts:
        text = post["text"]
        author = post.get("author")
        post_url = post.get("post_url")

        # 🔎 Relevanz-Scoring
        relevance, keywords = relevance_score(text)

        # 🔬 Weitere Analyse (Sprache, Highlight etc.)
        analysis = analyze_post(text)
        analysis["relevance"] = relevance
        analysis["keywords"] = keywords

        # 🤖 Entscheidung
        decision, comment = decide_action(analysis)
        decision, decision_reason = decide_post(analysis)
        analysis["decision"] = decision
        analysis["decision_reason"] = decision_reason

        # Optional: Kommentar
        if decision == "comment":
            analysis["comment"] = generate_comment(
                text=text,
                keywords=analysis.get("keywords", []),
                language=analysis.get("language", "de"),
            )

        # 💾 Speichern
        save_post(
            text=text,
            language=analysis["language"],
            relevance=analysis["relevance"],
            highlight=analysis["highlight"],
            keywords=analysis["keywords"],
            decision=analysis["decision"],
            decision_reason=analysis["decision_reason"],
            comment=analysis.get("comment"),
            author=author,
            post_url=post_url,
        )

    print("✅ Pipeline inkl. Relevanz-Scoring abgeschlossen.")


if __name__ == "__main__":
    main()
