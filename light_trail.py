import cv2


class LightTrail:

    def __init__(self):
        self.points = []

    def update(self, frame, center):

        self.points.append(center)

        if len(self.points) > 25:
            self.points.pop(0)

        for i in range(1, len(self.points)):

            thickness = max(1, 8 - i // 3)

            cv2.line(
                frame,
                self.points[i - 1],
                self.points[i],
                (255, 255, 0),
                thickness,
                lineType=cv2.LINE_AA
            )