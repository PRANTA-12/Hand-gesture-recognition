from powers.explosion_particle import ExplosionParticle
from powers.object_pool import ObjectPool

class ExplosionParticles:

    def __init__(self):

        self.pool = ObjectPool(
        ExplosionParticle,
        200
        )

    # ---------------------------------
    # Emit
    # ---------------------------------

    def emit(
        self,
        position,
        count=60
    ):

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
    # Alive Count
    # ---------------------------------

    def alive_count(self):

        return self.pool.active_count()

    # ---------------------------------
    # Is Empty
    # ---------------------------------

    def is_empty(self):

        return self.pool.active_count() == 0

    def count(self):

        return self.pool.active_count()

    def reset(self):

        self.pool.reset()