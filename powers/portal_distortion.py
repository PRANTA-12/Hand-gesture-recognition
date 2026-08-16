import math
import random
import cv2


class PortalDistortion:

    def __init__(self):

        self.rotation = 0.0
        self.waves = []

        self.colors = [
            (255, 140, 0),
            (255, 180, 50),
            (255, 220, 120)
        ]

        self.reset()

    def start(self, center):

        self.reset() 

    def stop(self):

        pass  

    def clear(self):

        self.waves.clear()     

    def reset(self):

        self.rotation = 0

        self.waves.clear()

        for _ in range(12):

            self.waves.append({

                "angle": random.uniform(0, 360),
                "offset": random.uniform(0, 25),
                "speed": random.uniform(40, 90),
                "width": random.randint(18, 30)

            })

    def update(self, dt):

        self.rotation += 40 * dt

        for wave in self.waves:

            wave["angle"] += wave["speed"] * dt

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

        for wave in self.waves:

            angle = math.radians(
                wave["angle"] + self.rotation
            )

            r = radius * 0.75 + wave["offset"]

            x = int(cx + math.cos(angle) * r)
            y = int(cy + math.sin(angle) * r)

            color = random.choice(self.colors)

            cv2.ellipse(

                overlay,

                (x, y),

                (wave["width"], 4),

                wave["angle"],

                0,

                360,

                color,

                2,

                cv2.LINE_AA

            )

        # Soft center glow

        cv2.circle(

            overlay,

            center,

            int(radius * 0.65),

            (40, 90, 255),

            -1,

            cv2.LINE_AA

        )

        cv2.addWeighted(

            overlay,

            0.30,

            frame,

            0.70,

            0,

            frame

        )