import math
import random

from animation_utils import AnimationUtils


class PortalParticles:

    def __init__(self):

        self.particles = []

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

        self.particles.clear()

    # ---------------------------------
    # Reset
    # ---------------------------------

    def reset(self):

        self.particles.clear()

    # ---------------------------------
    # Emit
    # ---------------------------------

    def emit(
        self,
        center,
        radius=None
    ):

        x, y = center

        if radius is None:
            radius = random.randint(65, 85)

        for _ in range(random.randint(3, 5)):

            angle = random.uniform(0, math.pi * 2)

            spawn_radius = radius + random.randint(-8, 8)

            px = x + spawn_radius * math.cos(angle)
            py = y + spawn_radius * math.sin(angle)

            self.particles.append({

                "cx": x,
                "cy": y,

                "x": px,
                "y": py,

                "angle": angle,

                "radius": spawn_radius,

                "speed": random.uniform(0.08, 0.18),

                "size": random.randint(2, 5),

                "life": random.randint(35, 55)

            })

    # ---------------------------------
    # Update
    # ---------------------------------

    def update(self, dt):

        alive = []

        for p in self.particles:

            p["angle"] += p["speed"]

            p["radius"] += 8 * dt

            p["x"] = (
                p["cx"] +
                p["radius"] * math.cos(
                    p["angle"]
                )
            )

            p["y"] = (
                p["cy"] +
                p["radius"] * math.sin(
                    p["angle"]
                )
            )

            p["life"] -= 1

            if p["life"] < 15:

                p["size"] -= 0.08

            if (
                p["life"] > 0
                and p["size"] > 0
            ):
                alive.append(p)

        self.particles = alive

    # ---------------------------------
    # Draw
    # ---------------------------------

    def draw(
        self,
        frame,
        center=None,
        radius=None
    ):

        for p in self.particles:

            if p["life"] > 35:

                color = (255, 255, 255)

            elif p["life"] > 22:

                color = (0, 255, 255)

            elif p["life"] > 10:

                color = (0, 180, 255)

            else:

                color = (0, 100, 255)

            AnimationUtils.glow_circle(

                frame,

                (
                    int(p["x"]),
                    int(p["y"])
                ),

                max(
                    1,
                    int(p["size"])
                ),

                color

            )