from powers.flame_particle import FlameParticle
from powers.object_pool import ObjectPool
import random


class FlameParticles:

    def __init__(self):

        self.pool = ObjectPool(
        FlameParticle,
        100
        )

    # ---------------------------------
    # Emit
    # ---------------------------------

    def emit(self, position):

        count = 3 if random.random() > 0.5 else 2

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

    def count(self):

        return self.pool.active_count()


    def reset(self):

        self.pool.reset()   