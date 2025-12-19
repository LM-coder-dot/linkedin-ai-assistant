def generate_repost_text(
    post_text: str,
    author: str | None = None,
    language: str = "en"
) -> str:

    author_part = f"by {author}" if author else "this post"

    if language == "de":
        return (
            f"Der Beitrag {author_part} greift ein spannendes Thema auf.\n\n"
            f"Kernpunkt:\n"
            f"„{post_text.strip()}“\n\n"
            f"Gerade im aktuellen Umfeld ist das hochrelevant. "
            f"Mich interessiert besonders, wie sich diese Entwicklung weiter entfaltet.\n\n"
            f"Was denkt ihr dazu?"
        )

    return (
        f"This post {author_part} highlights an important topic.\n\n"
        f"Key takeaway:\n"
        f"“{post_text.strip()}”\n\n"
        f"This is especially relevant right now. "
        f"I’m curious how others see this evolving.\n\n"
        f"What’s your take?"
    )
