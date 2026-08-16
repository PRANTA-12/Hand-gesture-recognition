import random

from physics.physics_body import PhysicsBody
from physics.vector2 import Vector2
from animation_utils import AnimationUtils


class ExplosionParticle(PhysicsBody):

    def __init__(self):
        super().__init__()

        # -------------------------
        # Physics
        # -------------------------

        self.radius = random.uniform(3, 8)

        self.mass = 0.5

        self.drag = 0.96

        self.gravity = Vector2(0, 120)

        self.bounce = 0.20

        self.max_speed = 700

        # -------------------------
        # Life
        # -------------------------

        self.life = 0.0

        self.max_life = random.uniform(
            0.5,
            0.9
        )

    # ---------------------------------
    # Start
    # ---------------------------------

    def start(self, position):

        super().start()

        self.position = Vector2(
            position[0],
            position[1]
        )

        angle = random.uniform(0, 360)

        speed = random.uniform(
            200,
            600
        )

        self.velocity = Vector2.from_angle(
            angle,
            speed
        )

        self.acceleration = Vector2.zero()

        self.life = 0.0

    # ---------------------------------
    # Update
    # ---------------------------------

    def update(self, dt):

        if not self.active:
            return

        super().update(dt)

        self.life += dt

        # Particle shrinks over time
        self.radius -= dt * 8

        expired = self.life >= self.max_life
        too_small = self.radius <= 0

        if expired or too_small:
            self.destroy()

    # ---------------------------------
    # Draw
    # ---------------------------------

    def draw(self, frame):

        if not self.active:
            return

        t = self.life / self.max_life

        if t < 0.25:

            color = (255, 255, 255)

        elif t < 0.50:

            color = (0, 255, 255)

        elif t < 0.75:

            color = (0, 180, 255)

        else:

            color = (0, 80, 255)

        position = (
            int(self.position.x),
            int(self.position.y)
        )

        radius = max(
            1,
            int(self.radius)
        )

        AnimationUtils.glow_circle(
            frame,
            position,
            radius,
            color
        )

    # ---------------------------------
    # Reset
    # ---------------------------------

    def reset(self):

        super().reset()

        self.radius = random.uniform(
            3,
            8
        )

        self.life = 0.0

    # ---------------------------------
    # Destroy
    # ---------------------------------

    def destroy(self):

        super().destroy()    