from physics.vector2 import Vector2


class PhysicsBody:

    def __init__(self):

        # -------------------------
        # Transform
        # -------------------------

        self.position = Vector2()

        self.velocity = Vector2()

        self.acceleration = Vector2()

        # -------------------------
        # Physics
        # -------------------------

        self.mass = 1.0

        self.drag = 0.98

        self.gravity = Vector2(0, 0)

        self.bounce = 0.75

        self.max_speed = 1200

        # -------------------------
        # Collision
        # -------------------------

        self.radius = 10

        self.collidable = True

        # -------------------------
        # Lifetime
        # -------------------------

        self.life = 0.0

        self.max_life = -1

        self.alive = True

        self.active = False

    # ---------------------------------
    # Start
    # ---------------------------------

    def start(self):

        self.active = True
        self.alive = True

    # ---------------------------------
    # Stop
    # ---------------------------------

    def stop(self):

        self.active = False

    # ---------------------------------
    # Reset
    # ---------------------------------

    def reset(self):

        self.position = Vector2()

        self.velocity = Vector2()

        self.acceleration = Vector2()

        self.life = 0

        self.active = False

        self.alive = True

    # ---------------------------------
    # Apply Force
    # ---------------------------------

    def apply_force(self, force):

        self.acceleration += force / self.mass

    # ---------------------------------
    # Set Velocity
    # ---------------------------------

    def set_velocity(self, velocity):

        self.velocity = velocity.copy()

    # ---------------------------------
    # Set Position
    # ---------------------------------

    def set_position(self, position):

        self.position = position.copy()

    # ---------------------------------
    # Add Velocity
    # ---------------------------------

    def add_velocity(self, velocity):

        self.velocity += velocity

    # ---------------------------------
    # Add Acceleration
    # ---------------------------------

    def add_acceleration(self, acceleration):

        self.acceleration += acceleration

    # ---------------------------------
    # Update Physics
    # ---------------------------------

    def update(self, dt):

        if not self.active:
            return

        self.life += dt

        if (
            self.max_life > 0
            and self.life >= self.max_life
        ):

            self.alive = False
            self.stop()
            return

        acceleration = self.acceleration
        velocity = self.velocity
        position = self.position

        acceleration += self.gravity

        velocity += acceleration * dt

        velocity = velocity.clamp(self.max_speed)

        position += velocity * dt

        velocity *= self.drag

        self.velocity = velocity
        self.position = position
        self.acceleration = Vector2()

    # ---------------------------------
    # Screen Bounce
    # ---------------------------------

    def bounce_screen(
        self,
        width,
        height
    ):

        if self.position.x < self.radius:

            self.position.x = self.radius

            self.velocity.x *= -self.bounce

        elif self.position.x > width - self.radius:

            self.position.x = width - self.radius

            self.velocity.x *= -self.bounce

        if self.position.y < self.radius:

            self.position.y = self.radius

            self.velocity.y *= -self.bounce

        elif self.position.y > height - self.radius:

            self.position.y = height - self.radius

            self.velocity.y *= -self.bounce

    # ---------------------------------
    # Distance
    # ---------------------------------

    def distance_to(self, other):

        position = self.position
        other_position = other.position

        return position.distance_to(other_position)

    # ---------------------------------
    # Collision
    # ---------------------------------

    def intersects(self, other):

        distance = self.distance_to(other)
        radius = self.radius + other.radius

        return distance <= radius

    # ---------------------------------
    # Destroy
    # ---------------------------------

    def destroy(self):

        if not self.active:
            return

        self.alive = False
        self.active = False

    # ---------------------------------
    # Draw
    # ---------------------------------

    def draw(self, frame):

        pass

    # ---------------------------------
    # Status
    # ---------------------------------

    def is_alive(self):

        return self.alive

    def is_active(self):

        return self.active