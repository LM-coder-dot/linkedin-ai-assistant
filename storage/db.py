from supabase import create_client
import os

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")

if not SUPABASE_URL or not SUPABASE_ANON_KEY:
    raise RuntimeError("Supabase credentials not set")

supabase = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)


def get_posts(decision=None, min_relevance=0):
    query = (
        supabase
        .table("posts")
        .select(
            "text, language, relevance, highlight, decision, decision_reason, comment, author, post_url, keywords"
        )
        .gte("relevance", min_relevance)
        .order("highlight", desc=True)
    )

    if decision and decision != "all":
        query = query.eq("decision", decision)

    response = query.execute()
    return response.data or []


def save_post(
    *,
    text: str,
    language: str,
    relevance: int,
    highlight: int,
    decision: str,
    author: str,
    post_url: str,
    decision_reason: str | None = None,
    comment: str | None = None,
    keywords: list[str] | None = None,
):
    data = {
        "text": text,
        "language": language,
        "relevance": relevance,
        "highlight": highlight,
        "decision": decision,
        "decision_reason": decision_reason,
        "comment": comment,
        "author": author,
        "post_url": post_url,
        "keywords": keywords,  # <-- LIST, kein Join
    }

    result = supabase.table("posts").insert(data).execute()
    return result
