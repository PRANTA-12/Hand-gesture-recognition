import math


class LightningTarget:

    def __init__(self):

        self.target = None

        self.locked = False

        self.lock_distance = 400

    # ---------------------------------
    # Set Target
    # ---------------------------------

    def set_target(self, position):

        self.target = position

        self.locked = True

    # ---------------------------------
    # Clear Target
    # ---------------------------------

    def clear(self):

        self.target = None

        self.locked = False

    # ---------------------------------
    # Has Target
    # ---------------------------------

    def has_target(self):

        return self.target is not None

    # ---------------------------------
    # Get Target
    # ---------------------------------

    def get_target(self):

        return self.target

    # ---------------------------------
    # Is Locked
    # ---------------------------------

    def is_locked(self):

        return self.locked

    # ---------------------------------
    # Find Nearest Target
    # ---------------------------------

    def find_nearest(

        self,

        origin,

        targets

    ):

        nearest = None

        nearest_distance = self.lock_distance

        ox, oy = origin

        for target in targets:

            tx, ty = target

            dx = tx - ox
            dy = ty - oy

            distance = math.sqrt(
                dx * dx +
                dy * dy
            )

            if distance < nearest_distance:

                nearest_distance = distance

                nearest = target

        if nearest is not None:

            self.target = nearest

            self.locked = True

        else:

            self.clear()

    # ---------------------------------
    # Update
    # ---------------------------------

    def update(self, physics):

        if self.target is None:

            self.locked = False

            return
        self.locked = True

        physics.end_position.x = self.target[0]

        physics.end_position.y = self.target[1]

    # ---------------------------------
    # Check Reached
    # ---------------------------------

    def reached(

        self,

        physics,

        threshold=20

    ):

        if self.target is None:

            return False

        dx = (
            physics.end_position.x
            - self.target[0]
        )

        dy = (
            physics.end_position.y
            - self.target[1]
        )

        distance = math.sqrt(
            dx * dx +
            dy * dy
        )

        return distance <= threshold

    # ---------------------------------
    # Remove Target
    # ---------------------------------

    def remove(self):

        self.clear()