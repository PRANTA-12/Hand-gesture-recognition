from powers.explosion_ember_particle import ExplosionEmberParticle
from powers.object_pool import ObjectPool

class ExplosionEmbers:

    def __init__(self):

        self.pool = ObjectPool(
        ExplosionEmberParticle,
        120
        )

    # ---------------------------------
    # Emit
    # ---------------------------------

    def emit(
        self,
        position,
        count=40
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