import cv2
import mediapipe as mp
from config import *


class HandDetector:

    def __init__(self):

        self.mpHands = mp.solutions.hands

        self.hands = self.mpHands.Hands(
            static_image_mode=False,
            max_num_hands=MAX_HANDS,
            model_complexity=0,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )

        self.drawer = mp.solutions.drawing_utils

        self.results = None

    # ---------------------------------
    # Detect Hands
    # ---------------------------------

    def findHands(self, frame, draw=True):

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        rgb.flags.writeable = False

        self.results = self.hands.process(rgb)

        rgb.flags.writeable = True
        if draw and self.results.multi_hand_landmarks:

            for hand in self.results.multi_hand_landmarks:

                self.drawer.draw_landmarks(
                    frame,
                    hand,
                    self.mpHands.HAND_CONNECTIONS
                )

        return frame

    # ---------------------------------
    # Return All Hands
    # ---------------------------------

    def findPosition(self, frame):

        allHands = []
        handTypes = []

        if self.results and self.results.multi_hand_landmarks:

            h, w, _ = frame.shape

            for hand, handedness in zip(
                self.results.multi_hand_landmarks,
                self.results.multi_handedness
            ):

                lmList = []

                for idx, lm in enumerate(hand.landmark):

                    x = int(lm.x * w)
                    y = int(lm.y * h)
                    z = lm.z

                    lmList.append([idx, x, y, z])

                allHands.append(lmList)

                handTypes.append(
                    handedness.classification[0].label
                )

        return allHands, handTypes

    # ---------------------------------
    # Left Hand
    # ---------------------------------

    def getLeftHand(self, frame):

        hands, types = self.findPosition(frame)

        for hand, handType in zip(hands, types):

            if handType == "Left":
                return hand

        return None

    # ---------------------------------
    # Right Hand
    # ---------------------------------

    def getRightHand(self, frame):

        hands, types = self.findPosition(frame)

        for hand, handType in zip(hands, types):

            if handType == "Right":
                return hand

        return None