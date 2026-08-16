from collections import deque
from two_hand_gesture import TwoHandPower


class TwoHandStabilizer:
    def __init__(self, history_size=5, stable_count=4):
        """
        history_size : Number of recent frames to keep
        stable_count : Minimum occurrences required to accept a power
        """
        self.history = deque(maxlen=history_size)
        self.stable_count = stable_count
        self.current_power = TwoHandPower.NONE

    def update(self, power):
        """
        Stabilize the detected two-hand power.
        """

        self.history.append(power)

        # Not enough history yet
        if len(self.history) < self.history.maxlen:
            return self.current_power

        counts = {}

        for p in self.history:
            counts[p] = counts.get(p, 0) + 1

        stable_power = max(counts, key=counts.get)

        # Accept only if seen enough times
        if counts[stable_power] >= self.stable_count:
            self.current_power = stable_power

        return self.current_power

    def reset(self):
        """
        Reset the stabilizer.
        """
        self.history.clear()
        self.current_power = TwoHandPower.NONE