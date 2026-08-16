import cv2
import math


class Effects:

    def __init__(self):
        self.angle = 0

    def draw_glow(self, frame, center, color=(255, 255, 0)):

        x, y = center

        h, w = frame.shape[:2]

        x = max(0, min(x, w - 1))
        y = max(0, min(y, h - 1))

        # Outer Glow
        for r in range(60, 10, -10):

            alpha = (r / 60) ** 2

            overlay = frame.copy()

            cv2.circle(
                overlay,
                (x, y),
                r,
                color,
                -1
            )

            cv2.addWeighted(
                overlay,
                alpha * 0.08,
                frame,
                1 - alpha * 0.08,
                0,
                frame
            )

        # Bright Core
        cv2.circle(
            frame,
            (x, y),
            12,
            (255, 255, 255),
            -1
        )

        # Small Energy Ring
        cv2.circle(
            frame,
            (x, y),
            20,
            color,
            2
        )

    def draw_rotating_ring(self, frame, center, radius=35):

        x, y = center

        self.angle = (self.angle + 5) % 360

        for i in range(4):

            angle = math.radians(self.angle + i * 90)

            px = int(x + radius * math.cos(angle))
            py = int(y + radius * math.sin(angle))

            cv2.circle(
                frame,
                (px, py),
                6,
                (0, 255, 255),
                -1
            )