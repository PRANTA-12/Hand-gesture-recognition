import math

from animation_utils import AnimationUtils
from effect_renderer import EffectRenderer
from animation_config import AnimationConfig


class FireballRenderer:

    def __init__(self):

        self.pulse = 0.0

    # ---------------------------------
    # Reset
    # ---------------------------------

    def reset(self):

        self.pulse = 0.0

    # ---------------------------------
    # Update Animation
    # ---------------------------------

    def update(self, dt):

        self.pulse += 18 * dt

        if self.pulse > math.pi * 2:
            self.pulse = 0.0

    # ---------------------------------
    # Draw
    # ---------------------------------

    def draw(
        self,
        frame,
        center,
        trail=None,
        flames=None,
        sparks=None
    ):

        x, y = center
        center_pos = (x, y)

        # -------------------------
        # Draw Trail
        # -------------------------

        if trail is not None:
            trail.draw(frame)

        # -------------------------
        # Flame Particles
        # -------------------------

        if flames is not None:
            flames.draw(frame)

        # -------------------------
        # Fire Sparks
        # -------------------------

        if sparks is not None:
            sparks.draw(frame)

        # -------------------------
        # Animated Radius
        # -------------------------

        pulse_sin = math.sin(self.pulse)

        radius = int(
            AnimationConfig.FIREBALL_RADIUS +
            3 * pulse_sin
        )

        glow_radius = radius + int(
            8 +
            2 * pulse_sin
        )
        # -------------------------
        # Dynamic Light
        # -------------------------

        AnimationUtils.dynamic_light(

            frame,

           center_pos,
           
            radius=120,

            color=(0, 120, 255),

            alpha=0.25

        )

        # -------------------------
        # Outer Glow
        # -------------------------

        AnimationUtils.glow_circle(

            frame,

            center_pos,

            glow_radius + 8,

            (0, 80, 255)

        )

        AnimationUtils.glow_circle(

            frame,

            center_pos,

            glow_radius,

            (0, 120, 255)

        )

        # -------------------------
        # Fireball Core
        # -------------------------

        EffectRenderer.fireball(

            frame,

            center_pos,

            radius

        )

        # -------------------------
        # Orbiting Energy
        # -------------------------

        orbit_radius = radius + 10

        quarter_turn = math.pi / 2
        base_angle = self.pulse * 2

        for i in range(4):

            angle = base_angle + i * quarter_turn

            cos_angle = math.cos(angle)
            sin_angle = math.sin(angle)

            px = int(
                x + orbit_radius * cos_angle
            )

            py = int(
                y + orbit_radius * sin_angle
            )

            orbit_pos = (px, py)

            AnimationUtils.glow_circle(

                frame,

                orbit_pos,

                4,

                (0, 200, 255)

            )

            AnimationUtils.glow_circle(

                frame,

                orbit_pos,

                2,

                (255, 255, 255)

            )