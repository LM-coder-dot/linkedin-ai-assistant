import streamlit as st
from storage.db import get_posts
import pyperclip

st.set_page_config(page_title="LinkedIn AI Assistant", layout="wide")
st.title("📊 LinkedIn AI Assistant – Dashboard")

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
    (
        text,
        language,
        relevance,
        highlight,
        decision,
        comment,
        author,
        post_url,
    ) = row

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

        st.progress(relevance / 10)

        if post_url:
            st.markdown(f"[🔗 Zum LinkedIn-Post]({post_url})")

        if comment:
            st.info(comment)


def render_dashboard(posts):
    print("\n📊 LinkedIn AI Assistant – Dashboard\n")

    for i, post in enumerate(posts, 1):
        text, author, relevance, highlight, decision, comment, url = post

        print(f"{i}. {author or 'Unbekannt'}")
        print(f"   🧠 Relevance : {relevance}/10")
        print(f"   🔥 Highlight : {highlight}/10")
        print(f"   🎯 Decision  : {decision}")
        print(f"   📝 Text      : {text[:120]}...")
        print("-" * 60)

def score_label(score):
    if score >= 8:
        return "🔥 sehr hoch"
    if score >= 5:
        return "👍 mittel"
    return "😐 niedrig"

print(f"   🧠 Relevance : {relevance}/10 ({score_label(relevance)})")
print(f"   🔥 Highlight : {highlight}/10 ({score_label(highlight)})")
