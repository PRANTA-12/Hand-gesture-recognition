from powers.explosion_fire_ring import ExplosionFireRing
from powers.object_pool import ObjectPool

class ExplosionFireRings:

    def __init__(self):

        self.pool = ObjectPool(
            ExplosionFireRing,
            20
        )

    # ---------------------------------
    # Emit
    # ---------------------------------

    def emit(
        self,
        position,
        count=1
    ):

        for _ in range(count):

            ring = self.pool.get()

            if ring:
                ring.start(position)

    # ---------------------------------
    # Update
    # ---------------------------------

    def update(self, dt):

        for ring in self.pool.active_objects():
            ring.update(dt)
    # ---------------------------------
    # Draw
    # ---------------------------------

    def draw(self, frame):

        rings = self.pool.active_objects()

        if not rings:
            return

        for ring in rings:
            ring.draw(frame)

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