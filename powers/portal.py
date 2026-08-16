import math
import random
import cv2

from continuous_animation import ContinuousAnimation
from powers.base_power import BasePower
from animation_utils import AnimationUtils
from powers.portal_runes import PortalRunes
from powers.portal_vortex import PortalVortex
from powers.portal_sparks import PortalSparks
from powers.portal_smoke import PortalSmoke
from powers.portal_flash import PortalFlash
from powers.portal_close import PortalClose
from powers.portal_galaxy import PortalGalaxy
from powers.portal_rays import PortalRays
from powers.camera_shake import CameraShake
from powers.portal_edge_fire import PortalEdgeFire
from powers.portal_distortion import PortalDistortion
from powers.portal_particles import PortalParticles
from powers.portal_lightning import PortalLightning
from powers.sound_manager import SoundManager
from powers.portal_state import PortalStateMachine
from powers.animation_manager import AnimationManager
from powers.portal_collision import PortalCollision
from powers.portal_teleport import PortalTeleport
from powers.portal_exit import PortalExit

class Portal(BasePower, ContinuousAnimation):
    def __init__(self):

        BasePower.__init__(self)
        ContinuousAnimation.__init__(self)

    
        self.center = (0, 0)

        self.outer_rotation = 0
        self.inner_rotation = 0

        self.radius = 100
        self.current_radius = 0
        self.target_radius = 100

        self.MAX_PARTICLES = 250
        self.MAX_SMOKE = 120
        self.MAX_SPARKS = 80
        self.MAX_LIGHTNING = 20

        self.state = PortalStateMachine()
        self.close = PortalClose()
        self.particles = PortalParticles()
        self.runes = PortalRunes()
        self.vortex = PortalVortex()
        self.lightning = PortalLightning()
        self.sparks = PortalSparks()
        self.smoke = PortalSmoke()
        self.flash = PortalFlash()
        self.distortion = PortalDistortion()
        self.galaxy = PortalGalaxy()
        self.rays = PortalRays()
        self.edge_fire = PortalEdgeFire()
        self.camera_shake = CameraShake()
        self.sound = SoundManager()
        self.animations = AnimationManager()
        self.collision = PortalCollision()
        self.teleport = PortalTeleport()
        self.exit_effect = PortalExit()

        self.animations.register(
            self.particles,
            max_count=self.MAX_PARTICLES,
            particle_attr="particles"
        )
        self.animations.register(self.flash)
        self.animations.register(self.distortion)
        self.animations.register(self.galaxy)
        self.animations.register(self.rays)
        self.animations.register(self.edge_fire)
        self.animations.register(self.vortex)
        self.animations.register(self.runes)
        self.animations.register(self.exit_effect)
        self.animations.register(
            self.smoke,
            max_count=self.MAX_SMOKE,
            particle_attr="particles"
        )

        self.animations.register(
            self.lightning,
            max_count=self.MAX_LIGHTNING,
            particle_attr="arcs"
        )

        self.animations.register(
            self.sparks,
            max_count=self.MAX_SPARKS,
            particle_attr="sparks"
        )

    def start(self, center):

        BasePower.start(self)
        self.state.start()

        self.center = center
        self.active = True
        self.animations.reset()
        self.sound.play_open()
        self.sound.play_loop()
        self.camera_shake.start(
            intensity=10,
            duration=0.30
        )
        self.current_radius = 0

        self.animations.clear()
        self.animations.reset()

        self.teleport.reset()
        self.teleport.update(
            self.center,
            self.current_radius
        )

    def stop(self):
        if self.state.is_opening() or self.state.is_active():
            
            BasePower.stop(self)
            self.state.close()
            self.close.start(self.current_radius)
            self.exit_effect.start(
                self.center,
                self.current_radius
            )
            self.sound.play_close()
            self.sound.stop_loop()
            self.camera_shake.start(
                intensity=5,
                duration=0.20
            )

    def move(self, center):

        self.center = center

    def update(self, frame, dt):

        if not self.active:
            return

        if self.state.is_idle():
            return

        cx, cy = self.center
        h, w = frame.shape[:2]

        if (
            cx < -200 or cx > w + 200 or
            cy < -200 or cy > h + 200
        ):
            return
        
        self.camera_shake.update(dt)
        if self.state.is_closing():

            self.close.update(dt)

            self.current_radius = self.close.get_radius()

            if self.close.is_finished():

                self.state.reset()

                self.animations.clear()

                return

        # Opening animation
        if self.state.is_opening() and self.current_radius < self.target_radius:

            self.current_radius += 180 * dt

            if self.current_radius > self.target_radius:
                self.current_radius = self.target_radius

        self.current_radius = max(45, self.current_radius)
        if (
            self.state.is_opening()
            and self.current_radius >= self.target_radius
        ):
            self.state.activate()       

        self.outer_rotation += 60 * dt
        self.inner_rotation -= 90 * dt

        self.teleport.update(
            self.center,
            self.current_radius
        )

       
        if not self.state.is_closing():

            self.animations.emit(
                self.center,
                self.current_radius
            )

        self.animations.update(dt)

        self.animations.draw(
            frame,
            self.center,
            self.current_radius
        )

        self.collision.update(
            self.center,
            self.current_radius
        )

        # -----------------------
        # Outer Portal Ring
        # -----------------------

        AnimationUtils.rotating_arcs(

            frame,

            (cx, cy),

            max(45, self.current_radius),

            self.outer_rotation

        )

        # -----------------------
        # Inner Ring
        # -----------------------

        AnimationUtils.rotating_arcs(

            frame,

            (cx, cy),

            max(45, self.current_radius - 25),

            self.inner_rotation

        )

        # -----------------------
        # Energy Aura
        # -----------------------

        AnimationUtils.glow_circle(

            frame,

            (cx, cy),

            self.current_radius + 25,

            (0, 120, 255)

        )

        # -----------------------
        # Portal Core
        # -----------------------

        AnimationUtils.glow_circle(

            frame,

            (cx, cy),

            35,

            (255, 255, 255)

        )
        shaken = self.camera_shake.apply(frame)
        frame[:] = shaken
        