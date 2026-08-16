from physics.vector2 import Vector2


class FireballTarget:

    def __init__(self):

        self.target = None

        # Homing strength (0.0 - 1.0)
        self.turn_speed = 0.08

        # Enable / Disable homing
        self.enabled = True

    # ---------------------------------
    # Set Target
    # ---------------------------------

    def set_target(self, target):

        self.target = target

    # ---------------------------------
    # Clear Target
    # ---------------------------------

    def clear(self):

        self.target = None

    # ---------------------------------
    # Enable
    # ---------------------------------

    def enable(self):

        self.enabled = True

    # ---------------------------------
    # Disable
    # ---------------------------------

    def disable(self):

        self.enabled = False

    # ---------------------------------
    # Has Target
    # ---------------------------------

    def has_target(self):

        return self.target is not None

    # ---------------------------------
    # Update Homing
    # ---------------------------------

    def update(self, physics):

        if not self.enabled:
            return

        if self.target is None:
            return

        target = Vector2(
            self.target[0],
            self.target[1]
        )

        direction = (
            target -
            physics.position
        ).normalize()

        desired_velocity = (
            direction *
            physics.max_speed
        )

        steering = (
            desired_velocity -
            physics.velocity
        ) * self.turn_speed

        physics.apply_force(
            steering
        )

    # ---------------------------------
    # Distance
    # ---------------------------------

    def distance(self, physics):

        if self.target is None:
            return None

        target = Vector2(
            self.target[0],
            self.target[1]
        )

        return physics.position.distance_to(
            target
        )

    # ---------------------------------
    # Target Reached
    # ---------------------------------

    def reached(
        self,
        physics,
        radius=20
    ):

        d = self.distance(physics)

        if d is None:
            return False

        return d <= radius

    # ---------------------------------
    # Reset
    # ---------------------------------

    def reset(self):

        self.clear()