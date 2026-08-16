import cv2
from animation_utils import AnimationUtils


class ExplosionShockwave:

    def __init__(self):

        self.active = False

        self.x = 0
        self.y = 0

        self.radius = 0

        self.max_radius = 160

        self.speed = 700.0

        self.alpha = 1.0

    # ---------------------------------
    # Start
    # ---------------------------------

    def start(
        self,
        position
    ):

        self.x = position[0]
        self.y = position[1]

        self.radius = 10

        self.alpha = 1.0

        self.active = True

    # ---------------------------------
    # Update
    # ---------------------------------

    def update(
        self,
        dt
    ):

        if not self.active:
            return

        self.radius += self.speed * dt

        self.alpha = max(
            0.0,
            1.0 - self.radius / self.max_radius
        )

        finished = self.radius >= self.max_radius

        if finished:
            self.active = False

    # ---------------------------------
    # Draw
    # ---------------------------------

    def draw(
        self,
        frame
    ):

        if not self.active:
            return

        position = (
            int(self.x),
            int(self.y)
        )
        radius = int(self.radius)

        color = (
            255,
            int(220 * self.alpha),
            80
        )

        thickness = max(1, int(6 * self.alpha))

        cv2.circle(
            frame,
            position,
            radius,
            color,
            thickness,
            cv2.LINE_AA
        )

        AnimationUtils.glow_circle(
            frame,
            position,
            radius,
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

        self.alpha = 1.0

    # ---------------------------------
    # Is Active
    # ---------------------------------

    def is_active(self):

        return self.active