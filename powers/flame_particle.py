import random

from physics.physics_body import PhysicsBody
from physics.vector2 import Vector2
from animation_utils import AnimationUtils


class FlameParticle(PhysicsBody):

    def __init__(self):
        super().__init__()

        # -------------------------
        # Physics
        # -------------------------

        self.radius = random.uniform(2, 5)

        self.mass = 0.2

        self.drag = 0.94

        self.gravity = Vector2(0, -10)

        self.max_speed = 250

        # -------------------------
        # Lifetime
        # -------------------------

        self.max_life = 0.35

        self.life = 0

        # -------------------------
        # Visual
        # -------------------------

        self.color = (0, 180, 255)

        self.alpha = 1.0

    # ---------------------------------
    # Spawn
    # ---------------------------------

    def start(self, position):

        super().start()

        self.position = Vector2(
            position[0],
            position[1]
        )

        self.velocity = Vector2(

            random.uniform(-40, 40),

            random.uniform(-140, -70)

        )

        self.acceleration = Vector2.zero()

        self.radius = random.uniform(2, 5)

        self.life = 0

        self.alpha = 1.0

    # ---------------------------------
    # Update
    # ---------------------------------

    def update(self, dt):

        if not self.active:
            return

        super().update(dt)

        progress = min(
            self.life / self.max_life,
            1.0
        )

        self.radius += 10 * dt

        self.alpha = 1.0 - progress

        if progress > 0.65:

            self.color = (0, 120, 255)

        if progress > 0.90:

            self.color = (80, 80, 80)

        if progress >= 1.0:

            self.destroy()

    # ---------------------------------
    # Draw
    # ---------------------------------

    def draw(self, frame):

        if not self.active:
            return

        AnimationUtils.glow_circle(

            frame,

            (
                int(self.position.x),
                int(self.position.y)
            ),

            int(self.radius),

            self.color

        )

    # ---------------------------------
    # Reset
    # ---------------------------------

    def reset(self):

        super().reset()

        self.alpha = 1.0

        self.color = (0, 180, 255)

    # ---------------------------------
    # Destroy
    # ---------------------------------

    def destroy(self):

        super().destroy()