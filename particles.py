from particle_pool import ParticlePool
import cv2
import random


class ParticleEngine:

    def __init__(self):
        self.particle_pool = ParticlePool(300)
        self.particles = []

    def emit(self, position, count=10):

        x, y = position

        for _ in range(count):

            particle = self.particle_pool.get()

            if particle is None:
                continue

            particle.x = x
            particle.y = y

            particle.vx = random.uniform(-3, 3)
            particle.vy = random.uniform(-3, 3)

            particle.life = random.randint(20, 40)
            particle.size = random.randint(2, 5)
            particle.color = (0, 255, 255)

            self.particles.append(particle)

    def update(self, frame):

        alive_particles = []

        for particle in self.particles:

            particle.x += particle.vx
            particle.y += particle.vy

            particle.life -= 1

            if particle.life <= 0:
                self.particle_pool.release(particle)
                continue

            cv2.circle(
                frame,
                (int(particle.x), int(particle.y)),
                particle.size,
                particle.color,
                -1,
                lineType=cv2.LINE_AA
            )

            alive_particles.append(particle)
        self.particles = alive_particles    