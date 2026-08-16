import time


class FrameTimer:

    def __init__(self):
        self.previous = time.perf_counter()

    def delta(self):
        current = time.perf_counter()
        dt = current - self.previous
        self.previous = current
        return dt