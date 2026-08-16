from gesture_actions import GESTURE_ACTIONS
from two_hand_gesture import TwoHandPower
from gesture_state import GestureState

class PowerPipeline:

    

    def __init__(

        self,

        power_controller,

        two_hand_controller,

        target_lock,

        fireball

    ):

        self.power_controller = power_controller

        self.two_hand_controller = two_hand_controller

        self.target_lock = target_lock

        self.fireball = fireball

        self.unknown_frames = 0
        self.max_unknown_frames = 6

    def process_single_hand(self, frame, handData):

        if handData is None:
            return

        gesture = handData.get("gesture")
        state = handData.get("state")

        if gesture is None:
            return

        if state != GestureState.CONFIRMED:
            return

        action = GESTURE_ACTIONS.get(gesture)

        if action is None:
            return

        self.power_controller.update(
            frame,
            action,
            handData
        )   

    # -----------------------------------
    # Update
    # -----------------------------------

    def update(
        self,
        frame,
        rightData,
        leftData,
        two_hand_power
    ):

        # =========================================
        # TWO-HAND POWER HAS HIGHEST PRIORITY
        # =========================================

        if two_hand_power != TwoHandPower.NONE:

            self.power_controller.stop_all()

            self.two_hand_controller.update(

                two_hand_power,

                leftData["hand"] if leftData else None,

                rightData["hand"] if rightData else None
            )

            # Target lock is not needed for two-hand mode
            self.target_lock.reset()

            return

        # =========================================
        # SINGLE-HAND POWER
        # =========================================

        selected_data = None

        # -----------------------------------------
        # Prefer RIGHT HAND
        # -----------------------------------------

        if rightData is not None:

            if rightData.get("state") == GestureState.CONFIRMED:

                gesture = rightData.get("gesture")

                action = GESTURE_ACTIONS.get(gesture)

                if action is not None:

                    selected_data = rightData

        # -----------------------------------------
        # Otherwise use LEFT HAND
        # -----------------------------------------

        if selected_data is None:

            if leftData is not None:

                if leftData.get("state") == GestureState.CONFIRMED:

                    gesture = leftData.get("gesture")

                    action = GESTURE_ACTIONS.get(gesture)

                    if action is not None:

                        selected_data = leftData

        # =========================================
        # NO CONFIRMED SINGLE-HAND POWER
        # =========================================

        if selected_data is None:

            self.unknown_frames += 1

            if self.unknown_frames >= self.max_unknown_frames:

                self.power_controller.stop_all()

                self.target_lock.reset()

            return

        # =========================================
        # PROCESS EXACTLY ONE HAND
        # =========================================
        self.unknown_frames = 0
        self.process_single_hand(
            frame,
            selected_data
        )

        # =========================================
        # FIREBALL TARGET
        # =========================================

        if (
            self.fireball.active
            and self.target_lock.locked
        ):

            self.fireball.set_target(
                (
                    self.target_lock.x,
                    self.target_lock.y
                )
            )

        # =========================================
        # TARGET LOCK
        # =========================================

        if selected_data is rightData:

            hand = rightData.get("hand")

            gesture = rightData.get("gesture")

            if (
                hand is not None
                and gesture == "ONE_FINGER"
            ):

                self.target_lock.update(
                    (
                        hand[8][1],
                        hand[8][2]
                    )
                )

            else:

                self.target_lock.reset()

        else:

            self.target_lock.reset()

    # -----------------------------------
    # Reset
    # -----------------------------------

    def reset(self):

        self.target_lock.reset()
        self.power_controller.stop_all()

        self.unknown_frames = 0