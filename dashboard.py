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
hide_duplicates = st.sidebar.checkbox(
    "Duplikate ausblenden",
    value=True
)
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
posts = get_posts(
    decision=decision_filter,
    min_relevance=min_relevance,
    hide_duplicates=hide_duplicates,
)
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
    decision_reason = row.get("decision_reason", "–")
    comment = row.get("comment")
    author = row.get("author", "Unbekannt")
    post_url = row.get("post_url")
    raw_keywords = row.get("keywords")
    keywords = [k.strip() for k in raw_keywords.split(",")] if raw_keywords else []
    is_duplicate = row.get("is_duplicate")
    relevance = int(relevance or 0)
    highlight = int(highlight or 0)

    relevance_label = (
        "🟢 hoch" if relevance >= 7
        else "🟡 mittel" if relevance >= 4
        else "🔴 niedrig"
    )

    with st.container():
        st.markdown("---")
        icon = DECISION_COLORS.get(decision, "⚪")
        st.markdown(f"### {icon} {decision.upper()} · {relevance_label}")
        st.write(text)

        st.markdown(
            f"""
            **Autor:** {author or '–'}  
            **Sprache:** {language}  
            **Relevanz:** {relevance}/10  
            **Highlight:** {highlight}/10  
            """
        )

        badge = "♻️ Duplicate" if is_duplicate else "🆕 Neu"
        st.caption(badge)

        st.progress(min(relevance / 10, 1.0))
        st.success(f"Decision: {decision}")
        st.caption(f"Reason: {decision_reason}")

        if post_url:
            st.markdown(f"[🔗 Zum LinkedIn-Post]({post_url})")

        if comment:
            st.markdown("**💬 Kommentar-Vorschlag:**")
            st.text_area(
                "Kommentar bearbeiten",
                value=comment,
                key=f"comment_edit_{idx}",
                height=120,
            )

            st.button(
                "📋 Kommentar kopieren",
                key=f"copy_comment_{idx}",
                on_click=lambda c=comment: pyperclip.copy(c),
            )


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

        col1, col2 = st.columns(2)
        col1.metric("🧠 Relevance", relevance)
        col2.metric("🔥 Highlight", highlight)

def score_label(score):
    if score >= 8:
        return "🔥 sehr hoch"
    if score >= 5:
        return "👍 mittel"
    return "😐 niedrig"
