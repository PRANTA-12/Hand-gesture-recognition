import time


class PerformanceMonitor:

    def __init__(self):

        self.last_time = time.time()

        self.frames = 0
        self.fps = 0

        self.timers = {}

    # -------------------------
    # FPS
    # -------------------------

    def update(self):

        self.frames += 1

        now = time.time()

        if now - self.last_time >= 1:

            self.fps = self.frames

            self.frames = 0

            self.last_time = now

    def get_fps(self):

        return self.fps

    # -------------------------
    # Timers
    # -------------------------

    def start(self, name):

        self.timers[name] = time.perf_counter()

    def stop(self, name):

        if name not in self.timers:
            return 0

        start = self.timers.pop(name, None)

        if start is None:
            return 0

        return (time.perf_counter() - start) * 1000