import math
from two_hand_gesture import TwoHandPower


class TwoHandPowerController:

    def __init__(self, power_manager):

        self.power_manager = power_manager


    def stop_all(self):

        self.power_manager.stop_all()


    def update(
        self,
        power,
        left_hand,
        right_hand
    ):
        
        self.portal = self.power_manager.get("PORTAL")
        self.rasengan = self.power_manager.get("RASENGAN")
        self.kamehameha = self.power_manager.get("KAMEHAMEHA")
        self.gravity_orb = self.power_manager.get("GRAVITY_ORB")
        self.arc_reactor = self.power_manager.get("ARC_REACTOR")
        self.dual_lightning = self.power_manager.get("DUAL_LIGHTNING")

        # -----------------------------
        # Need both hands
        # -----------------------------
        if (
            left_hand is None
            or right_hand is None
        ):

            self.stop_all()
            return

        # -----------------------------
        # Palm Centers
        # -----------------------------
        left_x = left_hand[0][1]
        left_y = left_hand[0][2]

        right_x = right_hand[0][1]
        right_y = right_hand[0][2]

        left_center = (
            left_x,
            left_y
        )

        right_center = (
            right_x,
            right_y
        )

        center = (
            (left_x + right_x) // 2,
            (left_y + right_y) // 2
        )

        # =====================================================
        # Doctor Strange Portal
        # =====================================================

        if power == TwoHandPower.PORTAL:
            self.power_manager.activate("PORTAL")

            self.rasengan.stop()

            if not self.portal.active:
                self.portal.start(center)

            else:
                self.portal.move(center)

            return

        # =====================================================
        # Rasengan
        # =====================================================

        if power == TwoHandPower.RASENGAN:
            self.power_manager.activate("RASENGAN")

            self.portal.stop()

            if not self.rasengan.active:
                self.rasengan.start(center)

            else:
                self.rasengan.move(center)

            return

        # =====================================================
        # Future Powers
        # =====================================================

        elif power == TwoHandPower.KAMEHAMEHA:
            self.power_manager.activate("KAMEHAMEHA")

            self.portal.stop()
            self.rasengan.stop()

            angle = math.atan2(
                right_y - left_y,
                right_x - left_x
            )

            if not self.kamehameha.active:

                self.kamehameha.start(
                    center,
                    angle
                )

            else:

                self.kamehameha.move(center)
                self.kamehameha.rotate(angle)

            return
        

        elif power == TwoHandPower.ARC_REACTOR:
            self.power_manager.activate("ARC_REACTOR")

            self.portal.stop()
            self.rasengan.stop()
            self.kamehameha.stop()
            self.gravity_orb.stop()

            if not self.arc_reactor.active:

                self.arc_reactor.start(center)

            else:

                self.arc_reactor.move(center)

            return

        elif power == TwoHandPower.GRAVITY_ORB:
            self.power_manager.activate("GRAVITY_ORB")

            self.portal.stop()
            self.rasengan.stop()
            self.kamehameha.stop()

            if not self.gravity_orb.active:

                self.gravity_orb.start(center)

            else:

                self.gravity_orb.move(center)

            return

        elif power == TwoHandPower.DUAL_LIGHTNING:
            self.power_manager.activate("DUAL_LIGHTNING")

            self.portal.stop()
            self.rasengan.stop()
            self.kamehameha.stop()
            self.gravity_orb.stop()
            self.arc_reactor.stop()

            if not self.dual_lightning.active:

                self.dual_lightning.start(
                    left_center,
                    right_center
                )

            else:

                self.dual_lightning.move(
                    left_center,
                    right_center
                )

            return

        elif power == TwoHandPower.DUAL_FIREBALL:
            pass

        # =====================================================
        # No Power
        # =====================================================

        else:

            self.stop_all()