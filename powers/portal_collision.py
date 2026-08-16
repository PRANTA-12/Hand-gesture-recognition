import math


class PortalCollision:

    def __init__(self):

        self.center = (0, 0)
        self.radius = 0

    # ---------------------------------
    # Update Portal Area
    # ---------------------------------

    def update(
        self,
        center,
        radius
    ):

        self.center = center
        self.radius = radius

    # ---------------------------------
    # Point Collision
    # ---------------------------------

    def contains_point(
        self,
        point
    ):

        px, py = point
        cx, cy = self.center

        distance = math.hypot(
            px - cx,
            py - cy
        )

        return distance <= self.radius

    # ---------------------------------
    # Circle Collision
    # ---------------------------------

    def intersects_circle(
        self,
        center,
        radius
    ):

        cx1, cy1 = self.center
        cx2, cy2 = center

        distance = math.hypot(
            cx2 - cx1,
            cy2 - cy1
        )

        return distance <= (self.radius + radius)

    # ---------------------------------
    # Rectangle Collision
    # ---------------------------------

    def intersects_rect(
        self,
        x,
        y,
        w,
        h
    ):

        closest_x = max(
            x,
            min(self.center[0], x + w)
        )

        closest_y = max(
            y,
            min(self.center[1], y + h)
        )

        distance = math.hypot(
            closest_x - self.center[0],
            closest_y - self.center[1]
        )

        return distance <= self.radius

    # ---------------------------------
    # Distance
    # ---------------------------------

    def distance_to(
        self,
        point
    ):

        px, py = point
        cx, cy = self.center

        return math.hypot(
            px - cx,
            py - cy
        )

    # ---------------------------------
    # Reset
    # ---------------------------------

    def reset(self):

        self.center = (0, 0)
        self.radius = 0