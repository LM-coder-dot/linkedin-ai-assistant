import streamlit as st
from storage.db import get_posts
import pyperclip

st.set_page_config(page_title="LinkedIn AI Assistant", layout="wide")
st.title("📊 LinkedIn AI Assistant – Dashboard")

DECISION_COLORS = {
    "auto_comment": "🟢",
    "review": "🟡",
    "ignore": "🔴",
}

# --- Sidebar Filter ---
st.sidebar.header("Filter")
decision_filter = st.sidebar.selectbox(
    "Entscheidung",
    ["all", "ignore", "like", "comment", "repost"],
    key="sidebar_decision_filter"
)
min_relevance = st.sidebar.slider(
    "Min. Relevanz",
    0, 10, 3,
    key="sidebar_min_relevance"
)
highlight_threshold = st.sidebar.slider(
    "Highlight-Schwelle für Repost",
    0, 10, 7,
    key="sidebar_highlight_threshold"
)

# --- Posts abrufen ---
posts = get_posts(decision=decision_filter, min_relevance=min_relevance)
st.write(f"### Gefundene Posts: {len(posts)}")

if not posts:
    st.info("Keine Posts gefunden. Bitte Pipeline ausführen.")

# --- Posts anzeigen ---
for idx, row in enumerate(posts):
    text = row.get("text", "")
    language = row.get("language", "N/A")
    relevance = int(row.get("relevance") or 0)
    highlight = int(row.get("highlight") or 0)
    decision = row.get("decision", "N/A")
    decision_reason = row.get("decision", "N/A")
    comment = row.get("comment")
    author = row.get("author", "Unbekannt")
    post_url = row.get("post_url")
    keywords = row["keywords"].split(",") if row["keywords"] else []

    relevance = int(relevance or 0)
    highlight = int(highlight or 0)

    relevance_label = (
        "🟢 hoch" if relevance >= 7
        else "🟡 mittel" if relevance >= 4
        else "🔴 niedrig"
    )

    with st.container():
        st.markdown("---")
        st.markdown(f"### {relevance_label} · `{decision.upper()}`")
        st.write(text)

        st.markdown(
            f"""
            **Autor:** {author or '–'}  
            **Sprache:** {language}  
            **Relevanz:** {relevance}/10  
            **Highlight:** {highlight}/10  
            """
        )

        st.progress(min(relevance / 10, 1.0))
        st.success(f"Decision: {decision}")
        st.caption(f"Reason: {decision_reason}")

        if post_url:
            st.markdown(f"[🔗 Zum LinkedIn-Post]({post_url})")

        if comment:
            st.markdown("**💬 Kommentar-Vorschlag:**")
            st.info(comment)

        if decision == "repost":
            repost_text = f"Starker Beitrag von {author}: {text[:200]}…"
            st.markdown("**🔁 Repost-Vorschlag:**")
            st.info(repost_text)

        if keywords:
            st.caption("Keywords: " + ", ".join(keywords))
        else:
            st.caption("Keywords: –")

        st.markdown(
            f"### {DECISION_COLORS.get(decision, '⚪')} {decision.upper()}"
        )

        DECISION_COLORS = {
            "ignore": "⚪",
            "like": "👍",
            "comment": "💬",
            "repost": "🔁",
        }

        col1, col2 = st.columns(2)
        col1.metric("🧠 Relevance", relevance)
        col2.metric("🔥 Highlight", highlight)

def score_label(score):
    if score >= 8:
        return "🔥 sehr hoch"
    if score >= 5:
        return "👍 mittel"
    return "😐 niedrig"

def test_decision_repost():
    decision, _ = decide_post({
        "relevance": 8,
        "highlight": 8,
        "keywords": ["AI", "Strategy"],
        "language": "en",
    })
    assert decision == "repost"
