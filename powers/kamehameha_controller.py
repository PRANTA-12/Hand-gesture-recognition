from powers.kamehameha_core import KamehamehaCore
from powers.kamehameha_beam import KamehamehaBeam
from powers.kamehameha_particles import KamehamehaParticles
from powers.kamehameha_light import KamehamehaLight
from powers.kamehameha_distortion import KamehamehaDistortion


class KamehamehaController:

    def __init__(self):

        self.core = KamehamehaCore()
        self.beam = KamehamehaBeam()
        self.particles = KamehamehaParticles()
        self.light = KamehamehaLight()
        self.distortion = KamehamehaDistortion()

        self.active = False
        self.angle = 0
        self.center = (0, 0)

    # -------------------------
    # Start
    # -------------------------

    def start(
        self,
        center,
        angle
    ):

        self.active = True

        self.center = center
        self.angle = angle

        self.beam.reset()
        self.particles.clear()

    # -------------------------
    # Stop
    # -------------------------

    def stop(self):

        self.active = False

        self.particles.clear()

        self.beam.reset()

    # -------------------------
    # Move
    # -------------------------

    def move(
        self,
        center
    ):

        self.center = center

    # -------------------------
    # Rotate
    # -------------------------

    def rotate(
        self,
        angle
    ):

        self.angle = angle

    # -------------------------
    # Update
    # -------------------------

    def update(
        self,
        frame,
        dt
    ):

        if not self.active:
            return

        self.core.update(dt)
        self.beam.update(dt)
        self.light.update(dt)
        self.distortion.update(dt)

        self.particles.emit(
            self.center,
            self.angle,
            self.beam.length
        )

        self.particles.update(dt)

        # -------------------------
        # Draw Order
        # -------------------------

        self.light.draw(
            frame,
            self.center,
            self.angle,
            self.beam.length
        )

        self.distortion.draw(
            frame,
            self.center,
            self.angle,
            self.beam.length
        )

        self.beam.draw(
            frame,
            self.center,
            self.angle
        )

        self.core.draw(
            frame,
            self.center,
            30
        )

        self.particles.draw(frame)