class LandmarkFilter:
    def __init__(self, alpha=0.7):
        self.alpha = alpha
        self.previous = None

    def smooth(self, landmarks):
        if len(landmarks) == 0:
            self.previous = None
            return landmarks

        # First frame
        if self.previous is None:
            self.previous = [point[:] for point in landmarks]
            return landmarks

        filtered = []

        for current, prev in zip(landmarks, self.previous):

            idx = current[0]

            x = int(self.alpha * prev[1] + (1 - self.alpha) * current[1])
            y = int(self.alpha * prev[2] + (1 - self.alpha) * current[2])

            z = self.alpha * prev[3] + (1 - self.alpha) * current[3]

            filtered.append([idx, x, y, z])

        self.previous = [point[:] for point in filtered]

        return filtered
    def reset(self):
        self.previous = None