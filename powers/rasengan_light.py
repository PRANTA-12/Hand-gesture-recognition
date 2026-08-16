import math

from animation_utils import AnimationUtils


class RasenganLight:

    def __init__(self):

        self.pulse = 0

    def update(self, dt):

        self.pulse += 8 * dt

    def draw(self, frame, center):

        cx, cy = center

        # Pulsing light radius
        radius = 90 + int(
            15 * math.sin(self.pulse)
        )

        # Outer lighting
        AnimationUtils.dynamic_light(
            frame,
            (cx, cy),
            radius,
            (255, 120, 0),
            0.18
        )

        # Middle lighting
        AnimationUtils.dynamic_light(
            frame,
            (cx, cy),
            radius - 25,
            (255, 180, 80),
            0.25
        )

        # Inner lighting
        AnimationUtils.dynamic_light(
            frame,
            (cx, cy),
            radius - 45,
            (255, 255, 255),
            0.35
        )

        # Core glow
        AnimationUtils.glow_circle(
            frame,
            (cx, cy),
            18,
            (255, 255, 255)
        )

    def reset(self):

        self.pulse = 0