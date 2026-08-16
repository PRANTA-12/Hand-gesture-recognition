import math
import random

from animation_utils import AnimationUtils


class RasenganParticles:

    def __init__(self):

        self.particles = []

    def emit(self, center):

        cx, cy = center

        for _ in range(4):

            angle = random.uniform(0, math.pi * 2)

            orbit = random.randint(25, 45)

            self.particles.append({

                "cx": cx,
                "cy": cy,

                "angle": angle,

                "orbit": orbit,

                "speed": random.uniform(2.0, 5.0),

                "radius": random.randint(2, 5),

                "life": random.randint(40, 60)

            })

    def update(self, dt):

        for p in self.particles[:]:

            p["angle"] += p["speed"] * dt

            p["life"] -= 1

            if p["life"] <= 0:

                self.particles.remove(p)

    def draw(self, frame, center):

        cx, cy = center

        for p in self.particles:

            x = cx + math.cos(p["angle"]) * p["orbit"]

            y = cy + math.sin(p["angle"]) * p["orbit"]

            if p["life"] > 40:

                color = (255, 255, 255)

            elif p["life"] > 20:

                color = (255, 220, 120)

            else:

                color = (255, 180, 0)

            AnimationUtils.glow_circle(

                frame,

                (int(x), int(y)),

                p["radius"],

                color

            )

    def clear(self):

        self.particles.clear()