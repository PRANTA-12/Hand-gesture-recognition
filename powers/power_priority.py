class PowerPriority:

    def __init__(self):
        self.current = None

    def update(self, new_power):

        if new_power == self.current:
            return False

        self.current = new_power
        return True

    def get(self):
        return self.current

    def reset(self):
        self.current = None