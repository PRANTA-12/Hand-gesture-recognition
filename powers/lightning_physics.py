from physics.physics_body import PhysicsBody
from physics.vector2 import Vector2


class LightningPhysics(PhysicsBody):

    def __init__(self):
        super().__init__()

        # -----------------------------
        # Lightning Settings
        # -----------------------------
        self.start_position = Vector2.zero()
        self.end_position = Vector2.zero()
        self.target = None
        self.angle = 0.0

        self.length = 0.0
        self.max_length = 350.0

        self.growth_speed = 1400.0

        self.intensity = 1.0

        self.duration = 0.20
        self.elapsed = 0.0

        self.finished = False

    # ---------------------------------
    # Start
    # ---------------------------------

    def start(self, start_pos, angle):

        super().start()

        self.start_position = Vector2(
            start_pos[0],
            start_pos[1]
        )

        self.length = 0.0

        self.intensity = 1.0

        self.elapsed = 0.0

        self.finished = False

        self.target = None
        self.angle = angle if angle is not None else 0.0

        self.update_end(angle)

    # ---------------------------------
    # Update
    # ---------------------------------

    def update(self, dt):

        if not self.active:
            return

        self.elapsed += dt

        self.length += self.growth_speed * dt

        if self.target is not None:

            self.end_position = Vector2(
                self.target[0],
                self.target[1]
            )
        else:
            self.update_end(self.angle)

        if self.length > self.max_length:
            self.length = self.max_length

        self.intensity = max(
            0.0,
            1.0 - self.elapsed / self.duration
        )

        if self.elapsed >= self.duration:

            self.finished = True

            self.destroy()

    # ---------------------------------
    # Update End Point
    # ---------------------------------

    def update_end(self, angle):

        direction = Vector2.from_angle(angle)

        self.end_position = (
            self.start_position +
            direction * self.length
        )

    # ---------------------------------
    # Set Direction
    # ---------------------------------

    def set_direction(self, angle):

        self.angle = angle

        self.update_end(angle)
    # ---------------------------------
    # Set Target
    # ---------------------------------

    def set_target(self, target):

        self.target = target

    # ---------------------------------
    # Set Angle
    # ---------------------------------

    def set_angle(self, angle):

        self.angle = angle

        self.update_end(angle)
  
  
    # ---------------------------------
    # Progress
    # ---------------------------------

    def progress(self):

        if self.duration == 0:
            return 1.0

        return min(
            self.elapsed / self.duration,
            1.0
        )
    
    # ---------------------------------
    # Get Start Position
    # ---------------------------------

    def get_start_position(self):

        return (
            int(self.start_position.x),
            int(self.start_position.y)
        )
    
    # ---------------------------------
    # Get End Position
    # ---------------------------------

    def get_end_position(self):

        return (
            int(self.end_position.x),
            int(self.end_position.y)
        )
    
    # ---------------------------------
    # Get Intensity
    # ---------------------------------

    def get_intensity(self):

        return self.intensity

    # ---------------------------------
    # Is Finished
    # ---------------------------------

    def is_finished(self):

        return self.finished

    # ---------------------------------
    # Reset
    # ---------------------------------

    def reset(self):

        super().reset()

        self.length = 0.0

        self.elapsed = 0.0

        self.intensity = 1.0

        self.finished = False

    # ---------------------------------
    # Destroy
    # ---------------------------------

    def destroy(self):

        self.finished = True

        super().destroy()