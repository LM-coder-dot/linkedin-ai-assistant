# storage/db.py
import os
import psycopg2
from urllib.parse import urlparse

DATABASE_URL = os.getenv("DATABASE_URL")

def get_connection():
    if not DATABASE_URL:
        raise RuntimeError("DATABASE_URL not set")

    result = urlparse(DATABASE_URL)

    return psycopg2.connect(
        dbname=result.path.lstrip("/"),
        user=result.username,
        password=result.password,
        host=result.hostname,
        port=result.port,
        sslmode="require",
    )

def get_posts(decision=None, min_relevance=0):
    conn = get_connection()
    cur = conn.cursor()

    query = """
        SELECT text, language, relevance, highlight, decision, comment, author, post_url
        FROM posts
        WHERE relevance >= %s
    """
    params = [min_relevance]

    if decision:
        query += " AND decision = %s"
        params.append(decision)

    cur.execute(query, params)
    rows = cur.fetchall()

    cur.close()
    conn.close()
    return rows

