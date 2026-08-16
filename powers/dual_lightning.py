import cv2
import math
import random
from powers.base_power import BasePower


class DualLightning(BasePower):

    def __init__(self):

        BasePower.__init__(self)

        self.left = (0, 0)
        self.right = (0, 0)

        self.branches = []

        self.frame = 0

    # -----------------------------
    # Start
    # -----------------------------

    def start(self, left_center, right_center):

        BasePower.start(self)

        self.left = left_center
        self.right = right_center

        self.branches.clear()

    # -----------------------------
    # Move
    # -----------------------------

    def move(self, left_center, right_center):

        self.left = left_center
        self.right = right_center

    # -----------------------------
    # Stop
    # -----------------------------

    def stop(self):

        BasePower.stop(self)

        self.branches.clear()

    # -----------------------------
    # Update
    # -----------------------------

    def update(self, frame=None, dt=None):

        if not self.active:
            return

        self.frame += 1

        self.branches.clear()

        x1, y1 = self.left
        x2, y2 = self.right

        points = []

        segments = 16

        for i in range(segments + 1):

            t = i / segments

            x = int(x1 + (x2 - x1) * t)
            y = int(y1 + (y2 - y1) * t)

            if i != 0 and i != segments:

                x += random.randint(-18, 18)
                y += random.randint(-18, 18)

            points.append((x, y))

        self.branches = points

    # -----------------------------
    # Draw
    # -----------------------------

    def draw(self, frame):

        if not self.active:
            return

        # glow

        for i in range(len(self.branches) - 1):

            cv2.line(

                frame,

                self.branches[i],

                self.branches[i + 1],

                (255, 255, 120),

                8,

                cv2.LINE_AA

            )

        # core

        for i in range(len(self.branches) - 1):

            cv2.line(

                frame,

                self.branches[i],

                self.branches[i + 1],

                (255, 255, 255),

                3,

                cv2.LINE_AA

            )

        # sparks

        for x, y in self.branches:

            for _ in range(2):

                dx = random.randint(-12, 12)
                dy = random.randint(-12, 12)

                cv2.line(

                    frame,

                    (x, y),

                    (x + dx, y + dy),

                    (255, 255, 180),

                    1,

                    cv2.LINE_AA

                )

        # energy balls

        pulse = int(6 + 2 * math.sin(self.frame * 0.3))

        cv2.circle(
            frame,
            self.left,
            pulse + 12,
            (255, 220, 120),
            2,
            cv2.LINE_AA
        )

        cv2.circle(
            frame,
            self.right,
            pulse + 12,
            (255, 220, 120),
            2,
            cv2.LINE_AA
        )

        cv2.circle(
            frame,
            self.left,
            8,
            (255, 255, 255),
            -1,
            cv2.LINE_AA
        )

        cv2.circle(
            frame,
            self.right,
            8,
            (255, 255, 255),
            -1,
            cv2.LINE_AA
        )