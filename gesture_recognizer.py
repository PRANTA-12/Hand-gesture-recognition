import math


class GestureRecognizer:

    def __init__(self):
        self.tipIds = [4, 8, 12, 16, 20]

    def fingers_up(self, landmarks, handType):

        if len(landmarks) < 21:
            return [0, 0, 0, 0, 0]

        fingers = []

        # Thumb (supports both hands)
        if handType == "Right":
            if landmarks[4][1] > landmarks[3][1]:
                fingers.append(1)
            else:
                fingers.append(0)

        else:  # Left hand
            if landmarks[4][1] < landmarks[3][1]:
                fingers.append(1)
            else:
                fingers.append(0)

        # Index, Middle, Ring, Pinky
        for tip in self.tipIds[1:]:

            if landmarks[tip][2] < landmarks[tip - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        return fingers

    def recognize(self, fingers):

        # ---------------------------------
        # OPEN HAND
        # ---------------------------------
        if fingers[1:] == [1, 1, 1, 1]:
            return "OPEN_HAND"

        # ---------------------------------
        # FIST
        # ---------------------------------
        elif sum(fingers) == 0:
            return "FIST"

        # ---------------------------------
        # SPIDER
        # IMPORTANT:
        # Check BEFORE TWO_FINGERS
        # ---------------------------------
        elif fingers == [1, 1, 1, 0, 0]:
            return "SPIDER"

        # ---------------------------------
        # THUMBS UP
        # ---------------------------------
        elif fingers == [1, 0, 0, 0, 0]:
            return "THUMBS_UP"

        # ---------------------------------
        # ONE FINGER
        # ---------------------------------
        elif fingers == [0, 1, 0, 0, 0]:
            return "ONE_FINGER"

        # ---------------------------------
        # TWO FINGERS
        # ---------------------------------
        elif fingers == [0, 1, 1, 0, 0]:
            return "TWO_FINGERS"

        # ---------------------------------
        # ROCK
        # ---------------------------------
        elif fingers[1:] == [1, 0, 0, 1]:
            return "ROCK"

        # ---------------------------------
        # UNKNOWN
        # ---------------------------------
        else:
            return "UNKNOWN"

    def is_pinch(self, landmarks, threshold=35):

        x1, y1 = landmarks[4][1], landmarks[4][2]
        x2, y2 = landmarks[8][1], landmarks[8][2]

        distance = math.hypot(x2 - x1, y2 - y1)

        return distance < threshold