import math


class LightningCollision:

    def __init__(self):

        self.hit_radius = 25

    # ---------------------------------
    # Check Screen Bounds
    # ---------------------------------

    def check_screen(
        self,
        end_position,
        screen_width,
        screen_height
    ):

        x, y = end_position

        if x < 0:
            return True

        if x > screen_width:
            return True

        if y < 0:
            return True

        if y > screen_height:
            return True

        return False

    # ---------------------------------
    # Check Point Collision
    # ---------------------------------

    def check_point(
        self,
        end_position,
        point
    ):

        dx = end_position[0] - point[0]
        dy = end_position[1] - point[1]

        distance = math.sqrt(
            dx * dx +
            dy * dy
        )

        return distance <= self.hit_radius

    # ---------------------------------
    # Check Circle Collision
    # ---------------------------------

    def check_circle(
        self,
        end_position,
        center,
        radius
    ):

        dx = end_position[0] - center[0]
        dy = end_position[1] - center[1]

        distance = math.sqrt(
            dx * dx +
            dy * dy
        )

        return distance <= (
            self.hit_radius +
            radius
        )

    # ---------------------------------
    # Check Rectangle Collision
    # ---------------------------------

    def check_rectangle(
        self,
        end_position,
        rect
    ):

        x, y = end_position

        rx, ry, rw, rh = rect

        return (
            rx <= x <= rx + rw
            and
            ry <= y <= ry + rh
        )

    # ---------------------------------
    # Set Hit Radius
    # ---------------------------------

    def set_hit_radius(
        self,
        radius
    ):

        self.hit_radius = radius

    # ---------------------------------
    # Get Hit Radius
    # ---------------------------------

    def get_hit_radius(self):

        return self.hit_radius
    
    # ---------------------------------
    # Hit Target
    # ---------------------------------

    def hit_target(self, physics):

        if not hasattr(physics, "target"):
            return False

        if physics.target is None:
            return False

        dx = (
            physics.end_position.x
            - physics.target[0]
        )

        dy = (
            physics.end_position.y
            - physics.target[1]
        )

        distance = math.sqrt(
            dx * dx +
            dy * dy
        )

        return distance <= self.hit_radius