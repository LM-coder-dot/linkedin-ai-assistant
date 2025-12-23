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
    post_hash: str,
    highlight: int | None = None,
    keywords: list[str] | None = None,
    decision: str | None = None,
    decision_reason: str | None = None,
    comment: str | None = None,
    language: str | None = None,
    is_duplicate: bool = False,
    author: str | None = None,
    post_url: str | None = None,
    author_avatar: str | None = None,
):
    data = {
        "text": text,
        "relevance": relevance,
        "post_hash": post_hash,
        "highlight":highlight,
        "keywords": ",".join(keywords) if keywords else None,
        "decision": decision,
        "decision_reason": decision_reason,
        "comment":comment,
        "is_duplicate": is_duplicate,
        "author": author,
        "post_url": post_url,
        "author_avatar": author_avatar,
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
