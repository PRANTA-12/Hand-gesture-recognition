import cv2
import math
from powers.base_power import BasePower


class GravityOrb(BasePower):

    def __init__(self):

        BasePower.__init__(self)
        self.center = (0, 0)

        self.radius = 40
        self.rotation = 0
        self.pulse = 0

    # -----------------------
    # Start
    # -----------------------

    def start(self, center):

        BasePower.start(self)
        self.center = center
        self.rotation = 0
        self.pulse = 0

    # -----------------------
    # Move
    # -----------------------

    def move(self, center):

        self.center = center

    # -----------------------
    # Stop
    # -----------------------

    def stop(self):

        BasePower.stop(self)

    # -----------------------
    # Update
    # -----------------------

    def update(self, frame=None, dt=None):

        if not self.active:
            return

        self.rotation += 4
        self.pulse += 0.15

    # -----------------------
    # Draw
    # -----------------------

    def draw(self, frame):

        if not self.active:
            return

        self.update(frame)

        cx, cy = self.center

        pulse_radius = int(
            self.radius +
            math.sin(self.pulse) * 6
        )

        # Glow
        for i in range(4):

            cv2.circle(
                frame,
                (cx, cy),
                pulse_radius + i * 8,
                (255, 60, 255),
                2
            )

        # Core
        cv2.circle(
            frame,
            (cx, cy),
            pulse_radius,
            (255, 255, 255),
            -1
        )

        # Rotating particles
        for angle in range(0, 360, 30):

            a = math.radians(
                angle + self.rotation
            )

            x = int(
                cx +
                math.cos(a) *
                (pulse_radius + 20)
            )

            y = int(
                cy +
                math.sin(a) *
                (pulse_radius + 20)
            )

            cv2.circle(
                frame,
                (x, y),
                4,
                (255, 0, 255),
                -1
            )

        # Orbit ring
        cv2.circle(
            frame,
            (cx, cy),
            pulse_radius + 20,
            (180, 0, 255),
            2
        )

        cv2.circle(
            frame,
            (cx, cy),
            pulse_radius + 35,
            (120, 0, 200),
            1
        )