from physics.physics_body import PhysicsBody
from physics.vector2 import Vector2


class FireballPhysics(PhysicsBody):

    def __init__(self):
        super().__init__()

        # -------------------------
        # Physics Settings
        # -------------------------

        self.radius = 18
        self.mass = 1.0
        self.drag = 0.985
        self.bounce = 0.0
        self.max_speed = 1200

        self.distance = 0.0
        self.max_distance = 900

        self.active = False

    # ---------------------------------
    # Start
    # ---------------------------------

    def start(self, position, angle, speed):

        super().start()

        self.position = Vector2(
            position[0],
            position[1]
        )

        self.velocity = Vector2.from_angle(
            angle,
            speed
        )

        self.acceleration = Vector2.zero()

        self.distance = 0.0

    # ---------------------------------
    # Stop
    # ---------------------------------

    def stop(self):

        super().stop()

    # ---------------------------------
    # Move Toward Target
    # ---------------------------------

    def seek(
        self,
        target,
        strength=0.08
    ):

        if target is None:
            return

        target_vector = Vector2(
            target[0],
            target[1]
        )

        direction = (
            target_vector -
            self.position
        ).normalize()

        desired_velocity = (
            direction *
            self.max_speed
        )

        steering = (
            desired_velocity -
            self.velocity
        ) * strength

        self.apply_force(
            steering
        )

    # ---------------------------------
    # Update
    # ---------------------------------

    def update(self, dt):

        if not self.active:
            return

        old_position = self.position.copy()

        super().update(dt)

        self.distance += (
            self.position.distance_to(
                old_position
            )
        )

    # ---------------------------------
    # Screen Position
    # ---------------------------------

    def center(self):

        return (
            int(self.position.x),
            int(self.position.y)
        )

    # ---------------------------------
    # Distance Limit
    # ---------------------------------

    def reached_limit(self):

        return (
            self.distance >=
            self.max_distance
        )

    # ---------------------------------
    # Reset
    # ---------------------------------

    def reset(self):

        super().reset()

        self.distance = 0.0

    # ---------------------------------
    # Destroy
    # ---------------------------------

    def destroy(self):

        super().destroy()