from physics.physics_body import PhysicsBody
from physics.vector2 import Vector2


class ExplosionPhysics(PhysicsBody):

    def __init__(self):
        super().__init__()

        # -------------------------
        # Explosion Settings
        # -------------------------

        self.radius = 0.0
        self.max_radius = 120.0

        self.expansion_speed = 900.0

        self.fade_speed = 2.5

        self.intensity = 1.0

        self.duration = 0.45
        self.elapsed = 0.0

        self.finished = False

    # ---------------------------------
    # Start
    # ---------------------------------

    def start(self, position):

        super().start()

        self.position = Vector2(
            position[0],
            position[1]
        )

        self.velocity = Vector2.zero()
        self.acceleration = Vector2.zero()

        self.radius = 0.0

        self.intensity = 1.0

        self.elapsed = 0.0

        self.finished = False

    # ---------------------------------
    # Update
    # ---------------------------------

    def update(self, dt):

        if not self.active:
            return

        radius = self.radius
        intensity = self.intensity
        elapsed = self.elapsed

        elapsed += dt

        radius += self.expansion_speed * dt

        radius = min(radius, self.max_radius)

        intensity -= self.fade_speed * dt

        intensity = max(intensity, 0)

        self.elapsed = elapsed
        self.radius = radius
        self.intensity = intensity

        if elapsed >= self.duration:

            self.finished = True

            self.destroy()

    # ---------------------------------
    # Progress
    # ---------------------------------

    def progress(self):

        if self.duration == 0:
            return 1.0

        return min(
            self.elapsed / self.duration,
            1.0
        )

    # ---------------------------------
    # Is Finished
    # ---------------------------------

    def is_finished(self):

        return self.finished

    # ---------------------------------
    # Reset
    # ---------------------------------

    def reset(self):

        super().reset()

        self.radius = 0.0

        self.elapsed = 0.0

        self.intensity = 1.0

        self.finished = False

    # ---------------------------------
    # Destroy
    # ---------------------------------

    def destroy(self):

        self.finished = True

        super().destroy()