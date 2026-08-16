class PhysicsEngine:

    def __init__(self):

        self.bodies = []

        self.gravity_enabled = False

        self.gravity = (0, 0)

    # ---------------------------------
    # Register Body
    # ---------------------------------

    def add(self, body):

        if body not in self.bodies:
            self.bodies.append(body)

    # ---------------------------------
    # Remove Body
    # ---------------------------------

    def remove(self, body):

        if body in self.bodies:
            self.bodies.remove(body)

    # ---------------------------------
    # Remove All Bodies
    # ---------------------------------

    def clear(self):

        self.bodies.clear()

    # ---------------------------------
    # Enable Gravity
    # ---------------------------------

    def enable_gravity(self, gx=0, gy=500):

        self.gravity_enabled = True

        self.gravity = (gx, gy)

    # ---------------------------------
    # Disable Gravity
    # ---------------------------------

    def disable_gravity(self):

        self.gravity_enabled = False

    # ---------------------------------
    # Update Physics
    # ---------------------------------

    def update(self, dt):

        alive_bodies = []

        gravity_enabled = self.gravity_enabled
        gx, gy = self.gravity

        for body in self.bodies:

            if not body.is_alive():
                continue

            if gravity_enabled:
                body.gravity.x = gx
                body.gravity.y = gy

            body.update(dt)

            alive_bodies.append(body)

        self.bodies = alive_bodies

    # ---------------------------------
    # Screen Collision
    # ---------------------------------

    def bounce_screen(self, width, height):

        bodies = self.bodies

        for body in bodies:
            body.bounce_screen(width, height)

    # ---------------------------------
    # Draw
    # ---------------------------------

    def draw(self, frame):

        bodies = self.bodies

        for body in bodies:
            body.draw(frame)

    # ---------------------------------
    # Total Bodies
    # ---------------------------------

    def count(self):

        return len(self.bodies)

    # ---------------------------------
    # Get Bodies
    # ---------------------------------

    def get_bodies(self):

        return self.bodies

    # ---------------------------------
    # Reset
    # ---------------------------------

    def reset(self):

        bodies = self.bodies

        for body in bodies:
            body.reset()

    # ---------------------------------
    # Destroy All
    # ---------------------------------

    def destroy_all(self):

        bodies = self.bodies

        for body in bodies:
            body.destroy()

        bodies.clear()