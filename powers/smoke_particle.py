import random

import cv2

from physics.physics_body import PhysicsBody
from physics.vector2 import Vector2
from animation_utils import AnimationUtils


class SmokeParticle(PhysicsBody):

    def __init__(self):
        super().__init__()

        # -------------------------
        # Physics
        # -------------------------

        self.radius = random.uniform(4, 7)
        self.mass = 0.3
        self.drag = 0.97
        self.gravity = Vector2(0, -5)

        # -------------------------
        # Lifetime
        # -------------------------

        self.max_life = 0.6
        self.life = 0.0

        # -------------------------
        # Appearance
        # -------------------------

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

            random.uniform(-25, 25),

            random.uniform(-90, -35)

        )

        self.acceleration = Vector2.zero()

        self.life = 0.0

        self.alpha = 1.0

        self.radius = random.uniform(4, 7)

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

        self.radius += 18 * dt

        self.alpha = 1.0 - progress

        if progress >= 1.0:

            self.destroy()

    # ---------------------------------
    # Draw
    # ---------------------------------

    def draw(self, frame):

        if not self.active:
            return

        AnimationUtils.smoke_cloud(

            frame,

            (
                int(self.position.x),
                int(self.position.y)
            ),

            int(self.radius)

        )

    # ---------------------------------
    # Reset
    # ---------------------------------

    def reset(self):

        super().reset()

        self.alpha = 1.0

    # ---------------------------------
    # Destroy
    # ---------------------------------

    def destroy(self):

        super().destroy()