import math

from animation_utils import AnimationUtils
from effect_renderer import EffectRenderer


class ExplosionRenderer:

    def __init__(self):

        self.pulse = 0.0

    # ---------------------------------
    # Reset
    # ---------------------------------

    def reset(self):

        self.pulse = 0.0

    # ---------------------------------
    # Update
    # ---------------------------------

    def update(self, dt):

        self.pulse += 8 * dt

        if self.pulse > math.pi * 2:

            self.pulse = 0.0

    # ---------------------------------
    # Draw
    # ---------------------------------

    def draw(
        self,
        frame,
        center,
    particles=None,
    shockwave=None,
    flash=None,
    light=None,
    smoke=None,
    debris=None,
    embers=None,
    fire_rings=None
    ):

        x, y = center
        center_pos = (x, y)
        # -------------------------
        # Draw Dynamic Light
        # -------------------------

        if light is not None:
            light.draw(frame)

        # -------------------------
        # Draw Flash
        # -------------------------

        if flash is not None:
            flash.draw(frame)

        # -------------------------
        # Draw Shockwave
        # -------------------------

        if shockwave is not None:
            shockwave.draw(frame)

        # -------------------------
        # Draw Smoke
        # -------------------------

        if smoke is not None:
            smoke.draw(frame)

        # -------------------------
        # Draw Fire Rings
        # -------------------------

        if fire_rings is not None:
            fire_rings.draw(frame)

        # -------------------------
        # Draw Debris
        # -------------------------

        if debris is not None:
            debris.draw(frame)

        # -------------------------
        # Draw Embers
        # -------------------------

        if embers is not None:
            embers.draw(frame)

        # -------------------------
        # Draw Explosion Particles
        # -------------------------

        if particles is not None:
            particles.draw(frame)
        radius = int(

            28 +

            8 * math.sin(self.pulse)

        )

       

        
        # -------------------------
        # Outer Glow
        # -------------------------

        AnimationUtils.glow_circle(
            frame,
            center_pos,
            radius + 24,
            (0, 120, 255)
        )

        AnimationUtils.glow_circle(
            frame,
            center_pos,
            radius + 12,
            (0, 180, 255)
        )

        # -------------------------
        # Explosion Core
        # -------------------------

        EffectRenderer.fireball(
            frame,
            center_pos,
            radius
        )

        # -------------------------
        # Energy Ring
        # -------------------------

        orbit = radius + 18

        for i in range(8):

            angle = (

                self.pulse +

                i *

                (math.pi / 4)

            )

            px = int(

                x +

                orbit *

                math.cos(angle)

            )

            py = int(

                y +

                orbit *

                math.sin(angle)

            )

            AnimationUtils.glow_circle(

                frame,

                (px, py),

                3,

                (255, 255, 255)

            )

            AnimationUtils.glow_circle(

                frame,

                (px, py),

                5,

                (0, 180, 255)

            )

        # -------------------------
        # Flash
        # -------------------------

        