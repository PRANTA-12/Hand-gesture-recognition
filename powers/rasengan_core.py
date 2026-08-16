import math

from animation_utils import AnimationUtils


class RasenganCore:

    def __init__(self):

        self.rotation = 0
        self.pulse = 0

    def update(self, dt):

        self.rotation += 180 * dt
        self.pulse += 8 * dt

        if self.rotation >= 360:
            self.rotation -= 360

    def draw(self, frame, center):

        cx, cy = center

        # Pulsing radius
        radius = 28 + int(
            3 * math.sin(self.pulse)
        )

        # Outer glow
        AnimationUtils.glow_circle(
            frame,
            (cx, cy),
            radius + 20,
            (255, 120, 0)
        )

        # Middle glow
        AnimationUtils.glow_circle(
            frame,
            (cx, cy),
            radius + 10,
            (255, 180, 80)
        )

        # Core
        AnimationUtils.glow_circle(
            frame,
            (cx, cy),
            radius,
            (255, 255, 255)
        )

        # Rotating orbit particles
        for i in range(6):

            angle = math.radians(
                self.rotation + i * 60
            )

            x = cx + math.cos(angle) * (radius - 6)
            y = cy + math.sin(angle) * (radius - 6)

            AnimationUtils.glow_circle(
                frame,
                (int(x), int(y)),
                3,
                (255, 255, 255)
            )

        # Second rotating layer
        for i in range(6):

            angle = math.radians(
                -self.rotation * 1.5 + i * 60
            )

            x = cx + math.cos(angle) * (radius + 4)
            y = cy + math.sin(angle) * (radius + 4)

            AnimationUtils.glow_circle(
                frame,
                (int(x), int(y)),
                2,
                (255, 200, 120)
            )

    def reset(self):

        self.rotation = 0
        self.pulse = 0