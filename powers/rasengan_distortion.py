import math

import cv2
import numpy as np


class RasenganDistortion:

    def __init__(self):

        self.phase = 0

    def update(self, dt):

        self.phase += 6 * dt

    def draw(self, frame, center):

        cx, cy = center

        overlay = frame.copy()

        # Draw multiple animated distortion rings
        for i in range(5):

            radius = 45 + i * 10

            wave = int(
                4 * math.sin(
                    self.phase * 6 + i
                )
            )

            cv2.circle(
                overlay,
                (cx, cy),
                radius + wave,
                (255, 180, 80),
                2,
                cv2.LINE_AA
            )

        # Blend with original frame
        cv2.addWeighted(
            overlay,
            0.18,
            frame,
            0.82,
            0,
            frame
        )

        # Small shimmering energy dots
        for angle in range(0, 360, 20):

            r = 65 + 5 * math.sin(
                self.phase * 5 +
                math.radians(angle)
            )

            x = cx + r * math.cos(
                math.radians(angle)
            )

            y = cy + r * math.sin(
                math.radians(angle)
            )

            cv2.circle(
                frame,
                (int(x), int(y)),
                2,
                (255, 255, 255),
                -1,
                cv2.LINE_AA
            )

    def reset(self):

        self.phase = 0