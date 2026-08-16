import math
import random

from animation_utils import AnimationUtils


class KamehamehaParticles:

    def __init__(self):

        self.particles = []

    def emit(
        self,
        center,
        angle,
        beam_length
    ):

        cx, cy = center

        # Create 6 particles every frame
        for _ in range(6):

            distance = random.uniform(0, beam_length)

            bx = cx + math.cos(angle) * distance
            by = cy + math.sin(angle) * distance

            # Offset around the beam
            offset = random.uniform(-18, 18)

            px = bx + math.cos(angle + math.pi / 2) * offset
            py = by + math.sin(angle + math.pi / 2) * offset

            self.particles.append({

                "x": px,
                "y": py,

                "vx": random.uniform(-1.2, 1.2),
                "vy": random.uniform(-1.2, 1.2),

                "radius": random.randint(2, 5),

                "life": random.randint(20, 35)

            })

    def update(self, dt):

        for p in self.particles[:]:

            p["x"] += p["vx"] * dt * 60
            p["y"] += p["vy"] * dt * 60

            p["radius"] -= 0.06
            p["life"] -= 1

            if p["radius"] <= 0 or p["life"] <= 0:

                self.particles.remove(p)

    def draw(self, frame):

        for p in self.particles:

            life = p["life"]

            if life > 24:

                color = (255, 255, 255)

            elif life > 16:

                color = (255, 220, 150)

            elif life > 8:

                color = (255, 170, 60)

            else:

                color = (255, 100, 20)

            AnimationUtils.glow_circle(

                frame,

                (
                    int(p["x"]),
                    int(p["y"])
                ),

                max(1, int(p["radius"])),

                color

            )

    def clear(self):

        self.particles.clear()