from continuous_animation import ContinuousAnimation
from powers.base_power import BasePower
from animation_utils import AnimationUtils
from animation_config import AnimationConfig
from effect_renderer import EffectRenderer
import cv2
import math
import random
from particle_pool import ParticlePool


class Shield(BasePower, ContinuousAnimation):

    def __init__(self):
        BasePower.__init__(self)
        ContinuousAnimation.__init__(self)
        self.angle = 0
        self.pulse = 0
        self.rotation = 0
        self.ripple = 0
        self.particle_pool = ParticlePool(150)
        self.particles_list = []

    def start(self, position):

        #print("Shield START called")
        #print("Position:", position)

        BasePower.start(self)
        ContinuousAnimation.start(self, position)

        #print("Shield Active:", self.active)

        self.ripple = 0

    def stop(self):

        BasePower.stop(self)    

    def move(self, position):
        self.position = position    

    def update(self, frame, dt):

        #print("Shield Update - Active:", self.active)

        if not self.active:
            return

        x, y = self.position
        self.rotation += 120 * dt
        self.pulse += 6 * dt
        if self.ripple < 150:
            self.ripple += 120 * dt

        outer_radius = (
            AnimationConfig.SHIELD_RADIUS
            + int(4 * math.sin(self.pulse))
        )

        # Create floating energy particles
        #if random.random() < 0.4:
            #angle = random.uniform(0, 2 * math.pi)
        if random.random() < 0.15:

            particle = self.particle_pool.get()

            if particle:

                particle.angle = random.uniform(0, 2 * math.pi)
                particle.radius = random.randint(40, outer_radius)
                particle.life = 30
                particle.center = (x, y)

                self.particles_list.append(particle)
           

        self.angle = (self.angle + 3) % 360

        

        # Energy aura
        AnimationUtils.shield_ring(
            frame,
            (x, y),
            outer_radius + 12,
            (255, 200, 0)
        )

        # Outer Ring
        

        AnimationUtils.shield_ring(
            frame,
            (x, y),
            outer_radius,
            (255, 255, 0)
        )

        # Inner Ring
        inner_radius = (
            AnimationConfig.SHIELD_RADIUS - 20
            + int(3 * math.sin(self.pulse))
        )
        AnimationUtils.shield_ring(
            frame,
            (x, y),
            inner_radius,
            (0, 255, 255)
        )

        # Rotating Nodes
        AnimationUtils.rotating_nodes(
            frame,
            (x, y),
            outer_radius,
            self.rotation
        )

        # Energy spokes
        AnimationUtils.energy_spokes(
            frame,
            (x, y),
            inner_radius,
            self.rotation,
            (0, 255, 255)
        )

        # Rotating holographic arcs
        AnimationUtils.rotating_arcs(
            frame,
            (x, y),
            outer_radius + 6,
            self.rotation
        )

        # Floating energy particles
        AnimationUtils.floating_particles(
            frame,
            self.particles_list
        )

        self.particles_list = [
            p for p in self.particles_list
            if p.life > 0
        ]

        # # Expanding shield ripple
        # AnimationUtils.shield_ripple(
        #     frame,
        #     (x, y),
        #     int(self.ripple)
        # )            