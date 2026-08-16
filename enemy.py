import cv2
import random


class Enemy:

    def __init__(self):

        self.x = random.randint(100, 1100)
        self.y = random.randint(100, 600)

        self.radius = 30
        self.health = 100
        self.alive = True

    def draw(self, frame):

        if not self.alive:
            return

        # Enemy body
        # cv2.circle(
        #     frame,
        #     (self.x, self.y),
        #     self.radius,
        #     (0, 0, 255),
        #     -1
        # )

        # Health bar background
        # cv2.rectangle(
        #     frame,
        #     (self.x - 30, self.y - 45),
        #     (self.x + 30, self.y - 38),
        #     (60, 60, 60),
        #     -1
        # )

        # Health bar
        width = int(60 * self.health / 100)

        # cv2.rectangle(
        #     frame,
        #     (self.x - 30, self.y - 45),
        #     (self.x - 30 + width, self.y - 38),
        #     (0, 255, 0),
        #     -1
        # )