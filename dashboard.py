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
    # Spalten robust auslesen
    text = row[0]
    language = row[1] if len(row) > 1 else "N/A"
    relevance = row[2] if len(row) > 2 else 0
    highlight = row[3] if len(row) > 3 else 0
    decision = row[4] if len(row) > 4 else "N/A"
    comment = row[5] if len(row) > 5 else None
    author = row[6] if len(row) > 6 else "Unbekannt"
    post_url = row[7] if len(row) > 7 else None

    # Container für jeden Post
    with st.container():
        st.markdown("---")
        st.markdown(f"**Entscheidung:** `{decision.upper()}`")
        st.markdown(f"**Sprache:** {language} | **Relevanz:** {relevance} | **Highlight:** {highlight}")
        st.markdown(f"**Verfasser:** {author}")
        st.markdown(f"**Link zum Post:** [Zum LinkedIn-Post]({post_url})")
        st.write(text)

        # Zusatzinfos
        st.markdown(f"**Verfasser:** {author}")
        if post_url:
            st.markdown(f"**Link zum Post:** [Hier klicken]({post_url})")

        # Kommentar-Vorschlag
        if comment:
            st.markdown("**Kommentar-Vorschlag:**")
            st.info(comment)
            st.button(
                "📋 Kommentar kopieren",
                key=f"copy_comment_{idx}",
                on_click=lambda c=comment: pyperclip.copy(c)
            )

        # Repost-Vorschlag (falls Highlight hoch)
        if highlight >= highlight_threshold:
            repost_text = f"Spannender Beitrag von {author}: \"{text[:200]}...\""
            st.markdown("**Repost-Vorschlag:**")
            st.info(repost_text)
            st.button(
                "📋 Repost-Text kopieren",
                key=f"copy_repost_{idx}",
                on_click=lambda t=repost_text: pyperclip.copy(t)
            )
