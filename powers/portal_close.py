import math


class PortalClose:

    def __init__(self):

        self.active = False

        self.radius = 100
        self.alpha = 1.0

        self.close_speed = 220.0
        self.fade_speed = 2.8

    def start(self, current_radius):

        self.active = True

        self.radius = current_radius
        self.alpha = 1.0

    def stop(self):

        self.active = False

    def update(self, dt):

        if not self.active:
            return

        # Shrink portal
        self.radius -= self.close_speed * dt

        if self.radius < 0:
            self.radius = 0

        # Fade glow
        self.alpha -= self.fade_speed * dt

        if self.alpha < 0:
            self.alpha = 0

        # Animation finished
        if self.radius <= 0 or self.alpha <= 0:
            self.active = False

    def is_finished(self):

        return not self.active

    def get_radius(self):

        return self.radius

    def get_alpha(self):

        return self.alpha