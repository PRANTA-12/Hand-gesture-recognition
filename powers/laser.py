from continuous_animation import ContinuousAnimation
from powers.base_power import BasePower
from animation_utils import AnimationUtils
from animation_config import AnimationConfig
import cv2
import math


class Laser(BasePower, ContinuousAnimation):

    def __init__(self):
        BasePower.__init__(self)
        ContinuousAnimation.__init__(self)
        self.length = AnimationConfig.LASER_LENGTH
        self.angle = 0

    def start(self, position, angle):
        BasePower.start(self)
        ContinuousAnimation.start(self, position)
        self.angle = angle

    def stop(self):

        BasePower.stop(self)    

    def move(self, position):
        self.position = position    

    def update(self, frame, dt):

        if not self.active:
            return

        x, y = self.position

        endX = int(x + self.length * math.cos(self.angle))
        endY = int(y + self.length * math.sin(self.angle))

        end = (endX, endY)

        AnimationUtils.laser_beam(
            frame,
            (x, y),
            end
        )

        # Laser source
        AnimationUtils.glow_circle(
            frame,
            (x, y),
            8,
            (255, 255, 255)
        )