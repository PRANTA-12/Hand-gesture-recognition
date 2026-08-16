import random
import math

from animation_utils import AnimationUtils
from physics.physics_body import PhysicsBody
from physics.vector2 import Vector2


class ExplosionDebrisParticle(PhysicsBody):

    def __init__(self):

        super().__init__()

        self.radius = 3

        self.life = 0.0
        self.max_life = 0.0

        self.rotation = 0.0
        self.rotation_speed = 0.0

    # ---------------------------------
    # Start
    # ---------------------------------

    def start(self, position):

        super().start()

        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(4.0, 10.0)

        self.position = Vector2(
            position[0],
            position[1]
        )

        self.velocity = Vector2(
            math.cos(angle) * speed,
            math.sin(angle) * speed
        )

        # Gravity
        self.acceleration = Vector2(
            0,
            8.0
        )

        self.radius = random.randint(2, 4)

        self.life = self.max_life = random.uniform(
            0.5,
            0.9
        )

        self.rotation = random.uniform(
            0,
            360
        )

        self.rotation_speed = random.uniform(
            -500,
            500
        )

    # ---------------------------------
    # Update
    # ---------------------------------

    def update(self, dt):

        if not self.active:
            return

        super().update(dt)

        self.rotation += self.rotation_speed * dt

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

        AnimationUtils.glow_circle(
            frame,
            position,
            radius,
            (80, 80, 80)
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

        self.rotation = 0

        self.rotation_speed = 0

    # ---------------------------------
    # Destroy
    # ---------------------------------

    def destroy(self):

        super().destroy()
        