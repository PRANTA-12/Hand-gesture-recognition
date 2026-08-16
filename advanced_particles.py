from particle_pool import ParticlePool
import cv2
import random

class AdvancedParticles:

    def __init__(self):
        self.particle_pool = ParticlePool(500)
        self.particles = []

    def emit(self, position, color=(0, 255, 255), count=10, speed=3):

        x, y = position

        for _ in range(count):

            particle = self.particle_pool.get()

            if particle is None:
                continue

            particle.x = x
            particle.y = y

            particle.vx = random.uniform(-speed, speed)
            particle.vy = random.uniform(-speed, speed)

            particle.life = random.randint(20, 40)
            particle.size = random.randint(2, 5)
            particle.color = color

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