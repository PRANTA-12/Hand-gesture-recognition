import time


class PerformanceProfiler:

    def __init__(self, print_every=30):
        self.last = time.perf_counter()
        self.print_every = print_every
        self.frame_count = 0

    def start(self):
        self.last = time.perf_counter()
        self.frame_count += 1

    def check(self, name):
        now = time.perf_counter()
        elapsed = (now - self.last) * 1000

        if self.frame_count % self.print_every == 0:
            print(f"{name}: {elapsed:.2f} ms")

        self.last = now