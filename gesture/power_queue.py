import time

class PowerQueue:

    def __init__(self, delay=0.25):
        self.current = None
        self.pending = None
        self.start_time = 0
        self.delay = delay

    def update(self, action):

        # Ignore invalid actions
        if action is None:
            return self.current

        if action == "UNKNOWN":
            return self.current

        if action == "NONE":
            return self.current

        if action == self.current:
            return self.current

        if action != self.pending:
            self.pending = action
            self.start_time = time.time()
            return self.current

        if time.time() - self.start_time >= self.delay:
            self.current = self.pending

        return self.current

    def reset(self):
        self.current = None
        self.pending = None