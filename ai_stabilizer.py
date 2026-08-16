from collections import deque
from collections import Counter


class AIStabilizer:

    def __init__(self, history=5):

        self.history = deque(maxlen=history)

    def update(self, prediction, confidence):

        # Reject only very weak predictions
        if confidence < 0.60:
            return "UNKNOWN"

        self.history.append(prediction)

        # Don't wait for a full buffer
        if len(self.history) < 3:
            return prediction

        counts = Counter(self.history)

        stable, count = counts.most_common(1)[0]

        # Majority vote
        if count >= 2:
            return stable

        return prediction

    def reset(self):
        self.history.clear()