import time


class PortalTeleport:

    def __init__(self):

        self.entry_center = (0, 0)
        self.exit_center = (0, 0)

        self.radius = 0

        self.cooldown = 1.0
        self.last_teleport = 0.0

    # ---------------------------------
    # Update Portal
    # ---------------------------------

    def update(
        self,
        center,
        radius
    ):

        self.entry_center = center
        self.radius = radius

    # ---------------------------------
    # Set Exit Portal
    # ---------------------------------

    def set_exit(
        self,
        center
    ):

        self.exit_center = center

    # ---------------------------------
    # Can Teleport
    # ---------------------------------

    def can_teleport(self):

        return (
            time.time() - self.last_teleport
        ) >= self.cooldown

    # ---------------------------------
    # Teleport Point
    # ---------------------------------

    def teleport_point(
        self,
        point
    ):

        if not self.can_teleport():

            return point

        px, py = point
        cx, cy = self.entry_center

        dx = px - cx
        dy = py - cy

        if (dx * dx + dy * dy) <= (self.radius * self.radius):

            self.last_teleport = time.time()

            ex, ey = self.exit_center

            return (
                ex + dx,
                ey + dy
            )

        return point

    # ---------------------------------
    # Reset
    # ---------------------------------

    def reset(self):

        self.entry_center = (0, 0)
        self.exit_center = (0, 0)

        self.radius = 0

        self.last_teleport = 0.0