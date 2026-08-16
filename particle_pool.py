class Particle:

    def __init__(self):
        self.active = False
        self.x = 0
        self.y = 0
        self.dx = 0
        self.dy = 0
        self.life = 0
        self.color = (255, 255, 255)


class ParticlePool:

    def __init__(self, size=500):

        self.pool = [Particle() for _ in range(size)]

    def get(self):

        for particle in self.pool:

            if not particle.active:

                particle.active = True
                return particle

        return None

    def release(self, particle):

        particle.active = False