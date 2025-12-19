import os
import psycopg2

DATABASE_URL = os.getenv("DATABASE_URL")

def get_connection():
    return psycopg2.connect(DATABASE_URL)

DB_PATH = "storage/posts.db"

def init_db():
    def get_connection():
        return psycopg2.connect(
            os.getenv("DATABASE_URL"),
            sslmode="require"
        )
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
        WHERE relevance >= ?
    """
    params = [min_relevance]

    if decision != "all":
        query += " AND decision = ?"
        params.append(decision)

    query += " ORDER BY relevance DESC"

    cur.execute(query, params)
    rows = cur.fetchall()

    conn.close()
    return rows

