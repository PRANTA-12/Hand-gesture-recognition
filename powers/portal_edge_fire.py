import math
import random
import cv2


class PortalEdgeFire:

    def __init__(self):

        self.flames = []

        self.colors = [

            (0, 140, 255),
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

        self.flames.clear()

    # ---------------------------------
    # Reset
    # ---------------------------------

    def reset(self):

        self.flames.clear()

        for _ in range(40):

            self.flames.append({

                "angle": random.uniform(0, 360),

                "height": random.randint(10, 25),

                "width": random.randint(3, 6),

                "offset": random.randint(-5, 5),

                "speed": random.uniform(40, 90),

                "flicker": random.uniform(0, math.pi * 2)

            })

    # ---------------------------------
    # Update
    # ---------------------------------

    def update(self, dt):

        for flame in self.flames:

            flame["angle"] += flame["speed"] * dt

            flame["flicker"] += dt * random.uniform(4, 8)

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

        for flame in self.flames:

            angle = math.radians(flame["angle"])

            pulse = 0.8 + 0.3 * math.sin(

                flame["flicker"]

            )

            base_r = radius + flame["offset"]

            tip_r = base_r + flame["height"] * pulse

            x1 = int(

                cx + math.cos(angle) * base_r

            )

            y1 = int(

                cy + math.sin(angle) * base_r

            )

            x2 = int(

                cx + math.cos(angle) * tip_r

            )

            y2 = int(

                cy + math.sin(angle) * tip_r

            )

            color = random.choice(

                self.colors

            )

            cv2.line(

                overlay,

                (x1, y1),

                (x2, y2),

                color,

                flame["width"],

                cv2.LINE_AA

            )

            cv2.circle(

                overlay,

                (x2, y2),

                2,

                (255, 255, 255),

                -1,

                cv2.LINE_AA

            )

        cv2.addWeighted(

            overlay,

            0.50,

            frame,

            0.50,

            0,

            frame

        )

    # ---------------------------------
    # Count
    # ---------------------------------

    def count(self):

        return len(self.flames)