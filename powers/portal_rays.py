import math
import random
import cv2


class PortalRays:

    def __init__(self):

        self.rotation = 0

        self.rays = []

        self.colors = [

            (0, 180, 255),
            (50, 220, 255),
            (120, 255, 255),
            (255, 255, 255)

        ]

        self.reset()

    # ---------------------------------
    # Start
    # ---------------------------------

    def start(self, center):

        self.reset()

    # ---------------------------------
    # Stop
    # ---------------------------------

    def stop(self):

        pass

    # ---------------------------------
    # Clear
    # ---------------------------------

    def clear(self):

        self.rays.clear()

    # ---------------------------------
    # Reset
    # ---------------------------------

    def reset(self):

        self.rotation = 0

        self.rays.clear()

        for _ in range(24):

            self.rays.append({

                "angle": random.uniform(0, 360),

                "length": random.randint(25, 60),

                "width": random.randint(1, 3),

                "speed": random.uniform(15, 40),

                "alpha": random.uniform(0.4, 1.0),

                "pulse": random.uniform(0, math.pi * 2)

            })

    # ---------------------------------
    # Update
    # ---------------------------------

    def update(self, dt):

        self.rotation += 20 * dt

        for ray in self.rays:

            ray["angle"] += ray["speed"] * dt

            ray["pulse"] += dt * 4

    # ---------------------------------
    # Draw
    # ---------------------------------

    def draw(
        self,
        frame,
        center=None,
        radius=None
    ):

        if center is None or radius is None:
            return

        if radius < 20:
            return

        overlay = frame.copy()

        cx, cy = center

        for ray in self.rays:

            angle = math.radians(

                ray["angle"] + self.rotation

            )

            start_r = radius - 8

            pulse = 0.85 + 0.15 * math.sin(

                ray["pulse"]

            )

            end_r = start_r + ray["length"] * pulse

            x1 = int(

                cx + math.cos(angle) * start_r

            )

            y1 = int(

                cy + math.sin(angle) * start_r

            )

            x2 = int(

                cx + math.cos(angle) * end_r

            )

            y2 = int(

                cy + math.sin(angle) * end_r

            )

            color = random.choice(

                self.colors

            )

            cv2.line(

                overlay,

                (x1, y1),

                (x2, y2),

                color,

                ray["width"],

                cv2.LINE_AA

            )

        cv2.addWeighted(

            overlay,

            0.45,

            frame,

            0.55,

            0,

            frame

        )

    # ---------------------------------
    # Count
    # ---------------------------------

    def count(self):

        return len(self.rays)