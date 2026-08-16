import math
import random

from animation_utils import AnimationUtils
from physics.physics_body import PhysicsBody
from physics.vector2 import Vector2


class ExplosionEmberParticle(PhysicsBody):

    def __init__(self):

        super().__init__()

        self.radius = 3

        self.life = 0.0
        self.max_life = 0.0

    # ---------------------------------
    # Start
    # ---------------------------------

    def start(self, position):

        super().start()

        angle = random.uniform(
            0,
            2 * math.pi
        )

        speed = random.uniform(
            2.0,
            6.0
        )

        self.position = Vector2(
            position[0],
            position[1]
        )

        self.velocity = Vector2(
            math.cos(angle) * speed,
            math.sin(angle) * speed
        )

        self.acceleration = Vector2.zero()

        self.radius = random.randint(
            2,
            4
        )

        self.life = self.max_life = random.uniform(
            0.8,
            1.2
        )

    # ---------------------------------
    # Update
    # ---------------------------------

    def update(self, dt):

        if not self.active:
            return

        super().update(dt)

        # Slow down gradually
        self.velocity.x *= 0.98
        self.velocity.y *= 0.98

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

        progress = self.life / self.max_life

        if progress > 0.7:

            color = (255, 255, 255)

        elif progress > 0.4:

            color = (0, 220, 255)

        elif progress > 0.2:

            color = (0, 160, 255)

        else:

            color = (0, 80, 255)

        position = (
            int(self.position.x),
            int(self.position.y)
        )

        radius = int(self.radius)

        AnimationUtils.glow_circle(
            frame,
            position,
            radius,
            color
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

        self.radius = 3

        self.life = 0

        self.max_life = 0

    # ---------------------------------
    # Destroy
    # ---------------------------------

    def destroy(self):

        super().destroy()