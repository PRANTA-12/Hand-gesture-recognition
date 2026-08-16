import math


class PortalController:

    def __init__(self, portal, sound_manager=None):

        self.portal = portal

        self.sound_manager = sound_manager

        self.opened = False

        self.center = (0, 0)

        self.open_distance = 180
        self.close_distance = 120

    def update(self, left_hand, right_hand):

        # Need both hands
        if left_hand is None or right_hand is None:

            if self.opened:
                self.close()

            return

        # Palm landmark (MediaPipe landmark 0)
        lx = left_hand[0][1]
        ly = left_hand[0][2]

        rx = right_hand[0][1]
        ry = right_hand[0][2]

        distance = math.hypot(
            rx - lx,
            ry - ly
        )

        # Portal center = midpoint of both palms
        cx = int((lx + rx) / 2)
        cy = int((ly + ry) / 2)

        self.center = (cx, cy)

        # Open portal
        if (not self.opened) and distance >= self.open_distance:

            self.open()

        # Close portal
        elif self.opened and distance <= self.close_distance:

            self.close()

        # Move portal
        if self.opened:

            self.move(self.center)

    def open(self):

        self.portal.start(self.center)

        self.opened = True

        if self.sound_manager:
            self.sound_manager.play_open()
            self.sound_manager.play_loop()

    def close(self):

        self.portal.stop()

        self.opened = False

        if self.sound_manager:
            self.sound_manager.stop_loop()
            self.sound_manager.play_close()

    def move(self, center):

        self.portal.move(center)

    def is_open(self):

        return self.opened
