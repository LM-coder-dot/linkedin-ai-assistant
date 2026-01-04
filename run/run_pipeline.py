import hashlib
from dotenv import load_dotenv
load_dotenv()
from collector.linkedin_collector import LinkedInCollector
from analyzer.post_analyzer import analyze_post
from analyzer.relevance_scorer import relevance_score
from analyzer.comment_generator import generate_comment
from recommender.decision_engine import decide_action
from storage.db import save_post, post_exists
from llm.comment_generator import generate_comment
from analyzer.decision_engine import decide_post
from utils.hashing import generate_post_hash

def main():
    collector = LinkedInCollector()
    posts = collector.collect(limit=10)

    for post in posts:
        text = post["text"]
        author = post.get("author")
        post_url = post.get("post_url")
        post_hash = generate_post_hash(text, author)
        is_duplicate = post_exists(post_hash)
        hash_value = generate_post_hash(text, author)

        # 🔎 Relevanz
        relevance, keywords = relevance_score(text)

        # 🔬 Analyse
        analysis = analyze_post(text)
        analysis["relevance"] = relevance
        analysis["keywords"] = keywords

        # 🧠 Entscheidung
        decision, decision_reason = decide_post(analysis)
       
        # --- Duplicate Override ---
        if is_duplicate:
            decision = "ignore"
            decision_reason = "Duplicate post (same content already processed)"

        comment = generate_comment(
            text=text,
            decision=decision,
            relevance=relevance,
            keywords=analysis.get("keywords", []),
        )
        analysis["decision"] = decision
        analysis["decision_reason"] = decision_reason

        # 💬 Kommentar (optional)
        if decision == "comment":
            analysis["comment"] = generate_comment(
                text=text,
                keywords=keywords,
                language=analysis.get("language", "de"),
            )

        # 💾 Persistenz
        save_post(
            text=text,
            language=analysis["language"],
            relevance=analysis["relevance"],
            highlight=analysis["highlight"],
            keywords=analysis.get("keywords", []),
            decision=analysis["decision"],
            decision_reason=analysis["decision_reason"],
            comment=comment,
            is_duplicate=is_duplicate,
            author=author,
            post_url=post_url,
            post_hash=hash_value,
        )

    print("✅ Pipeline inkl. Decision Engine abgeschlossen.")

def compute_post_hash(text: str) -> str:
    normalized = " ".join(text.lower().split())
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()

if __name__ == "__main__":
    main()
