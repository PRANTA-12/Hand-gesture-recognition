import random

from animation_utils import AnimationUtils
from physics.physics_body import PhysicsBody
from physics.vector2 import Vector2


class ExplosionSmokeParticle(PhysicsBody):

    def __init__(self):

        super().__init__()

        self.radius = 10.0

        self.life = 0.0
        self.max_life = 1.0

    # ---------------------------------
    # Start
    # ---------------------------------

    def start(self, position):

        super().start()

        self.position = Vector2(
            position[0],
            position[1]
        )

        self.velocity = Vector2(
            random.uniform(-2.0, 2.0),
            random.uniform(-3.0, -1.0)
        )

        self.acceleration = Vector2(
            0,
            -0.2
        )

        self.radius = random.uniform(
            8,
            16
        )

        self.life = self.max_life = random.uniform(
            0.7,
            1.2
        )

    # ---------------------------------
    # Update
    # ---------------------------------

    def update(self, dt):

        if not self.active:
            return

        super().update(dt)

        self.radius += 8 * dt

        self.life -= dt

        expired = self.life <= 0

        if expired:
            self.destroy()

    # ---------------------------------
    # Draw
    # ---------------------------------

    def draw(self, frame):

        if not self.active:
            return

        position = (
            int(self.position.x),
            int(self.position.y)
        )

        radius = int(self.radius)

        AnimationUtils.smoke_cloud(
            frame,
            position,
            radius
        )
    # ---------------------------------
    # Alive
    # ---------------------------------

    def is_alive(self):

        return self.active

    # ---------------------------------
    # Reset
    # ---------------------------------

    def reset(self):

        super().reset()

        self.radius = 10

        self.life = 0

    # ---------------------------------
    # Destroy
    # ---------------------------------

    def destroy(self):

        super().destroy()