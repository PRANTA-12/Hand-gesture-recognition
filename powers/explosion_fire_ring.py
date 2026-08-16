from animation_utils import AnimationUtils


class ExplosionFireRing:

    def __init__(self):

        self.active = False

        self.x = 0
        self.y = 0

        self.radius = 20.0
        self.max_radius = 220.0

        self.life = 0.0
        self.max_life = 0.45

        self.speed = 220.0

    # ---------------------------------
    # Start
    # ---------------------------------

    def start(self, position):

        self.x = position[0]
        self.y = position[1]

        self.radius = 20.0

        self.life = self.max_life

        self.active = True

    # ---------------------------------
    # Update
    # ---------------------------------

    def update(self, dt):

        if not self.active:
            return

        self.radius += self.speed * dt

        self.life -= dt

        if self.life <= 0:

            self.destroy()

    # ---------------------------------
    # Draw
    # ---------------------------------

    def draw(self, frame):

        if not self.active:
            return
        position = (
            int(self.x),
            int(self.y)
        )

        radius = int(self.radius)
        outer_radius = radius + 6

        progress = self.life / self.max_life

        thickness = max(1, int(4 * progress))
        outer_thickness = max(1, thickness - 1)

        AnimationUtils.ring(
            frame,
            position,
            radius,
            (0,180,255),
            thickness
        )

        AnimationUtils.ring(
            frame,
            position,
            outer_radius,
            (0,80,255),
            outer_thickness
        )

    # ---------------------------------
    # Alive
    # ---------------------------------

    def is_alive(self):

        return self.active

    # ---------------------------------
    # Reset
    # ---------------------------------

    def reset(self):

        self.active = False

        self.radius = 20

        self.life = 0

    # ---------------------------------
    # Destroy
    # ---------------------------------

    def destroy(self):

        self.active = False