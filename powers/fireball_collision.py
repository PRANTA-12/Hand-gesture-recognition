import math


class FireballCollision:

    def __init__(self):

        self.screen_padding = 20
        self.target_radius = 25

    # ---------------------------------
    # Screen Collision
    # ---------------------------------

    def check_screen(
        self,
        position,
        frame_width,
        frame_height
    ):

        x, y = position

        if x < -self.screen_padding:
            return True

        if x > frame_width + self.screen_padding:
            return True

        if y < -self.screen_padding:
            return True

        if y > frame_height + self.screen_padding:
            return True

        return False

    # ---------------------------------
    # Target Collision
    # ---------------------------------

    def check_target(
        self,
        position,
        target
    ):

        if target is None:
            return False

        px, py = position
        tx, ty = target

        distance = math.hypot(
            tx - px,
            ty - py
        )

        return distance <= self.target_radius

    # ---------------------------------
    # Circle Collision
    # ---------------------------------

    def check_circle(
        self,
        position1,
        radius1,
        position2,
        radius2
    ):

        x1, y1 = position1
        x2, y2 = position2

        distance = math.hypot(
            x2 - x1,
            y2 - y1
        )

        return distance <= (
            radius1 + radius2
        )

    # ---------------------------------
    # Rectangle Collision
    # ---------------------------------

    def check_rect(
        self,
        position,
        rect
    ):

        px, py = position

        rx = rect[0]
        ry = rect[1]
        rw = rect[2]
        rh = rect[3]

        return (

            rx <= px <= rx + rw

            and

            ry <= py <= ry + rh

        )

    # ---------------------------------
    # Collision With Multiple Targets
    # ---------------------------------

    def check_targets(
        self,
        position,
        targets
    ):

        if targets is None:
            return None

        for target in targets:

            if self.check_target(
                position,
                target
            ):

                return target

        return None

    # ---------------------------------
    # Update Collision
    # ---------------------------------

    def update(
        self,
        position,
        frame_width,
        frame_height,
        target=None
    ):

        result = {

            "screen": False,
            "target": False

        }

        if self.check_screen(
            position,
            frame_width,
            frame_height
        ):

            result["screen"] = True

        if target is not None:

            if self.check_target(
                position,
                target
            ):

                result["target"] = True

        return result

    # ---------------------------------
    # Reset
    # ---------------------------------

    def reset(self):

        pass