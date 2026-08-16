import cv2
import math


class EnergyBall:

    def __init__(self):
        self.frame = 0

    def draw(self, frame, center):

        x, y = center

        # Animation counter
        self.frame += 1

        # Pulse radius
        pulse = 25 + int(5 * math.sin(self.frame * 0.2))

        # ---------- Glow ----------
        overlay = frame.copy()

        cv2.circle(
            overlay,
            (x, y),
            pulse + 25,
            (255, 255, 0),
            -1
        )

        cv2.addWeighted(
            overlay,
            0.15,
            frame,
            0.85,
            0,
            frame
        )

        # ---------- Energy Ball ----------
        cv2.circle(
            frame,
            (x, y),
            pulse,
            (255, 180, 0),
            -1
        )

        # ---------- White Core ----------
        cv2.circle(
            frame,
            (x, y),
            pulse // 2,
            (255, 255, 255),
            -1
        )

        # ---------- Expanding Ring ----------
        ring = (self.frame * 3) % 60

        cv2.circle(
            frame,
            (x, y),
            pulse + ring,
            (255, 255, 0),
            2
        )