import random
import cv2
import numpy as np


class CameraShake:

    def __init__(self):

        self.intensity = 0
        self.duration = 0

        self.decay = 18.0

        self.active = False

    def start(self, intensity=8, duration=0.35):

        # If another shake is already running,
        # keep the stronger one.
        self.intensity = max(self.intensity, intensity)
        self.duration = max(self.duration, duration)
        self.active = True

    def update(self, dt):

        if self.duration <= 0:

            self.intensity = 0
            self.active = False
            return

        self.duration -= dt

        self.intensity -= self.decay * dt

        if self.intensity < 0:
            self.intensity = 0
            self.active = False

    def apply(self, frame):

        if self.intensity <= 0:
            return frame

        dx = random.randint(
            -int(self.intensity),
            int(self.intensity)
        )

        dy = random.randint(
            -int(self.intensity),
            int(self.intensity)
        )

        h, w = frame.shape[:2]

        matrix = np.float32([
            [1, 0, dx],
            [0, 1, dy]
        ])

        shaken = cv2.warpAffine(
            frame,
            matrix,
            (w, h),
            borderMode=cv2.BORDER_REFLECT
        )

        return shaken