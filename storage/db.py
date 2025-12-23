from supabase import create_client
import os

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")

if not SUPABASE_URL or not SUPABASE_ANON_KEY:
    raise RuntimeError("Supabase credentials not set")

supabase = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)


def get_posts(decision=None, min_relevance=0, hide_duplicates=True):
    query = (
        supabase
        .table("posts")
        .select(
            "text, language, relevance, highlight, decision, decision_reason, comment, author, post_url, keywords"
        )
        .gte("relevance", min_relevance)
        .order("highlight", desc=True)
    )
    if hide_duplicates:
        query = query.eq("is_duplicate", False)

    if decision and decision != "all":
        query = query.eq("decision", decision)

    query = query.gte("relevance", min_relevance)
    query = query.order("created_at", desc=True)

    response = query.execute()
    return response.data or []

def save_post(
    text: str,
    relevance: int,
    highlight: int | None = None,
    keywords: list[str] | None = None,
    decision: str | None = None,
    decision_reason: str | None = None,
    comment: str | None = None,
    language: str | None = None,
    post_hash: str | None = None,
    is_duplicate: bool = False,
    author: str | None = None,
    post_url: str | None = None,
):
    data = {
        "text": str(text),
        "language": str(language),
        "relevance": int(relevance),
        "highlight": int(highlight),
        "keywords": keywords if isinstance(keywords, list) else [],
        "decision": str(decision),
        "decision_reason": str(decision_reason),
        "comment": str(comment) if comment else None,
        "is_duplicate": bool(is_duplicate),
        "author": str(author) if author else None,
        "post_url": str(post_url) if post_url else None,
        "post_hash": str(post_hash),
    }

    try:
        for k, v in data.items():
            if callable(v):
                raise TypeError(f"{k} is a function, not a value")
        result = supabase.table("posts").insert(data).execute()
        return result

    except Exception as e:
        msg = str(e).lower()
        if "duplicate" in msg or "unique constraint" in msg:
            import logging
            logging.info("Duplicate post skipped")
            return None
        raise

def post_exists(post_hash: str) -> bool:
    result = (
        supabase
        .table("posts")
        .select("id")
        .eq("post_hash", post_hash)
        .limit(1)
        .execute()
    )
    return bool(result.data)
