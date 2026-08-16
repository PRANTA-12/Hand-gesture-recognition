import cv2


class TrailManager:

    def __init__(self, max_points=20):

        self.max_points = max_points
        self.points = []

    def add(self, position):

        self.points.append(position)

        if len(self.points) > self.max_points:
            self.points.pop(0)

    def clear(self):

        self.points.clear()

    def update(self):
        pass

    def draw(
        self,
        frame,
        outer_color=(0, 80, 255),
        inner_color=(0, 170, 255)
    ):

        if len(self.points) < 2:
            return

        total = len(self.points)

        for i in range(total - 1):

            p1 = self.points[i]
            p2 = self.points[i + 1]

            thickness = max(
                1,
                int(8 * (i + 1) / total)
            )    

            cv2.line(
                frame,
                p1,
                p2,
                outer_color,
                thickness,
                lineType=cv2.LINE_AA
            )

            cv2.line(
                frame,
                p1,
                p2,
                inner_color,
                max(thickness - 2, 1),
                lineType=cv2.LINE_AA
            )