import math
import cv2

from powers.base_animation import BaseAnimation


class PortalExit(BaseAnimation):

    def __init__(self):

        super().__init__()

        self.center = (0, 0)

        self.radius = 0
        self.max_radius = 100

        self.life = 0.0
        self.max_life = 0.50

        self.rotation = 0

    # ---------------------------------
    # Start
    # ---------------------------------

    def start(
        self,
        center,
        radius
    ):

        super().start()

        self.center = center

        self.radius = radius
        self.max_radius = radius

        self.life = self.max_life

        self.rotation = 0

    # ---------------------------------
    # Stop
    # ---------------------------------

    def stop(self):

        super().stop()

    # ---------------------------------
    # Reset
    # ---------------------------------

    def reset(self):

        self.active = False

        self.radius = 0
        self.life = 0

        self.rotation = 0

    # ---------------------------------
    # Clear
    # ---------------------------------

    def clear(self):

        self.reset()

    # ---------------------------------
    # Update
    # ---------------------------------

    def update(self, dt):

        if not self.active:
            return

        self.life -= dt

        if self.life <= 0:

            self.stop()
            return

        progress = self.life / self.max_life

        self.radius = self.max_radius * progress

        self.rotation += 240 * dt

    # ---------------------------------
    # Draw
    # ---------------------------------

    def draw(
        self,
        frame,
        center=None,
        radius=None
    ):

        if not self.active:
            return

        if center is not None:
            self.center = center

        cx, cy = self.center

        overlay = frame.copy()

        alpha = self.life / self.max_life

        # Outer shrinking ring

        cv2.circle(

            overlay,

            (cx, cy),

            max(1, int(self.radius)),

            (0, 180, 255),

            2,

            cv2.LINE_AA

        )

        # Inner shrinking ring

        cv2.circle(

            overlay,

            (cx, cy),

            max(1, int(self.radius * 0.65)),

            (255, 255, 255),

            2,

            cv2.LINE_AA

        )

        # Rotating sparks

        for i in range(8):

            angle = math.radians(
                self.rotation + i * 45
            )

            x = int(
                cx +
                self.radius *
                math.cos(angle)
            )

            y = int(
                cy +
                self.radius *
                math.sin(angle)
            )

            cv2.circle(

                overlay,

                (x, y),

                3,

                (255, 220, 120),

                -1,

                cv2.LINE_AA

            )

        # Center glow

        cv2.circle(

            overlay,

            (cx, cy),

            max(1, int(self.radius * 0.25)),

            (255, 255, 255),

            -1,

            cv2.LINE_AA

        )

        cv2.addWeighted(

            overlay,

            alpha,

            frame,

            1.0,

            0,

            frame

        )

    # ---------------------------------
    # Finished?
    # ---------------------------------

    def is_finished(self):

        return not self.active