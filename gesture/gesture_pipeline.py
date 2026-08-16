from gesture_recognizer import GestureRecognizer
from gesture_manager import GestureManager
from ai_gesture import AIGestureRecognizer
from ai_stabilizer import AIStabilizer
from gesture_lock import GestureLock
from gesture_state_machine import GestureStateMachine
from gesture_state import GestureState
from two_hand_gesture import TwoHandGesture
from gesture.gesture_stabilizer import GestureStabilizer
from .two_hand_stabilizer import TwoHandStabilizer


class GesturePipeline:

    def __init__(self):

        self.manager = GestureManager()
        self.ai = AIGestureRecognizer()

        self.left_ai_stabilizer = AIStabilizer()
        self.right_ai_stabilizer = AIStabilizer()

        self.left_stabilizer = GestureStabilizer()

        self.right_stabilizer = GestureStabilizer()

        self.left_lock = GestureLock()
        self.right_lock = GestureLock()

        self.left_state_machine = GestureStateMachine()
        self.right_state_machine = GestureStateMachine()

        self.rule_gesture = GestureRecognizer()

        self.two_hand = TwoHandGesture()

        self.two_hand_stabilizer = TwoHandStabilizer()

    # -----------------------------------------
    # Main Processing
    # -----------------------------------------

    def process(
        self,
        allHands,
        handTypes
    ):

        self.manager.update(
            allHands,
            handTypes
        )

        leftHand = self.manager.get_left()
        rightHand = self.manager.get_right()

        leftGesture = None
        rightGesture = None

        leftConfidence = 0.0
        rightConfidence = 0.0

        leftState = GestureState.NONE
        rightState = GestureState.NONE
        # ============================
        # LEFT HAND
        # ============================

        if leftHand is not None and len(leftHand) >= 21:

            leftGesture, leftConfidence = self.ai.predict(leftHand)

            # Use rule gesture only when AI is not confident
            if leftConfidence < 0.80:

                fingers = self.rule_gesture.fingers_up(leftHand, "Left")
                ruleGesture = self.rule_gesture.recognize(fingers)

                if ruleGesture != "UNKNOWN":
                    leftGesture = ruleGesture
            

            leftGesture = self.left_ai_stabilizer.update(
                leftGesture,
                leftConfidence
            )

            leftGesture = self.left_stabilizer.update(leftGesture)

            leftGesture = self.left_lock.update(leftGesture)

            leftGesture, leftState = self.left_state_machine.update(leftGesture)
            

            if self.rule_gesture.is_pinch(leftHand):
                leftGesture = "PINCH"

        # ============================
        # RIGHT HAND
        # ============================

        if rightHand is not None and len(rightHand) >= 21:

            rightGesture, rightConfidence = self.ai.predict(rightHand)

            # Use rule gesture only when AI is not confident
            if rightConfidence < 0.80:

                fingers = self.rule_gesture.fingers_up(rightHand, "Right")
                ruleGesture = self.rule_gesture.recognize(fingers)

                if ruleGesture != "UNKNOWN":
                    rightGesture = ruleGesture
            

            rightGesture = self.right_ai_stabilizer.update(
                rightGesture,
                rightConfidence
            )

            rightGesture = self.right_stabilizer.update(rightGesture)

            rightGesture = self.right_lock.update(rightGesture)

            rightGesture, rightState = self.right_state_machine.update(rightGesture)
           


            if self.rule_gesture.is_pinch(rightHand):
                rightGesture = "PINCH"

        # ============================
        # TWO HAND POWER
        # ============================

        power = self.two_hand.recognize(
            leftGesture,
            rightGesture
        )
        power = self.two_hand_stabilizer.update(power)
        

        return {

            "left": {
                "hand": leftHand,
                "gesture": leftGesture,
                "confidence": leftConfidence,
                "state": leftState
            },

            "right": {
                "hand": rightHand,
                "gesture": rightGesture,
                "confidence": rightConfidence,
                "state": rightState
            },

            "two_hand_power": power

        }

    # -----------------------------------------
    # Reset
    # -----------------------------------------

    def reset(self):

        self.left_ai_stabilizer.reset()
        self.right_ai_stabilizer.reset()

        self.left_stabilizer.reset()

        self.right_stabilizer.reset()

        self.left_lock.reset()
        self.right_lock.reset()

        self.left_state_machine.reset()
        self.right_state_machine.reset()

        self.two_hand.reset()
        
        self.two_hand_stabilizer.reset()