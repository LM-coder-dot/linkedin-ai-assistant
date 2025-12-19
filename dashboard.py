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
    # tuple → sicher auslesen
    text = row[0]
    language = row[1] if len(row) > 1 else "N/A"
    relevance = int(row[2]) if len(row) > 2 and row[2] is not None else 0
    highlight = int(row[3]) if len(row) > 3 and row[3] is not None else 0
    decision = row[4] if len(row) > 4 else "N/A"
    comment = row[5] if len(row) > 5 else None
    author = row[6] if len(row) > 6 else "Unbekannt"
    post_url = row[7] if len(row) > 7 else None


    relevance = int(row[2]) if len(row) > 2 and row[2] is not None else 0
    highlight = int(row[3]) if len(row) > 3 and row[3] is not None else 0

    relevance_label = (
    "🟢 hoch" if relevance >= 7 else
    "🟡 mittel" if relevance >= 4 else
    "🔴 niedrig"
)

    highlight_label = (
        "🔥 hoch" if highlight >= highlight_threshold else
        "😐 normal"
    )

    with st.container():
        st.markdown("---")

        st.markdown(f"**Autor:** {author}")
        st.markdown(f"**Entscheidung:** `{decision.upper()}`")
        st.markdown(f"**Sprache:** {language}")
        st.metric("🧠 Relevance", f"{relevance}/10", relevance_label)
        st.progress(relevance / 10)
        st.metric("🔥 Highlight", f"{highlight}/10")

        if post_url:
            st.markdown(f"[🔗 Zum LinkedIn-Post]({post_url})")

        st.markdown("**Post-Inhalt:**")
        st.write(text)

        if comment:
            st.markdown("**💬 Kommentar-Vorschlag:**")
            st.info(comment)
            st.button(
                "📋 Kommentar kopieren",
                key=f"copy_comment_{idx}",
                on_click=lambda c=comment: pyperclip.copy(c)
            )

        if highlight >= highlight_threshold:
            repost_text = f"Spannender Beitrag von {author}: {text[:200]}..."
            st.markdown("**🔁 Repost-Vorschlag:**")
            st.info(repost_text)
            st.button(
                "📋 Repost-Text kopieren",
                key=f"copy_repost_{idx}",
                on_click=lambda t=repost_text: pyperclip.copy(t)
            )

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
