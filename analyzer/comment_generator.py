def generate_comment(text: str, decision: str, keywords: list[str]) -> str | None:
    """
    Erzeugt einen kurzen, professionellen LinkedIn-Kommentar
    abhängig von der Decision.
    """

    if decision == "ignore":
        return None

    base_openers = {
        "comment": "Spannender Punkt!",
        "repost": "Sehr relevanter Beitrag.",
        "review": "Interessanter Gedanke.",
        "like": "Danke fürs Teilen.",
    }

    opener = base_openers.get(decision, "Interessanter Beitrag.")

    keyword_part = ""
    if keywords:
        keyword_part = f" Besonders spannend finde ich den Aspekt zu {keywords[0]}."

    closing = " Wie siehst du das?"

    return f"{opener}{keyword_part}{closing}"
