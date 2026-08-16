import math

from animation_utils import AnimationUtils


class KamehamehaCore:

    def __init__(self):

        self.rotation = 0
        self.pulse = 0

    def update(self, dt):

        self.rotation += 180 * dt
        self.pulse += 8 * dt

    def draw(
        self,
        frame,
        center,
        radius
    ):

        cx, cy = center

        # Animated radius
        r = radius + int(
            4 * math.sin(self.pulse)
        )

        # Outer energy glow
        AnimationUtils.glow_circle(
            frame,
            (cx, cy),
            r + 30,
            (255, 180, 0)
        )

        AnimationUtils.glow_circle(
            frame,
            (cx, cy),
            r + 18,
            (255, 120, 0)
        )

        # Core
        AnimationUtils.glow_circle(
            frame,
            (cx, cy),
            r,
            (255, 255, 255)
        )

        # Rotating energy rings
        for i in range(8):

            angle = math.radians(
                self.rotation + i * 45
            )

            x = cx + math.cos(angle) * (r + 10)
            y = cy + math.sin(angle) * (r + 10)

            AnimationUtils.glow_circle(
                frame,
                (
                    int(x),
                    int(y)
                ),
                5,
                (255, 220, 150)
            )

        # Inner orbit
        for i in range(6):

            angle = math.radians(
                -self.rotation * 1.5 + i * 60
            )

            x = cx + math.cos(angle) * (r - 8)
            y = cy + math.sin(angle) * (r - 8)

            AnimationUtils.glow_circle(
                frame,
                (
                    int(x),
                    int(y)
                ),
                3,
                (255, 255, 255)
            )