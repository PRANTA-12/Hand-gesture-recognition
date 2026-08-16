from animation_utils import AnimationUtils
import cv2
import random
import math
from powers.explosion_physics import ExplosionPhysics
from powers.explosion_renderer import ExplosionRenderer
from powers.explosion_particles import ExplosionParticles
from powers.explosion_shockwave import ExplosionShockwave
from powers.explosion_flash import ExplosionFlash
from powers.explosion_light import ExplosionLight
from powers.explosion_smoke_particles import ExplosionSmokeParticles
from powers.explosion_debris import ExplosionDebris
from powers.explosion_embers import ExplosionEmbers
from powers.explosion_fire_rings import ExplosionFireRings


class Explosion:

    def __init__(self):

        self.active = False
        self.physics = ExplosionPhysics()
        self.physics_engine = None

        self.renderer = ExplosionRenderer()

        self.particles = ExplosionParticles()

        self.shockwave = ExplosionShockwave()
        self.flash = ExplosionFlash()

        self.light = ExplosionLight()

        self.smoke = ExplosionSmokeParticles()

        self.debris = ExplosionDebris()

        self.embers = ExplosionEmbers()

        self.fire_rings = ExplosionFireRings()
    

    def set_physics_engine(self, physics_engine):

        self.physics_engine = physics_engine

        physics_engine.add(self.physics)    

    def trigger(self, center):
        #print("Explosion trigger called")
        self.active = True
        self.physics.start(center)

        self.renderer.reset()

        self.particles.clear()

        self.particles.emit(center)

        self.shockwave.start(center)

        self.flash.start(center)

        self.light.start(center)

        for effect in (
            self.smoke,
            self.debris,
            self.embers,
            self.fire_rings,
        ):
            effect.clear()
            effect.emit(center)

    def update(self, frame, dt):

        physics = self.physics

        physics.update(dt)

        if physics.is_finished():

            self.active = False
            return

        self.particles.update(dt)

        self.shockwave.update(dt)
        self.flash.update(dt)

        self.light.update(dt)

        self.smoke.update(dt)

        self.debris.update(dt)

        self.embers.update(dt)

        self.fire_rings.update(dt)

        self.renderer.update(dt)

        center = (
            int(physics.position.x),
            int(physics.position.y)
        )

        self.renderer.draw(
            frame,
            center,
            self.particles,
            self.shockwave,
            self.flash,
            self.light,
            self.smoke,
            self.debris,
            self.embers,
            self.fire_rings
        )

    def stop(self):

        self.active = False

        self.physics.destroy()

        self.particles.clear()

        self.smoke.clear()

        self.debris.clear()

        self.embers.clear()

        self.fire_rings.clear()
        