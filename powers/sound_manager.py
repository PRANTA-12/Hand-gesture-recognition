import os
import pygame


class SoundManager:

    def __init__(self):

        self.enabled = False

        try:

            pygame.mixer.init()

            self.enabled = True

        except Exception:

            print("[Sound] Audio initialization failed.")
            return

        self.open_sound = self.load("assets/sounds/portal_open.wav")
        self.close_sound = self.load("assets/sounds/portal_close.wav")
        self.loop_sound = self.load("assets/sounds/portal_loop.wav")
        self.lightning_sound = self.load("assets/sounds/lightning.wav")
        self.spark_sound = self.load("assets/sounds/sparks.wav")

        # Added for Step 91 (Power Sounds) / Step 93 (Explosion Sounds)
        self.explosion_sound = self.load("assets/sounds/explosion.wav")
        self.fireball_sound = self.load("assets/sounds/fireball.wav")
        self.shield_sound = self.load("assets/sounds/shield.wav")

        self.loop_channel = pygame.mixer.Channel(0)

    def load(self, path):

        if not self.enabled:
            return None

        if not os.path.exists(path):

            print(f"[Sound] Missing: {path}")
            return None

        try:

            return pygame.mixer.Sound(path)

        except Exception as e:

            print(f"[Sound] Failed to load {path}: {e}")
            return None

    def play_open(self):

        if self.open_sound:
            self.open_sound.play()

    def play_close(self):

        if self.close_sound:
            self.close_sound.play()

    def play_lightning(self):

        if self.lightning_sound:
            self.lightning_sound.play()

    def play_sparks(self):

        if self.spark_sound:
            self.spark_sound.play()

    def play_explosion(self):

        if self.explosion_sound:
            self.explosion_sound.play()

    def play_fireball(self):

        if self.fireball_sound:
            self.fireball_sound.play()

    def play_shield(self):

        if self.shield_sound:
            self.shield_sound.play()

    def play_loop(self):

        if self.loop_sound:

            if not self.loop_channel.get_busy():

                self.loop_channel.play(
                    self.loop_sound,
                    loops=-1
                )

    def stop_loop(self):

        if self.loop_channel.get_busy():

            self.loop_channel.stop()

    def set_volume(self, volume):

        volume = max(0.0, min(1.0, volume))

        for sound in [

            self.open_sound,
            self.close_sound,
            self.loop_sound,
            self.lightning_sound,
            self.spark_sound,
            self.explosion_sound,
            self.fireball_sound,
            self.shield_sound

        ]:

            if sound:
                sound.set_volume(volume)
