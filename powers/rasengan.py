from continuous_animation import ContinuousAnimation
from powers.base_power import BasePower
from powers.rasengan_core import RasenganCore
from powers.rasengan_particles import RasenganParticles
from powers.rasengan_light import RasenganLight
from powers.rasengan_trail import RasenganTrail
from powers.rasengan_distortion import RasenganDistortion
from physics.physics_body import PhysicsBody



class Rasengan(
    BasePower,
    ContinuousAnimation,
    PhysicsBody
):

    def __init__(self):
        BasePower.__init__(self)
        ContinuousAnimation.__init__(self)
        PhysicsBody.__init__(self)

        self.center = (0, 0)
        # -------------------------
        # Physics Settings
        # -------------------------

        self.radius = 30
        self.mass = 1.0
        self.drag = 0.90
        self.max_speed = 900
        self.core = RasenganCore()
        self.particles = RasenganParticles()
        self.light = RasenganLight()
        self.trail = RasenganTrail()
        self.distortion = RasenganDistortion()

    # ----------------------------------
    # Start
    # ----------------------------------

    def start(self, center):

        BasePower.start(self)
        from physics.vector2 import Vector2

        self.position = Vector2(
            center[0],
            center[1]
        )

        self.velocity = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)
        self.center = center

        self.core.reset()
        self.particles.clear()
        self.light.reset()
        self.trail.reset()
        self.distortion.reset()

    # ----------------------------------
    # Stop
    # ----------------------------------

    def stop(self):

        BasePower.stop(self)

        self.particles.clear()

    # ----------------------------------
    # Move
    # ----------------------------------

    def move(self, center):

        from physics.vector2 import Vector2

        target = Vector2(
            center[0],
            center[1]
        )

        direction = target - self.position

        self.velocity = direction * 8

        

    # ----------------------------------
    # Update
    # ----------------------------------

    def update(self, frame, dt):

        if not self.active:
            return
        PhysicsBody.update(self, dt)

        self.center = (
            int(self.position.x),
            int(self.position.y)
        )

        self.core.update(dt)
        self.particles.emit(self.center)
        self.particles.update(dt)
        self.light.update(dt)
        self.trail.update(dt)
        self.distortion.update(dt)

        # Draw order

        self.light.draw(
            frame,
            self.center
        )

        self.distortion.draw(
            frame,
            self.center
        )

        self.trail.draw(
            frame,
            self.center
        )

        self.core.draw(
            frame,
            self.center
        )

        self.particles.draw(
            frame,
            self.center
        )