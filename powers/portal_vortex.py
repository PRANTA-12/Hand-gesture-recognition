import math
import random

from animation_utils import AnimationUtils


class PortalVortex:

    def __init__(self):

        self.rotation = 0

        self.layers = []

        self.reset()

    def start(self, center):

        self.reset() 

    def stop(self):

        pass  

    def clear(self):

        self.layers.clear()

    def reset(self):

        self.rotation = 0

        self.layers.clear()

        for _ in range(6):

            self.layers.append({

                "angle": random.uniform(0, math.pi * 2),

                "speed": random.uniform(20, 60),

                "offset": random.uniform(0.3, 1.0)

            })         

    def update(self, dt):

        self.rotation += 80 * dt

        for layer in self.layers:

            layer["angle"] += math.radians(layer["speed"]) * dt

    def draw(
        self,
        frame,
        center=None,
        radius=None
    ):
        
        if center is None or radius is None:
            return

        cx, cy = center
        radius = max(radius, 45)

        # Draw spiral vortex layers
        for layer in self.layers:

            for i in range(60):

                t = i / 60.0

                r = radius * layer["offset"] * t

                angle = (
                    layer["angle"]
                    + t * math.pi * 6
                )

                x = int(
                    cx + r * math.cos(angle)
                )

                y = int(
                    cy + r * math.sin(angle)
                )

                if t < 0.35:
                    color = (255, 255, 255)

                elif t < 0.70:
                    color = (0, 220, 255)

                else:
                    color = (0, 120, 255)

                AnimationUtils.glow_circle(

                    frame,

                    (x, y),

                    2,

                    color

                )

        # Energy swirl ring
        for i in range(40):

            angle = (
                math.radians(i * 9)
                + self.rotation
            )

            r = radius * 0.8

            x = int(
                cx + r * math.cos(angle)
            )

            y = int(
                cy + r * math.sin(angle)
            )

            AnimationUtils.glow_circle(

                frame,

                (x, y),

                3,

                (0, 180, 255)

            )

        # Portal core glow
        AnimationUtils.glow_circle(

            frame,

            (cx, cy),

            int(radius * 0.45),

            (255, 255, 255)

        )

        AnimationUtils.glow_circle(

            frame,

            (cx, cy),

            int(radius * 0.60),

            (0, 180, 255)

        )