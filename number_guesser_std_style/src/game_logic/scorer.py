class Scorer:
    def __init__(self, initial_score=100):
        self.score = initial_score

    def update_score(self, penalty=0):
        self.score -= penalty

    def get_score(self):
        """Return the current score."""
        return self.score
