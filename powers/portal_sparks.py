import math
import random

from animation_utils import AnimationUtils


class PortalSparks:

    def __init__(self):

        self.sparks = []

        self.colors = [

            (255, 255, 255),
            (0, 220, 255),
            (0, 170, 255),
            (0, 80, 255)

        ]

    # ---------------------------------
    # Start
    # ---------------------------------

    def start(self, center):

        self.reset()

    # ---------------------------------
    # Stop
    # ---------------------------------

    def stop(self):

        pass

    # ---------------------------------
    # Clear
    # ---------------------------------

    def clear(self):

        self.sparks.clear()

    # ---------------------------------
    # Reset
    # ---------------------------------

    def reset(self):

        self.sparks.clear()

    # ---------------------------------
    # Emit
    # ---------------------------------

    def emit(self, center, radius):

        if center is None or radius is None:
            return

        cx, cy = center

        for _ in range(random.randint(3, 5)):

            angle = random.uniform(0, math.pi * 2)

            x = cx + radius * math.cos(angle)
            y = cy + radius * math.sin(angle)

            speed = random.uniform(2.0, 5.0)

            self.sparks.append({

                "x": x,
                "y": y,

                "vx": math.cos(angle) * speed,
                "vy": math.sin(angle) * speed,

                "radius": random.randint(2, 4),

                "life": random.randint(18, 30)

            })

    # ---------------------------------
    # Update
    # ---------------------------------

    def update(self, dt):

        alive = []

        for spark in self.sparks:

            spark["x"] += spark["vx"] * dt * 60
            spark["y"] += spark["vy"] * dt * 60

            spark["vx"] *= 0.98
            spark["vy"] *= 0.98

            spark["radius"] -= 0.05
            spark["life"] -= 1

            if spark["life"] > 0 and spark["radius"] > 0:

                alive.append(spark)

        self.sparks = alive

    # ---------------------------------
    # Draw
    # ---------------------------------

    def draw(
        self,
        frame,
        center=None,
        radius=None
    ):

        if not self.sparks:
            return

        for spark in self.sparks:

            life = spark["life"]

            if life > 20:

                color = self.colors[0]

            elif life > 12:

                color = self.colors[1]

            elif life > 6:

                color = self.colors[2]

            else:

                color = self.colors[3]

            AnimationUtils.glow_circle(

                frame,

                (
                    int(spark["x"]),
                    int(spark["y"])
                ),

                max(1, int(spark["radius"])),

                color

            )