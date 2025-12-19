def detect_language(text: str) -> str:
    """
    Sehr einfache Heuristik:
    - erkennt Deutsch vs. Englisch
    - 100 % offline / kostenlos
    """

    text_lower = text.lower()

    german_markers = [
        " und ", " oder ", "nicht", "ist", "sind", "mit",
        "für", "das", "die", "ein", "eine", "wird"
    ]

    english_markers = [
        " the ", " and ", " or ", "is ", "are ", "with ",
        "for ", "this ", "that ", "will "
    ]

    de_hits = sum(1 for w in german_markers if w in text_lower)
    en_hits = sum(1 for w in english_markers if w in text_lower)

    return "de" if de_hits >= en_hits else "en"
