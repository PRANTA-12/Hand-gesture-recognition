import math

from animation_utils import AnimationUtils


class RasenganTrail:

    def __init__(self):

        self.angle = 0

    def update(self, dt):

        self.angle += 220 * dt

        if self.angle >= 360:
            self.angle -= 360

    def draw(self, frame, center):

        cx, cy = center

        # Number of trails
        trail_count = 3

        for i in range(trail_count):

            offset = self.angle + i * 120

            for j in range(16):

                a = math.radians(offset + j * 12)

                radius = 18 + j * 2.5

                x = cx + math.cos(a) * radius
                y = cy + math.sin(a) * radius

                size = max(1, 5 - j // 4)

                # Trail color
                if j < 5:
                    color = (255, 255, 255)
                elif j < 10:
                    color = (255, 220, 120)
                else:
                    color = (255, 150, 40)

                AnimationUtils.glow_circle(
                    frame,
                    (int(x), int(y)),
                    size,
                    color
                )

    def reset(self):

        self.angle = 0