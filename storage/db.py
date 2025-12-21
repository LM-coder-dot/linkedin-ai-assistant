from supabase import create_client
import os

supabase = create_client(
    os.environ["SUPABASE_URL"],
    os.environ["SUPABASE_ANON_KEY"]
)

def get_posts(decision=None, min_relevance=0):
    conn = get_connection()
    cur = conn.cursor()

    query = """
    SELECT
        text,
        language,
        relevance,
        highlight,
        decision,
        comment,
        author,
        post_url
    FROM posts
    WHERE COALESCE(relevance, 0) >= %s
    """
    params = [min_relevance]

    if decision and decision != "all":
        query += " AND decision = %s"
        params.append(decision)

    query += " ORDER BY highlight DESC NULLS LAST, relevance DESC NULLS LAST"

    cur.execute(query, params)
    rows = cur.fetchall()

    cur.close()
    conn.close()
    return rows


def save_post(
    text: str,
    relevance: int,
    highlight: int,
    language: str,
    decision: str,
    comment: str | None = None,
    author: str | None = None,
    post_url: str | None = None,
):
    """
    Speichert einen Post in der Supabase-Tabelle `posts`.
    """

    data = {
        "text": text,
        "relevance": relevance,
        "highlight": highlight,
        "language": language,
        "decision": decision,
        "comment": comment,
        "author": author,
        "post_url": post_url,
    }

    result = supabase.table("posts").insert(data).execute()

    return result
