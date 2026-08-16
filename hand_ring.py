import cv2
import math


class HandRing:

    def __init__(self):
        self.angle = 0
        self.finger_angle = 0

    def draw(self, frame, center):

        x, y = center

        # Outer rotating arc
        cv2.ellipse(
            frame,
            (x, y),
            (45, 45),
            self.angle,
            0,
            270,
            (255, 255, 0),
            2,
            lineType=cv2.LINE_AA
        )

        # Inner ring
        cv2.circle(
            frame,
            (x, y),
            32,
            (180, 255, 255),
            1,
            lineType=cv2.LINE_AA
        )

        # Center glow
        cv2.circle(
            frame,
            (x, y),
            5,
            (255, 255, 255),
            -1,
            lineType=cv2.LINE_AA
        )

        self.angle += 2

        if self.angle >= 360:
            self.angle = 0

        self.finger_angle += 5

        if self.finger_angle >= 360:
            self.finger_angle = 0    