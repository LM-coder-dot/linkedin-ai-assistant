# storage/db.py
import os
import psycopg2

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL not set")

def get_connection():
    return psycopg2.connect(
        DATABASE_URL,
        sslmode="require"
    )

def get_posts(decision="all", min_relevance=0):
    conn = get_connection()
    cur = conn.cursor()

    query = """
        SELECT text, language, relevance, highlight, decision, comment, author, post_url
        FROM posts
        WHERE relevance >= %s
    """
    params = [min_relevance]

    if decision != "all":
        query += " AND decision = %s"
        params.append(decision)

    query += " ORDER BY relevance DESC LIMIT 100"

    cur.execute(query, params)
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows
