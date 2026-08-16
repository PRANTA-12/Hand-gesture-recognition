import math

from continuous_animation import ContinuousAnimation
from powers.base_power import BasePower
from powers.kamehameha_controller import KamehamehaController


class Kamehameha(BasePower, ContinuousAnimation):

    def __init__(self):

        BasePower.__init__(self)
        ContinuousAnimation.__init__(self)

        self.controller = KamehamehaController()

        self.center = (0, 0)
        self.angle = 0

    # ---------------------------------
    # Start Animation
    # ---------------------------------

    def start(
        self,
        center,
        angle=0
    ):

        BasePower.start(self)

        self.center = center
        self.angle = angle

        self.controller.start(
            center,
            angle
        )

    # ---------------------------------
    # Stop Animation
    # ---------------------------------

    def stop(self):

        BasePower.stop(self)

        self.controller.stop()

    # ---------------------------------
    # Move Animation
    # ---------------------------------

    def move(
        self,
        center
    ):

        self.center = center

        self.controller.move(center)

    # ---------------------------------
    # Rotate Beam
    # ---------------------------------

    def rotate(
        self,
        angle
    ):

        self.angle = angle

        self.controller.rotate(angle)

    # ---------------------------------
    # Update Animation
    # ---------------------------------

    def update(
        self,
        frame,
        dt
    ):

        if not self.active:
            return

        self.controller.update(
            frame,
            dt
        )