import cv2
import math
from powers.base_power import BasePower


class ArcReactor(BasePower):

    def __init__(self):

        BasePower.__init__(self)
        
        self.center = (0, 0)

        self.radius = 35
        self.rotation = 0
        self.pulse = 0

    # -----------------------------
    # Start
    # -----------------------------
    def start(self, center):

        BasePower.start(self)
        self.center = center
        self.rotation = 0
        self.pulse = 0

    # -----------------------------
    # Move
    # -----------------------------
    def move(self, center):

        self.center = center

    # -----------------------------
    # Stop
    # -----------------------------
    def stop(self):

        BasePower.stop(self)

    # -----------------------------
    # Update
    # -----------------------------
    def update(self, frame=None, dt=None):

        if not self.active:
            return

        self.rotation += 5
        self.pulse += 0.15

    # -----------------------------
    # Draw
    # -----------------------------
    def draw(self, frame):

        if not self.active:
            return

        self.update(frame)

        cx, cy = self.center

        pulse = int(
            self.radius +
            math.sin(self.pulse) * 5
        )

        # Outer glow
        for i in range(5):

            cv2.circle(
                frame,
                (cx, cy),
                pulse + i * 6,
                (255, 180, 0),
                2
            )

        # Rotating ring
        cv2.ellipse(
            frame,
            (cx, cy),
            (pulse + 18, pulse + 18),
            self.rotation,
            0,
            360,
            (255, 255, 0),
            2
        )

        cv2.ellipse(
            frame,
            (cx, cy),
            (pulse + 28, pulse + 28),
            -self.rotation,
            0,
            360,
            (255, 220, 50),
            2
        )

        # Energy core
        cv2.circle(
            frame,
            (cx, cy),
            pulse,
            (255, 255, 255),
            -1
        )

        cv2.circle(
            frame,
            (cx, cy),
            pulse - 10,
            (255, 255, 120),
            -1
        )

        cv2.circle(
            frame,
            (cx, cy),
            pulse - 18,
            (255, 240, 0),
            -1
        )

        # Orbiting particles
        for angle in range(0, 360, 45):

            a = math.radians(
                angle + self.rotation * 2
            )

            x = int(
                cx +
                math.cos(a) *
                (pulse + 30)
            )

            y = int(
                cy +
                math.sin(a) *
                (pulse + 30)
            )

            cv2.circle(
                frame,
                (x, y),
                4,
                (255, 255, 255),
                -1
            )

        # Cross lines
        cv2.line(
            frame,
            (cx - pulse, cy),
            (cx + pulse, cy),
            (255, 255, 255),
            2
        )

        cv2.line(
            frame,
            (cx, cy - pulse),
            (cx, cy + pulse),
            (255, 255, 255),
            2
        )

        # Small center glow
        cv2.circle(
            frame,
            (cx, cy),
            5,
            (255, 255, 255),
            -1
        )