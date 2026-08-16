import math

from animation_utils import AnimationUtils


class KamehamehaLight:

    def __init__(self):

        self.pulse = 0

    def update(self, dt):

        self.pulse += 8 * dt

    def draw(
        self,
        frame,
        center,
        angle,
        beam_length
    ):

        cx, cy = center

        glow = int(
            140 +
            20 * math.sin(self.pulse)
        )

        # ==========================
        # Hand Light
        # ==========================

        AnimationUtils.dynamic_light(
            frame,
            (cx, cy),
            radius=glow,
            color=(255, 180, 80),
            alpha=0.30
        )

        # ==========================
        # Beam Light
        # ==========================

        for i in range(0, int(beam_length), 60):

            x = int(
                cx +
                math.cos(angle) * i
            )

            y = int(
                cy +
                math.sin(angle) * i
            )

            AnimationUtils.dynamic_light(
                frame,
                (x, y),
                radius=70,
                color=(255, 180, 100),
                alpha=0.10
            )

        # ==========================
        # Impact Light
        # ==========================

        end_x = int(
            cx +
            math.cos(angle) * beam_length
        )

        end_y = int(
            cy +
            math.sin(angle) * beam_length
        )

        AnimationUtils.dynamic_light(
            frame,
            (
                end_x,
                end_y
            ),
            radius=120,
            color=(255, 220, 180),
            alpha=0.25
        )