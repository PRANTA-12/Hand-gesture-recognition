import random
import math

from animation_utils import AnimationUtils
from physics.vector2 import Vector2


class LightningParticle:

    def __init__(self):

        self.position = Vector2.zero()
        self.velocity = Vector2.zero()

        self.radius = 2.0

        self.life = 0.0
        self.max_life = 0.25

        self.active = False

    # ---------------------------------
    # Start
    # ---------------------------------

    def start(self, position):

        self.position = Vector2(
            position[0],
            position[1]
        )

        angle = random.uniform(
            0,
            math.pi * 2
        )

        speed = random.uniform(
            80,
            220
        )

        self.velocity = Vector2(

            math.cos(angle) * speed,

            math.sin(angle) * speed

        )

        self.radius = random.uniform(
            2,
            5
        )

        self.life = self.max_life

        self.active = True

    # ---------------------------------
    # Update
    # ---------------------------------

    def update(self, dt):

        if not self.active:
            return

        self.position += self.velocity * dt

        # Slight slowdown
        self.velocity *= 0.95

        self.life -= dt

        if self.life <= 0:

            self.life = 0

            self.active = False

    # ---------------------------------
    # Draw
    # ---------------------------------

    def draw(self, frame):

        if not self.active:
            return

        alpha = self.life / self.max_life

        if alpha > 0.7:

            color = (255, 255, 255)

        elif alpha > 0.35:

            color = (255, 220, 120)

        else:

            color = (0, 180, 255)

        AnimationUtils.glow_circle(

            frame,

            (
                int(self.position.x),
                int(self.position.y)
            ),

            max(1, int(self.radius)),

            color

        )

    # ---------------------------------
    # Is Alive
    # ---------------------------------

    def is_alive(self):

        return self.active

    # ---------------------------------
    # Reset
    # ---------------------------------

    def reset(self):

        self.active = False

        self.life = 0