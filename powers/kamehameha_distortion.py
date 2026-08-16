import math

from animation_utils import AnimationUtils


class KamehamehaDistortion:

    def __init__(self):

        self.wave = 0

    def update(self, dt):

        self.wave += 10 * dt

    def draw(
        self,
        frame,
        center,
        angle,
        beam_length
    ):

        cx, cy = center

        # Draw heat waves along the beam
        for d in range(0, int(beam_length), 18):

            offset = math.sin(
                self.wave + d * 0.08
            ) * 8

            px = (
                cx
                + math.cos(angle) * d
                + math.cos(angle + math.pi / 2) * offset
            )

            py = (
                cy
                + math.sin(angle) * d
                + math.sin(angle + math.pi / 2) * offset
            )

            AnimationUtils.glow_circle(
                frame,
                (
                    int(px),
                    int(py)
                ),
                5,
                (255, 220, 180)
            )

        # Second moving distortion layer
        for d in range(0, int(beam_length), 30):

            offset = math.sin(
                self.wave * 1.5 + d * 0.12
            ) * 12

            px = (
                cx
                + math.cos(angle) * d
                - math.cos(angle + math.pi / 2) * offset
            )

            py = (
                cy
                + math.sin(angle) * d
                - math.sin(angle + math.pi / 2) * offset
            )

            AnimationUtils.glow_circle(
                frame,
                (
                    int(px),
                    int(py)
                ),
                3,
                (255, 255, 255)
            )

        # Strong distortion around the charging core
        AnimationUtils.glow_circle(
            frame,
            (cx, cy),
            45 + int(4 * math.sin(self.wave)),
            (255, 240, 200)
        )
        