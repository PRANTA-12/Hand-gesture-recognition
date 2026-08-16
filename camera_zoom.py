import cv2

class CameraZoom:

    def __init__(self):
        self.scale = 1.0
        self.target = 1.0
        self.active = False

    def trigger(self, amount=1.15):
        self.target = amount
        self.active = True

    def update(self):
        self.scale += (self.target - self.scale) * 0.15

        if abs(self.scale - self.target) < 0.01:
            self.target = 1.0
            
            if abs(self.scale - 1.0) < 0.01:
                self.active = False

    def apply(self, frame):

        self.update()

        if abs(self.scale - 1.0) < 0.01:
            return frame

        h, w = frame.shape[:2]

        nw = int(w / self.scale)
        nh = int(h / self.scale)

        x = (w - nw) // 2
        y = (h - nh) // 2

        crop = frame[y:y+nh, x:x+nw]

        return cv2.resize(crop, (w, h))