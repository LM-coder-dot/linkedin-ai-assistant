import sqlite3
import os

DB_PATH = "storage/posts.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS posts (
    text TEXT,
    language TEXT,
    relevance INTEGER,
    highlight INTEGER,
    decision TEXT,
    comment TEXT,
    author TEXT,
    post_url TEXT
)
""")


    conn.commit()
    conn.close()


def save_post(text, language, relevance, highlight, decision, comment, author, post_url):
    conn = sqlite3.connect("storage/posts.db")
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO posts (
        text, language, relevance, highlight, decision, comment, author, post_url
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        text, language, relevance, highlight, decision, comment, author, post_url
    ))

    conn.commit()
    conn.close()


def get_posts(decision="all", min_relevance=0):
    try:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
    except sqlite3.Error:

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
        WHERE relevance >= ?
    """
    params = [min_relevance]

    if decision and decision != "all":
        query += " AND decision = ?"
        params.append(decision)

    cur.execute(query, params)
    rows = cur.fetchall()
    conn.close()

    return []  # <- WICHTIG für Streamlit Cloud
