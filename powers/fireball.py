from animation import Animation
from collision import CollisionManager
from powers.base_power import BasePower
from animation_utils import AnimationUtils
from trail_manager import TrailManager
from effect_renderer import EffectRenderer
from animation_config import AnimationConfig
from powers.flame_particles import FlameParticles
from powers.fire_sparks import FireSparks
from powers.fireball_physics import FireballPhysics
from powers.fireball_collision import FireballCollision
from powers.fireball_renderer import FireballRenderer
from powers.fireball_target import FireballTarget
from powers.smoke_particles import SmokeParticles
import cv2
import math
import random

class Fireball(BasePower, Animation):

    def __init__(self):
        BasePower.__init__(self)
        Animation.__init__(self, duration=1.0)
        self.angle = 0


        # Current position
        self.x = 0
        self.y = 0

        # Velocity

        self.speed = AnimationConfig.FIREBALL_SPEED

        self.vx = 0
        self.vy = 0
        self.pulse = 0
        self.orbit = 0

        # Fire trail
        self.trail = TrailManager(AnimationConfig.FIREBALL_TRAIL)
        self.on_explode = None
        self.smoke = SmokeParticles()

        self.physics = FireballPhysics()
        self.physics_engine = None

        self.distance = 0
        from config import FIREBALL_MAX_DISTANCE

        self.max_distance = FIREBALL_MAX_DISTANCE
        self.exploded = False
        self.target = None

        self.collision = CollisionManager()
        self.flames = FlameParticles()
        self.sparks = FireSparks()
        self.renderer = FireballRenderer()
        self.target_system = FireballTarget()
        self.collision_system = FireballCollision()

    def start(self, position,angle):
        BasePower.start(self)
        Animation.start(self, position)
        self.angle = angle

        self.physics.start(
            position,
            angle,
            self.speed
        )

       

        self.x = position[0]
        self.y = position[1]

        self.trail.clear()
        self.flames.clear()
        self.sparks.clear()
        self.smoke.clear()

        self.distance = 0
        self.exploded = False
        self.target = None

        self.target_system.clear()
        self.renderer.reset()

    def stop(self):

        BasePower.stop(self)

        self.physics.destroy()

        self.target_system.clear()
        self.smoke.clear()
        self.trail.clear()
        self.flames.clear()
        self.sparks.clear() 

    def set_physics_engine(self, engine):

        self.physics_engine = engine       

    def set_target(self, position):

        self.target = position

        self.target_system.set_target(
            position
        )    

    def update(self, frame, dt):

        if not Animation.update(self):
            BasePower.stop(self)
            return

        BasePower.update(self)

        if not self.active or self.paused:
            return

        if self.state == "CHARGE":

            self.x = self.position[0]
            self.y = self.position[1]

            self.renderer.update(dt)

            self.renderer.draw(
                frame,
                (
                    int(self.x),
                    int(self.y)
                )
            )

            return

        
        self.pulse += 18 * dt
        wave = 2 * math.sin(self.pulse * 2)

        # Move fireball
        if self.state != "TRAVEL":
            return

        height, width = frame.shape[:2]

        physics = self.physics

        self.target_system.update(physics)

        physics.update(dt)

        self.x = physics.position.x
        self.y = physics.position.y

        self.distance = physics.distance

        position = (int(self.x), int(self.y))

        self.flames.emit(position)
        self.sparks.emit(position)

        if hasattr(self, "particles"):
            self.particles.emit(
                position,
                color=(0, 140, 255),
                count=3,
                speed=1.5
            )

        self.trail.add(position)
        
        # Create smoke
        self.smoke.emit(position)


        # Update smoke particles
        self.smoke.update(dt)

        self.smoke.draw(frame)   
    
        # Draw trail
        self.sparks.update(dt)
        self.flames.update(dt)

        self.renderer.update(dt)

        self.renderer.draw(
            frame,
            position,
            self.trail,
            self.flames,
            self.sparks
        )

        # Fireball
        on_explode = self.on_explode

        # Remove when off-screen
        screen_hit = self.collision_system.check_screen(
            (self.x, self.y),
            width,
            height
        )

        if screen_hit and not self.exploded:

            self.exploded = True

            if on_explode:
                on_explode(position)

            BasePower.stop(self)
            return
        # Explode when reaching target
        if (
            self.target_system.reached(
                self.physics
            )
            and not self.exploded
        ):

                self.exploded = True

                if on_explode:
                    on_explode(position)

                BasePower.stop(self)
                return

        # Explode only once
        if (
            self.physics.reached_limit()
            and not self.exploded
        ):

            self.exploded = True

            #print(f"Explosion Position: ({self.x:.1f}, {self.y:.1f})")

            if on_explode:
                on_explode(position)

            BasePower.stop(self)
            return   