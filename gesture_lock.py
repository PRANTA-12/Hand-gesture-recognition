import time


class GestureLock:

    def __init__(self):

        self.current = "UNKNOWN"
        self.last_prediction = "UNKNOWN"

        self.start_time = time.time()

        self.lock_time = 0.8

    def update(self, prediction):

        now = time.time()

        # Never lock UNKNOWN
        if prediction == "UNKNOWN":
            return self.current

        # New gesture detected
        if prediction != self.last_prediction:

            self.last_prediction = prediction
            self.start_time = now

            return self.current

        # Lock after stable time
        if now - self.start_time >= self.lock_time:

            self.current = prediction

        return self.current

    def reset(self):

        self.current = "UNKNOWN"
        self.last_prediction = "UNKNOWN"
        self.start_time = time.time()