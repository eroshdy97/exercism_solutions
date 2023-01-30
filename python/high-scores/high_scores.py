class HighScores:
    def __init__(self, scores:list[int]):
        self.scores = scores

    def latest(self):
        return self.scores[-1]

    def personal_best(self):
        return max(self.scores)

    def personal_top_three(self):
        res = []
        scr = self.scores.copy()
        for _ in range(3):
            if len(scr) <= 0:
                break
            res.append(max(scr))
            scr.remove(max(scr))
        return res