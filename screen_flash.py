import cv2

class ScreenFlash:

    def __init__(self):
        self.alpha = 0
        self.active = False

    def trigger(self):
        self.alpha = 180
        self.active = True

    def update(self, frame):

        if self.alpha <= 0:
            self.active = False
            return

        overlay = frame.copy()

        cv2.rectangle(
            overlay,
            (0, 0),
            (frame.shape[1], frame.shape[0]),
            (0, 180, 255),
            -1
        )

        cv2.addWeighted(
            overlay,
            self.alpha / 255,
            frame,
            1 - self.alpha / 255,
            0,
            frame
        )

        self.alpha -= 15
        if self.alpha <= 0:

            self.alpha = 0

            self.active = False