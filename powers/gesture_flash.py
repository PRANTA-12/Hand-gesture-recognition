import cv2

class GestureFlash:

    def __init__(self):
        self.frames = 0

    def trigger(self):
        self.frames = 8

    def draw(self, frame, center):

        if self.frames <= 0:
            return

        cv2.circle(
            frame,
            center,
            45,
            (0, 255, 255),
            3
        )

        self.frames -= 1