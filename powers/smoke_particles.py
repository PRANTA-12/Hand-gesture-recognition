import random

from powers.smoke_particle import SmokeParticle
from powers.object_pool import ObjectPool

class SmokeParticles:

    def __init__(self):

        self.pool = ObjectPool(
        SmokeParticle,
        80
        )

    # ---------------------------------
    # Emit
    # ---------------------------------

    def emit(self, position):

        count = 2 if random.random() > 0.5 else 1

        for _ in range(count):

            particle = self.pool.get()

            if particle:
                particle.start(position)
    # ---------------------------------
    # Update
    # ---------------------------------

    def update(self, dt):

        for particle in self.pool.active_objects():
            particle.update(dt)

    # ---------------------------------
    # Draw
    # ---------------------------------

    def draw(self, frame):

        particles = self.pool.active_objects()

        if not particles:
            return

        for particle in particles:
            particle.draw(frame)

    # ---------------------------------
    # Clear
    # ---------------------------------

    def clear(self):

        self.pool.clear()

    # ---------------------------------
    # Count
    # ---------------------------------

    def count(self):

        return self.pool.active_count()

    # ---------------------------------
    # Reset
    # ---------------------------------

    def reset(self):

        self.pool.reset()