class InteractionRecommender:
    def __init__(self):
        # Schwellenwerte – später leicht anpassbar
        self.like_threshold = 40
        self.comment_threshold = 60
        self.repost_threshold = 80

    def decide(self, analyzed_post):
        """
        Entscheidet, wie mit einem Beitrag interagiert werden soll
        Rückgabe: 'ignore' | 'like' | 'comment' | 'repost'
        """
        relevance = analyzed_post["analysis"]["relevance_score"]
        highlight = analyzed_post["analysis"]["highlight_score"]

        if highlight >= self.repost_threshold:
            return "repost"
        elif relevance >= self.comment_threshold:
            return "comment"
        elif relevance >= self.like_threshold:
            return "like"
        else:
            return "ignore"
