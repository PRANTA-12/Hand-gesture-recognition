import time
from config import *


class CooldownManager:

    def __init__(self):

        self.last_time = {}

        self.cooldowns = {
            "FIST": FIST_COOLDOWN,
            "THUMBS_UP": THUMBS_UP_COOLDOWN,
            "SPIDER": SPIDER_COOLDOWN,
            "PINCH": 0.2,
            "ROCK": 0.3,
            "OPEN_HAND": 0.0,
            "ONE_FINGER": 0.0,
            "TWO_FINGERS": 0.2
        }

    # -------------------------
    # Ready
    # -------------------------

    def ready(self, gesture):

        now = time.time()

        last = self.last_time.get(gesture, 0)

        cooldown = self.cooldowns.get(gesture, 0)

        return (now - last) >= cooldown

    # -------------------------
    # Trigger
    # -------------------------

    def trigger(self, gesture):

        self.last_time[gesture] = time.time()

    # -------------------------
    # Reset
    # -------------------------

    def reset(self):

        self.last_time.clear()

    # -------------------------
    # Set Cooldown
    # -------------------------

    def set_cooldown(self, gesture, value):

        self.cooldowns[gesture] = value

    # -------------------------
    # Get Cooldown
    # -------------------------

    def get_cooldown(self, gesture):

        return self.cooldowns.get(gesture, 0)