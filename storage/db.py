# storage/db.py
import os
import psycopg2

DATABASE_URL = os.getenv("DATABASE_URL")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise RuntimeError("SUPABASE_URL or SUPABASE_KEY not set")

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
}

def get_connection():
    if not DATABASE_URL:
        raise RuntimeError("DATABASE_URL not set")

    return psycopg2.connect(
        DATABASE_URL,
        sslmode="require"
    )


def get_posts(decision=None, min_relevance=0):
    params = {
        "select": "*",
        "relevance": f"gte.{min_relevance}",
        "order": "created_at.desc",
        "limit": 100,
    }

    if decision:
        params["decision"] = f"eq.{decision}"

    resp = requests.get(
        f"{SUPABASE_URL}/rest/v1/posts",
        headers=HEADERS,
        params=params,
        timeout=10,
    )

    resp.raise_for_status()
    return resp.json()
