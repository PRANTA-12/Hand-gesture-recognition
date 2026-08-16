import cv2

from powers.base_animation import BaseAnimation


class PortalFlash(BaseAnimation):

    def __init__(self):

        super().__init__()

        self.center = (0, 0)

        self.life = 0.0
        self.max_life = 0.25

        self.radius = 0
        self.max_radius = 170

    # ---------------------------------
    # Start
    # ---------------------------------

    def start(self, center):

        super().start()

        self.center = center

        self.life = self.max_life
        self.radius = 20

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

        self.life = 0.0
        self.radius = 0

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

        progress = 1 - (self.life / self.max_life)

        self.radius = int(
            20 +
            progress *
            (self.max_radius - 20)
        )

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

        alpha = self.life / self.max_life

        overlay = frame.copy()

        # Outer Glow
        cv2.circle(
            overlay,
            self.center,
            self.radius,
            (0, 180, 255),
            -1,
            cv2.LINE_AA
        )

        # Middle Glow
        cv2.circle(
            overlay,
            self.center,
            int(self.radius * 0.65),
            (100, 220, 255),
            -1,
            cv2.LINE_AA
        )

        # White Core
        cv2.circle(
            overlay,
            self.center,
            int(self.radius * 0.35),
            (255, 255, 255),
            -1,
            cv2.LINE_AA
        )

        cv2.addWeighted(
            overlay,
            alpha * 0.7,
            frame,
            1.0,
            0,
            frame
        )