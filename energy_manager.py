class EnergyManager:

    def __init__(self):
        self.max_energy = 100
        self.energy = 100
        self.regen_rate = 0.2

    def use(self, amount):
        if self.energy >= amount:
            self.energy -= amount
            return True
        return False

    def regenerate(self):
        if self.energy < self.max_energy:
            self.energy += self.regen_rate
            if self.energy > self.max_energy:
                self.energy = self.max_energy

    def get(self):
        return int(self.energy)