import sqlite3

DB_PATH = "storage/posts.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT UNIQUE,
        language TEXT,
        relevance INTEGER,
        highlight INTEGER,
        decision TEXT,
        comment TEXT
    )
    """)


    conn.commit()
    conn.close()


def save_post(text, analysis, decision, comment=None, author=None, post_url=None):
    cur.execute("""
        INSERT INTO posts (text, language, relevance, highlight, decision, comment, author, post_url)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        text,
        analysis["language"],
        analysis["relevance_score"],
        analysis["highlight_score"],
        decision,
        comment,
        author,
        post_url
    ))
    conn.commit()
    conn.close()



def get_posts(decision=None, min_relevance=0):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    query = """
        SELECT text, language, relevance, highlight, decision
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

    return rows
