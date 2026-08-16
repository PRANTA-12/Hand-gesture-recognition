import time


class Animation:

    def __init__(self, duration=0.8):
        self.active = False
        self.start_time = 0
        self.duration = duration
        self.position = (0, 0)

        # Animation state
        self.state = "IDLE"

    def start(self, position):
        self.active = True
        self.start_time = time.time()
        self.position = position

        self.state = "START"

    def update(self):

        if not self.active:
            return False

        current_time = time.time()
        elapsed = current_time - self.start_time

        # Animation states
        # Animation states
        duration = self.duration

        if elapsed < 0.15:
            self.state = "CHARGE"

        elif elapsed < duration * 0.7:
            self.state = "TRAVEL"

        else:
            self.state = "FADE"

        if elapsed >= duration:
            self.active = False
            self.state =  "IDLE"
            return False

        return True

    def progress(self):

        if not self.active:
            return 0

        current_time = time.time()

        return (current_time - self.start_time) / self.duration

    def stop(self):
        if not self.active:
            return
        self.active = False
        self.state = "IDLE"    


        