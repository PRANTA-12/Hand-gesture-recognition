from collections import deque


class GestureStabilizer:
    def __init__(self, history_size=5):
        self.history = deque(maxlen=history_size)

    def update(self, gesture):
        self.history.append(gesture)

        if len(self.history) < self.history.maxlen:
            return gesture

        counts = {}

        for g in self.history:
            counts[g] = counts.get(g, 0) + 1

        stable = max(counts, key=counts.get)

        return stable

    def reset(self):
        self.history.clear()