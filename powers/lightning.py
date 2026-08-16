from continuous_animation import ContinuousAnimation
from powers.base_power import BasePower
from particle_pool import ParticlePool
from animation_utils import AnimationUtils
from effect_renderer import EffectRenderer
from animation_config import AnimationConfig
from powers.lightning_physics import LightningPhysics
from powers.lightning_renderer import LightningRenderer
from powers.lightning_particles import LightningParticles
from powers.lightning_collision import LightningCollision
from powers.lightning_target import LightningTarget
import cv2
import random
import math

class Lightning(BasePower, ContinuousAnimation):

    def __init__(self):
        BasePower.__init__(self)
        ContinuousAnimation.__init__(self)
        self.angle = 0
        self.ball_radius = 0
        self.pulse = 0
        self.orbit_angle = 0
        self.particle_pool = ParticlePool(150)

        self.physics = LightningPhysics()

        self.renderer = LightningRenderer()

        self.particles = LightningParticles()

        self.collision = LightningCollision()

        self.target_system = LightningTarget()

        self.target = None

        self.physics_engine = None

    def set_physics_engine(self, engine):

        self.physics_engine = engine    

    def start(self, position, angle=None):
        BasePower.start(self)
        self.position = position
        self.ball_radius = 0
        self.pulse = 0
        self.orbit_angle = 0

        self.physics.start(
            position,
            angle
        )

        if (
            self.physics_engine
            and self.physics not in self.physics_engine.bodies
        ):
            self.physics_engine.add(self.physics)

        if angle is not None:
            self.angle = angle

        self.renderer.reset()

        if hasattr(self.particles, "clear"):
            self.particles.clear()

    def move(self, position, angle=None):

        self.position = position

        self.physics.start_position.x = position[0]
        self.physics.start_position.y = position[1]

        if angle is not None:

            self.angle = angle

            self.physics.set_angle(angle)
        elif self.physics.target is None:

            self.physics.update_end(self.physics.angle)    

    def set_target(self, position):

        self.target = position

        self.target_system.set_target(
            position
        ) 
        self.physics.set_target(
           position
        )   

    def stop(self):

        BasePower.stop(self)

        self.physics.destroy()

        self.target_system.clear()

        if hasattr(self.particles, "clear"):
            self.particles.clear()

        self.renderer.reset() 

    def update_physics(self, dt):

        if self.physics_engine is None:
            self.physics.update(dt)

        self.target_system.update(self.physics)

        if self.physics.is_finished():

            self.stop()

            return False

        if self.collision.hit_target(self.physics):

            self.stop()

            return False

        if self.target_system.reached(self.physics):

            self.stop()

            return False

        return True 

    def update_particles(self, dt):

        if hasattr(self.particles, "update"):
            self.particles.update(dt)

        x = int(self.physics.start_position.x)
        y = int(self.physics.start_position.y)

        if (
            random.random() < 0.15
            and hasattr(self.particles, "emit")
        ):

            self.particles.emit(
                (
                    x,
                    y
                ),
                count=2
            ) 

    def render(self, frame):

        x = int(self.physics.start_position.x)
        y = int(self.physics.start_position.y)

        ball_radius = int(self.ball_radius)

        EffectRenderer.lightning_charge(
            frame,
            (x, y),
            ball_radius
        )
        if self.physics.length > 0:
            self.renderer.draw(
                frame,
                self.physics.get_start_position(),
                self.physics.get_end_position(),
                self.physics.get_intensity()
            )
        

        if hasattr(self.particles, "draw"):
            self.particles.draw(frame)

    def update(self, frame, dt):

        if not self.active:
            return

        self.pulse += 8 * dt

        self.orbit_angle += 4 * dt

        self.renderer.update(dt)

        if not self.update_physics(dt):
            return

        self.update_particles(dt)

        if self.ball_radius < AnimationConfig.LIGHTNING_RADIUS:

            self.ball_radius += 60 * dt

            if self.ball_radius > AnimationConfig.LIGHTNING_RADIUS:

                self.ball_radius = AnimationConfig.LIGHTNING_RADIUS

        self.render(frame)