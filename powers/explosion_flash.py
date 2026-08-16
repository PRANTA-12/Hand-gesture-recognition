import cv2

from animation_utils import AnimationUtils


class ExplosionFlash:

    def __init__(self):

        self.active = False

        self.x = 0
        self.y = 0

        self.radius = 0.0
        self.max_radius = 45.0

        self.life = 0.0
        self.max_life = 0.15

    # ---------------------------------
    # Start
    # ---------------------------------

    def start(self, position):

        self.x = position[0]
        self.y = position[1]

        self.radius = self.max_radius

        self.life = self.max_life

        self.active = True

    # ---------------------------------
    # Update
    # ---------------------------------

    def update(self, dt):

        if not self.active:
            return

        self.life -= dt

        expired = self.life <= 0

        if expired:

            self.life = 0
            self.active = False
            return

        progress = self.life / self.max_life

        self.radius = self.max_radius * progress

    # ---------------------------------
    # Draw
    # ---------------------------------

    def draw(self, frame):

        if not self.active:
            return

        position = (
            int(self.x),
            int(self.y)
        )
        radius = max(1, int(self.radius))
        glow_radius = max(1, int(self.radius * 1.4))

        color = (
            255,
            255,
            255
        )

        AnimationUtils.impact_flash(
            frame,
            position,
            radius,
            color
        )

        AnimationUtils.glow_circle(
            frame,
            position,
            glow_radius,
            (
                0,
                180,
                255
            )
        )

    # ---------------------------------
    # Reset
    # ---------------------------------

    def reset(self):

        self.active = False

        self.radius = 0

        self.life = 0

    # ---------------------------------
    # Is Active
    # ---------------------------------

    def is_active(self):

        return self.active