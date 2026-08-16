import math
import random
import cv2


class PortalGalaxy:

    def __init__(self):

        self.stars = []
        self.rotation = 0
        self.nebula_colors = [

            (120, 40, 255),
            (180, 80, 255),
            (255, 120, 180),
            (255, 80, 120),
            (255, 180, 80)

        ]

        self.reset()

    def start(self, center):

        self.reset()

    def stop(self):

        pass 

    def clear(self):

        self.stars.clear()       

    def reset(self):

        self.rotation = 0
        self.stars.clear()

        # Generate stars
        for _ in range(80):

            self.stars.append({

                "angle": random.uniform(0, math.pi * 2),
                "distance": random.uniform(5, 1.0),
                "size": random.randint(1, 3),

                "speed": random.uniform(10, 40),

                "color": random.choice([
                    (255, 255, 255),
                    (255, 220, 180),
                    (255, 255, 180),
                    (255, 180, 120)
                ]),

                "blink": random.uniform(0, math.pi * 2)

            })

    def update(self, dt):

        self.rotation += 20 * dt

        for star in self.stars:

            star["angle"] += math.radians(
                star["speed"] * dt
            )

            star["blink"] += dt * 5

    def draw(
        self,
        frame,
        center=None,
        radius=None
    ):
        
        if center is None or radius is None:
            return

        if radius < 20:
            return

        overlay = frame.copy()

        cx, cy = center

        # ---------
        # Nebula
        # ---------

        for i in range(5):

            nebula_radius = int(radius * (0.25 + i * 0.12))

            color = self.nebula_colors[i]

            cv2.circle(

                overlay,

                center,

                nebula_radius,

                color,

                -1,

                cv2.LINE_AA

            )

        # ---------
        # Stars
        # ---------

        for star in self.stars:

            r = star["distance"] * radius * 0.85

            angle = star["angle"] + math.radians(self.rotation)

            x = int(cx + math.cos(angle) * r)
            y = int(cy + math.sin(angle) * r)

            brightness = (
                math.sin(star["blink"]) + 1
            ) / 2

            color = tuple(
                int(c * brightness)
                for c in star["color"]
            )

            cv2.circle(

                overlay,

                (x, y),

                star["size"],

                color,

                -1,

                cv2.LINE_AA

            )

        # ---------
        # Blend
        # ---------

        cv2.addWeighted(

            overlay,

            0.35,

            frame,

            0.65,

            0,

            frame

        )