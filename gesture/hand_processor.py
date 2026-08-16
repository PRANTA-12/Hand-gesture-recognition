import math

from ai_gesture import AIGestureRecognizer
from ai_stabilizer import AIStabilizer
from gesture_recognizer import GestureRecognizer
from gesture_lock import GestureLock
from gesture_state_machine import GestureStateMachine

from hand_position import HandPosition
from hand_rotation import HandRotation
from landmark_filter import LandmarkFilter


class HandProcessor:

    def __init__(self):


        self.landmark_filter = LandmarkFilter(alpha=0.7)

        self.smoothX = 0
        self.smoothY = 0

        self.alpha = 0.80

        self.glow_phase = 0
        self.orbit_angle = 0

    # ---------------------------------------
    # Process One Hand
    # ---------------------------------------

    def process(self, hand):

        if hand is None or len(hand) < 21:

            self.reset()

            return None

        # -------------------------
        # Smooth landmarks
        # -------------------------

        hand = self.landmark_filter.smooth(hand)


        # -------------------------
        # Palm Center
        # -------------------------

        palmX, palmY = HandPosition.get_palm_center(hand)

        self.smoothX = int(

            self.alpha * self.smoothX +

            (1 - self.alpha) * palmX

        )

        self.smoothY = int(

            self.alpha * self.smoothY +

            (1 - self.alpha) * palmY

        )

        # -------------------------
        # Rotation
        # -------------------------

        angle = HandRotation.get_rotation(hand)

        # -------------------------
        # Animation Counters
        # -------------------------

        self.glow_phase += 6

        if self.glow_phase >= 360:

            self.glow_phase = 0

        self.orbit_angle += 5

        if self.orbit_angle >= 360:

            self.orbit_angle = 0

        glow_radius = 38 + int(

            6 * math.sin(

                math.radians(self.glow_phase)

            )

        )

        # -------------------------
        # Return Processed Data
        # -------------------------

        return {

            "hand": hand,

            "smoothX": self.smoothX,

            "smoothY": self.smoothY,

            "handAngle": angle,

            "glowRadius": glow_radius,

            "orbitAngle": self.orbit_angle,

            "palm": (

                self.smoothX,

                self.smoothY

            ),

            "indexFinger": (

                hand[8][1],

                hand[8][2]

            )

        }

    # ---------------------------------------
    # Reset
    # ---------------------------------------

    def reset(self):

        self.smoothX = 0

        self.smoothY = 0

        self.glow_phase = 0

        self.orbit_angle = 0