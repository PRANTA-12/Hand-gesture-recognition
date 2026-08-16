class GestureTransition:

    def __init__(self):
        self.previous = "UNKNOWN"

    def update(self, current):

        changed = current != self.previous

        old = self.previous
        self.previous = current

        return changed, old, current

    def reset(self):
        self.previous = "UNKNOWN"