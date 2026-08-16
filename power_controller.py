from gesture_state import GestureState
from powers.power_priority import PowerPriority
import math
from config import *

class PowerController:

    def __init__(
        self,
        power_manager,
        animation_manager,
        shield,
        fireball,
        explosion,
        lightning,
        ice,
        spider_web,
        cooldown,
        energy,
        camera_zoom,
        camera_shake,
        screen_flash,
        target_lock,
        sound_manager=None,
    ):
        self.power_manager = power_manager
        self.animation_manager = animation_manager
        self.shield = shield
        self.fireball = fireball
        self.explosion = explosion
        self.lightning = lightning
        self.ice = ice
        self.spider_web = spider_web

        self.cooldown = cooldown
        self.energy = energy

        self.camera_zoom = camera_zoom
        self.camera_shake = camera_shake
        self.screen_flash = screen_flash
        self.target_lock = target_lock

        # Step 91/93 — sound_manager is optional so this class still
        # works if nothing passes one in (backwards compatible)
        self.sound_manager = sound_manager

        self.priority = PowerPriority()
        self.current_action = None

    def stop_all(self):

        self.priority.reset()

        self.power_manager.stop_all()

        self.animation_manager.stop_all()

        if self.fireball.active:
            self.fireball.stop()

        if self.shield.active:
            self.shield.stop()

        self.current_action = None

    def switch_power(self, new_action):

        if self.current_action == new_action:
            return

        # Stop previous power
        self.stop_all()

        # Remember new power
        self.current_action = new_action

        # Activate new power
        if new_action:
            self.power_manager.activate(new_action)        

    
    def update(
        self,
        frame,
        action,
        handData
    ):
        
        if handData is None:
            return

        gesture_state = handData["state"]
        if gesture_state != GestureState.CONFIRMED:
            return

        self.priority.update(action)

        lmList = handData["hand"]

        smoothX = handData["smoothX"]

        smoothY = handData["smoothY"]

        handAngle = handData["handAngle"]

        # ==========================
        # SHIELD
        # ==========================

        if action == "SHIELD":

            self.switch_power("SHIELD")

            # Always move the shield every frame
            self.shield.move((smoothX, smoothY))

            # Only spend energy when the gesture is confirmed
            if gesture_state == GestureState.CONFIRMED:

                if not self.shield.active:

                    if self.energy.use(SHIELD_ENERGY):

                        self.shield.start((smoothX, smoothY))

                        if self.sound_manager:
                            self.sound_manager.play_shield()

        else:

            if self.shield.active:
                self.shield.stop()

        # ==========================
        # LASER
        # ==========================

        if action == "LASER":

            self.switch_power("LASER")


            indexX = lmList[8][1]
            indexY = lmList[8][2]
            if gesture_state == GestureState.CONFIRMED:

                # Start only once
                if not self.animation_manager.is_active("LASER"):

                    if self.energy.use(LASER_ENERGY):

                        self.animation_manager.play(
                            "LASER",
                            (indexX, indexY),
                            handAngle
                        )

                else:
                    # Already active → only move/update
                    self.animation_manager.play(
                        "LASER",
                        (indexX, indexY),
                        handAngle
                    )
            else:

                if self.animation_manager.is_active("LASER"):

                    self.animation_manager.stop("LASER")        
 

        # ==========================
        # FIREBALL
        # ==========================

        if action == "FIREBALL":

            self.switch_power("FIREBALL")

            if (
                gesture_state == GestureState.CONFIRMED
                and self.cooldown.ready("THUMBS_UP")
                and self.energy.use(FIREBALL_ENERGY)
            ):

                self.cooldown.trigger("THUMBS_UP")

                if self.target_lock.locked:

                    dx = self.target_lock.x - smoothX
                    dy = self.target_lock.y - smoothY

                    fireAngle = math.atan2(dy, dx)

                else:

                    fireAngle = handAngle


                self.fireball.start(
                    (smoothX, smoothY),
                    fireAngle
                )
                if self.target_lock.locked:
                    self.fireball.set_target(
                        (
                            self.target_lock.x,
                            self.target_lock.y
                        )
                    )

                self.camera_zoom.trigger(1.18)

                if self.sound_manager:
                    self.sound_manager.play_fireball()
        else:

            if self.fireball.active:
                self.fireball.stop()        
        # ==========================
        # LIGHTNING
        # ==========================

        if action == "LIGHTNING":

            self.switch_power("LIGHTNING")

            if gesture_state == GestureState.CONFIRMED:

                # Start only once
                if not self.animation_manager.is_active("LIGHTNING"):

                    if self.energy.use(LIGHTNING_ENERGY):

                        self.animation_manager.play(
                            "LIGHTNING",
                            (smoothX, smoothY),
                            handAngle
                        )

                        if self.sound_manager:
                            self.sound_manager.play_lightning()

                else:

                    # Already active → don't spend energy again
                    self.animation_manager.play(
                        "LIGHTNING",
                        (smoothX, smoothY),
                        handAngle
                    )

            else:

                if self.animation_manager.is_active("LIGHTNING"):

                    self.animation_manager.stop("LIGHTNING")
        # ==========================
        # SPIDER
        # ==========================

        if action == "SPIDER":

            self.switch_power("SPIDER")

            if gesture_state == GestureState.CONFIRMED:

                # Start only once
                if not self.animation_manager.is_active("SPIDER"):

                    if self.energy.use(SPIDER_ENERGY):

                        self.animation_manager.play(
                            "SPIDER",
                            (smoothX, smoothY),
                            handAngle
                        )

                        if self.sound_manager:
                            self.sound_manager.play_sparks()

                else:

                    # Already active → only update
                    self.animation_manager.play(
                        "SPIDER",
                        (smoothX, smoothY),
                        handAngle
                    )

            else:

                if self.animation_manager.is_active("SPIDER"):

                    self.animation_manager.stop("SPIDER")      
        # ==========================
        # ICE
        # ==========================

        if action == "ICE":

            self.switch_power("ICE")

            if gesture_state == GestureState.CONFIRMED:

                # Start only once
                if not self.animation_manager.is_active("ICE"):

                    if self.energy.use(ICE_ENERGY):

                        self.animation_manager.play(
                            "ICE",
                            (smoothX, smoothY),
                            handAngle
                        )

                else:

                    # Already active → only update position
                    self.animation_manager.play(
                        "ICE",
                        (smoothX, smoothY),
                        handAngle
                    )

            else:

                if self.animation_manager.is_active("ICE"):

                    self.animation_manager.stop("ICE")     
        # ==========================
        # EXPLOSION
        # ==========================

        if (
            action == "EXPLOSION"
            and gesture_state == GestureState.CONFIRMED
            and self.cooldown.ready("FIST")
            and self.energy.use(EXPLOSION_ENERGY)
        ):

            self.cooldown.trigger("FIST")

            self.explosion.trigger((smoothX, smoothY))

            self.camera_shake.trigger()

            self.screen_flash.trigger()  

            if self.sound_manager:
                self.sound_manager.play_explosion()

        # else:

        #     self.explosion.stop()
    def reset(self):

        self.stop_all()
