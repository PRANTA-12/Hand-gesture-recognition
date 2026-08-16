from enum import Enum


class TwoHandPower(Enum):
    NONE = "NONE"
    PORTAL = "PORTAL"
    RASENGAN = "RASENGAN"
    KAMEHAMEHA = "KAMEHAMEHA"
    ARC_REACTOR = "ARC_REACTOR"
    GRAVITY_ORB = "GRAVITY_ORB"
    DUAL_LIGHTNING = "DUAL_LIGHTNING"
    DUAL_FIREBALL = "DUAL_FIREBALL"


class TwoHandGesture:

    def __init__(self):
        self.current_power = TwoHandPower.NONE

    def recognize(self, left_gesture, right_gesture):

        self.current_power = TwoHandPower.NONE

        # No hands
        if left_gesture is None or right_gesture is None:
            return self.current_power

        # ===========================
        # Doctor Strange Portal
        # ===========================
        if (
            left_gesture == "OPEN_HAND"
            and right_gesture == "OPEN_HAND"
        ):
            self.current_power = TwoHandPower.PORTAL
   

        # ===========================
        # Rasengan
        # ===========================
        elif (
            left_gesture == "PINCH"
            and right_gesture == "PINCH"
        ):
            self.current_power = TwoHandPower.RASENGAN

        # ===========================
        # Kamehameha
        # ===========================
        elif (
            left_gesture == "FIST"
            and right_gesture == "OPEN_HAND"
        ):
            self.current_power = TwoHandPower.KAMEHAMEHA

        # ===========================
        # Arc Reactor
        # ===========================
        elif (
            left_gesture == "OPEN_HAND"
            and right_gesture == "FIST"
        ):
            self.current_power = TwoHandPower.ARC_REACTOR

        # ===========================
        # Gravity Orb
        # ===========================
        elif (
            left_gesture == "FIST"
            and right_gesture == "FIST"
        ):
            self.current_power = TwoHandPower.GRAVITY_ORB

        # ===========================
        # Dual Lightning
        # ===========================
        elif (
            left_gesture in ("PEACE", "TWO_FINGERS")
            and
            right_gesture in ("PEACE", "TWO_FINGERS")
        ):
            self.current_power = TwoHandPower.DUAL_LIGHTNING
        # ===========================
        # Dual Fireball
        # ===========================
        elif (
            left_gesture == "THUMBS_UP"
            and right_gesture == "THUMBS_UP"
        ):
            self.current_power = TwoHandPower.DUAL_FIREBALL

        return self.current_power

    def get_power(self):
        return self.current_power

    def reset(self):
        self.current_power = TwoHandPower.NONE