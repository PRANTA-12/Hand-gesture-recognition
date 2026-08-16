from collections import deque


class PredictionFilter:

    def __init__(self, size=5):
        self.history = deque(maxlen=size)

    def update(self, prediction):

        self.history.append(prediction)

        counts = {}

        for item in self.history:
            counts[item] = counts.get(item, 0) + 1

        return max(counts, key=counts.get)