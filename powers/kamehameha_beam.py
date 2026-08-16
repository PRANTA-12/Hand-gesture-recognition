import math
import cv2

from animation_utils import AnimationUtils


class KamehamehaBeam:

    def __init__(self):

        self.length = 0
        self.target_length = 800

        self.width = 30

        self.pulse = 0

    def update(self, dt):

        self.pulse += 10 * dt

        # Beam grows smoothly
        if self.length < self.target_length:

            self.length += 1600 * dt

            if self.length > self.target_length:
                self.length = self.target_length

    def reset(self):

        self.length = 0
        self.pulse = 0

    def draw(
        self,
        frame,
        center,
        angle
    ):

        cx, cy = center

        ex = int(
            cx + math.cos(angle) * self.length
        )

        ey = int(
            cy + math.sin(angle) * self.length
        )

        beam_width = int(
            self.width +
            4 * math.sin(self.pulse)
        )

        # ============================
        # Outer Glow
        # ============================

        overlay = frame.copy()

        cv2.line(
            overlay,
            (cx, cy),
            (ex, ey),
            (255, 120, 0),
            beam_width + 28,
            cv2.LINE_AA
        )

        cv2.addWeighted(
            overlay,
            0.20,
            frame,
            0.80,
            0,
            frame
        )

        # ============================
        # Middle Glow
        # ============================

        overlay = frame.copy()

        cv2.line(
            overlay,
            (cx, cy),
            (ex, ey),
            (255, 200, 120),
            beam_width + 12,
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

        # ============================
        # Beam Core
        # ============================

        cv2.line(
            frame,
            (cx, cy),
            (ex, ey),
            (255, 255, 255),
            beam_width,
            cv2.LINE_AA
        )

        # ============================
        # Beam Center Glow
        # ============================

        for i in range(0, int(self.length), 35):

            px = int(
                cx + math.cos(angle) * i
            )

            py = int(
                cy + math.sin(angle) * i
            )

            AnimationUtils.glow_circle(
                frame,
                (px, py),
                4,
                (255, 255, 255)
            )

        # ============================
        # Impact Glow
        # ============================

        AnimationUtils.glow_circle(
            frame,
            (ex, ey),
            beam_width + 20,
            (255, 220, 120)
        )

        AnimationUtils.glow_circle(
            frame,
            (ex, ey),
            beam_width,
            (255, 255, 255)
        )