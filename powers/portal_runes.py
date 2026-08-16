import cv2
import math

from animation_utils import AnimationUtils


class PortalRunes:

    def __init__(self):

        self.outer_rotation = 0
        self.inner_rotation = 0

        self.outer_count = 12
        self.inner_count = 8

        self.reset()

    # ---------------------------------
    # Start
    # ---------------------------------

    def start(self, center):

        self.reset()

    # ---------------------------------
    # Stop
    # ---------------------------------

    def stop(self):

        pass

    # ---------------------------------
    # Clear
    # ---------------------------------

    def clear(self):

        self.outer_rotation = 0
        self.inner_rotation = 0

    # ---------------------------------
    # Reset
    # ---------------------------------

    def reset(self):

        self.outer_rotation = 0
        self.inner_rotation = 0

    # ---------------------------------
    # Update
    # ---------------------------------

    def update(self, dt):

        self.outer_rotation += 60 * dt
        self.inner_rotation -= 90 * dt

        if self.outer_rotation >= 360:
            self.outer_rotation -= 360

        if self.inner_rotation <= -360:
            self.inner_rotation += 360

    # ---------------------------------
    # Draw
    # ---------------------------------

    def draw(
        self,
        frame,
        center=None,
        radius=None
    ):

        if center is None or radius is None:
            return

        cx, cy = center
        radius = max(radius, 45)

        # ==========================
        # Outer Magic Circle
        # ==========================

        AnimationUtils.ring(
            frame,
            center,
            radius,
            (0, 180, 255),
            2
        )

        AnimationUtils.ring(
            frame,
            center,
            radius + 6,
            (0, 120, 255),
            1
        )

        # ==========================
        # Inner Magic Circle
        # ==========================

        AnimationUtils.ring(
            frame,
            center,
            max(1, radius - 22),
            (255, 255, 255),
            2
        )

        # ==========================
        # Outer Rune Symbols
        # ==========================

        for i in range(self.outer_count):

            angle = (
                math.radians(self.outer_rotation)
                + i * 2 * math.pi / self.outer_count
            )

            x = int(
                cx + radius * math.cos(angle)
            )

            y = int(
                cy + radius * math.sin(angle)
            )

            AnimationUtils.glow_circle(
                frame,
                (x, y),
                3,
                (0, 180, 255)
            )

            x2 = int(
                cx + (radius - 10) * math.cos(angle)
            )

            y2 = int(
                cy + (radius - 10) * math.sin(angle)
            )

            cv2.line(
                frame,
                (x, y),
                (x2, y2),
                (0, 180, 255),
                1,
                cv2.LINE_AA
            )

        # ==========================
        # Inner Rune Symbols
        # ==========================

        inner_radius = max(1, radius - 25)

        for i in range(self.inner_count):

            angle = (
                math.radians(self.inner_rotation)
                + i * 2 * math.pi / self.inner_count
            )

            x = int(
                cx + inner_radius * math.cos(angle)
            )

            y = int(
                cy + inner_radius * math.sin(angle)
            )

            AnimationUtils.glow_circle(
                frame,
                (x, y),
                2,
                (255, 255, 255)
            )

        # ==========================
        # Cross Energy Lines
        # ==========================

        for i in range(6):

            angle = (
                math.radians(self.outer_rotation * 0.5)
                + i * math.pi / 3
            )

            line_start = max(1, radius - 40)
            line_end = max(1, radius - 5)

            x1 = int(
                cx + line_start * math.cos(angle)
            )

            y1 = int(
                cy + line_start * math.sin(angle)
            )

            x2 = int(
                cx + line_end * math.cos(angle)
            )

            y2 = int(
                cy + line_end * math.sin(angle)
            )

            cv2.line(
                frame,
                (x1, y1),
                (x2, y2),
                (255, 255, 255),
                1,
                cv2.LINE_AA
            )