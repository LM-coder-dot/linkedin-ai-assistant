import random

class CommentGenerator:
    def generate(self, post_text, language):
        if language.startswith("de"):
            comments = [
                "Spannender Punkt – gerade im Kontext von Digitalisierung im Banking.",
                "Sehr relevant, besonders mit Blick auf aktuelle Entwicklungen im Finanzsektor.",
                "Guter Beitrag, AI wird hier definitiv ein Gamechanger."
            ]
        else:
            comments = [
                "Very interesting perspective on finance and technology.",
                "This is highly relevant for the future of banking.",
                "Great insight – AI will clearly play a major role here."
            ]

        return random.choice(comments)
