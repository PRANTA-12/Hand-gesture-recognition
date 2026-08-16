import cv2

class MotionBlur:

    def __init__(self):
        self.previous = None
        self.active = False

    def apply(self, frame):

        if self.previous is None:
            self.previous = frame.copy()
            self.active = False
            return frame

        blurred = cv2.addWeighted(
            frame,
            0.80,
            self.previous,
            0.20,
            0
        )

        self.previous = frame.copy()

        self.active = True


        return blurred