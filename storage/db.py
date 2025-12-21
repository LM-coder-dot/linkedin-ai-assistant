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
            "text, language, relevance, highlight, decision, comment, author, post_url, keywords"
        )
        .gte("relevance", min_relevance)
        .order("highlight", desc=True)
    )

    if decision and decision != "all":
        query = query.eq("decision", decision)

    response = query.execute()
    return response.data or []

def save_post(
    text: str,
    language: str,
    relevance: int,
    highlight: int,
    decision: str | None = None,
    comment: str | None = None,
    author: str | None = None,
    post_url: str | None = None,
    keywords: list[str] | None = None,
):
    data = {
        "text": text,
        "language": language,
        "relevance": relevance,
        "highlight": highlight,
        "decision": decision,
        "comment": comment,
        "author": author,
        "post_url": post_url,
        "keywords": ",".join(keywords or []),
    }

    supabase.table("posts").insert(data).execute()
