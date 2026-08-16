from animation_utils import AnimationUtils


class ExplosionLight:

    def __init__(self):

        self.active = False

        self.x = 0
        self.y = 0

        self.radius = 180.0
        self.max_radius = 180.0

        self.life = 0.0
        self.max_life = 0.35

    # ---------------------------------
    # Start
    # ---------------------------------

    def start(self, position):

        self.x = position[0]
        self.y = position[1]

        self.radius = self.max_radius

        self.life = self.max_life

        self.active = True

    # ---------------------------------
    # Update
    # ---------------------------------

    def update(self, dt):

        if not self.active:
            return

        self.life -= dt
        expired = self.life <= 0

        if expired:

            self.life = 0
            self.active = False
            return

        progress = self.life / self.max_life

        self.radius = self.max_radius * progress

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
        radius = max(1, int(self.radius))

        AnimationUtils.dynamic_light(
            frame,
             position,
            radius=radius,
            color=(0, 180, 255),
            alpha=0.35
        )

        AnimationUtils.glow_circle(
            frame,
            position,
            radius,
            color=(0, 180, 255)
        )

    # ---------------------------------
    # Reset
    # ---------------------------------

    def reset(self):

        self.active = False

        self.radius = 0

        self.life = 0

    # ---------------------------------
    # Is Active
    # ---------------------------------

    def is_active(self):

        return self.active