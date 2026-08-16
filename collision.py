import math


class CollisionManager:

    def __init__(self):
        pass

    # -------------------------------
    # Screen Boundary Collision
    # -------------------------------
    def check_screen(self, x, y, width, height, margin=20):

        if (
            x < margin
            or x > width - margin
            or y < margin
            or y > height - margin
        ):
            return True

        return False

    # -------------------------------
    # Circle Collision
    # -------------------------------
    def check_circle(self, x1, y1, r1, x2, y2, r2):

        dx = x1 - x2
        dy = y1 - y2

        distance_sq = dx * dx + dy * dy

        radius = r1 + r2

        return distance_sq <= radius * radius

    # -------------------------------
    # Rectangle Collision
    # -------------------------------
    def check_rectangle(self, x, y, rect):

        rx, ry, rw, rh = rect

        return (
            rx <= x <= rx + rw
            and
            ry <= y <= ry + rh
        )