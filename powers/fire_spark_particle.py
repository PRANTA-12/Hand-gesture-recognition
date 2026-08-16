import random

from physics.physics_body import PhysicsBody
from physics.vector2 import Vector2

from animation_utils import AnimationUtils


class FireSparkParticle(PhysicsBody):

    def __init__(self):

        super().__init__()

        # -------------------------
        # Physics
        # -------------------------

        self.radius = random.randint(2, 4)

        self.mass = 0.15

        self.drag = 0.96

        self.gravity = Vector2(
            0,
            12
        )

        self.bounce = 0.0

        self.max_speed = 450

        # -------------------------
        # Lifetime
        # -------------------------

        self.life = 0

        self.max_life = random.uniform(
            0.25,
            0.45
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

        self.velocity = Vector2(

            random.uniform(-4.5, 4.5),

            random.uniform(-5.5, -2.0)

        )

        self.acceleration = Vector2.zero()

        self.radius = random.randint(2, 4)

        self.life = 0

        self.alive = True

    # ---------------------------------
    # Update
    # ---------------------------------

    def update(self, dt):

        if not self.active:
            return

        super().update(dt)

        self.life += dt

        self.radius -= dt * 6

        if self.life >= self.max_life:

            self.destroy()

    # ---------------------------------
    # Draw
    # ---------------------------------

    def draw(self, frame):

        if not self.alive:
            return

        ratio = self.life / self.max_life

        if ratio < 0.30:

            color = (
                255,
                255,
                255
            )

        elif ratio < 0.60:

            color = (
                0,
                255,
                255
            )

        elif ratio < 0.85:

            color = (
                0,
                180,
                255
            )

        else:

            color = (
                0,
                100,
                255
            )

        AnimationUtils.glow_circle(

            frame,

            (
                int(self.position.x),
                int(self.position.y)
            ),

            max(
                1,
                int(self.radius)
            ),

            color

        )

    # ---------------------------------
    # Reset
    # ---------------------------------

    def reset(self):

        super().reset()

        self.radius = random.randint(
            2,
            4
        )

    # ---------------------------------
    # Destroy
    # ---------------------------------

    def destroy(self):

        super().destroy()