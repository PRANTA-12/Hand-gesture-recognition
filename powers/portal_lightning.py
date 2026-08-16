import math
import random

from animation_utils import AnimationUtils


class PortalLightning:

    def __init__(self):

        self.bolts = []

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

        self.bolts.clear()

    # ---------------------------------
    # Reset
    # ---------------------------------

    def reset(self):

        self.bolts.clear()

    # ---------------------------------
    # Emit
    # ---------------------------------

    def emit(self, center, radius):

        if center is None or radius is None:
            return

        if random.random() > 0.35:
            return

        cx, cy = center

        start_angle = random.uniform(0, math.pi * 2)
        end_angle = start_angle + random.uniform(-0.6, 0.6)

        r1 = radius - random.randint(5, 15)
        r2 = radius + random.randint(5, 15)

        x1 = int(cx + r1 * math.cos(start_angle))
        y1 = int(cy + r1 * math.sin(start_angle))

        x2 = int(cx + r2 * math.cos(end_angle))
        y2 = int(cy + r2 * math.sin(end_angle))

        self.bolts.append({

            "start": (x1, y1),

            "end": (x2, y2),

            "life": 6

        })

    # ---------------------------------
    # Update
    # ---------------------------------

    def update(self, dt):

        alive = []

        for bolt in self.bolts:

            bolt["life"] -= 1

            if bolt["life"] > 0:

                alive.append(bolt)

        self.bolts = alive

    # ---------------------------------
    # Draw
    # ---------------------------------

    def draw(
        self,
        frame,
        center=None,
        radius=None
    ):

        if not self.bolts:
            return

        for bolt in self.bolts:

            sx, sy = bolt["start"]
            ex, ey = bolt["end"]

            points = []

            segments = 8

            for i in range(segments + 1):

                t = i / segments

                x = sx + (ex - sx) * t
                y = sy + (ey - sy) * t

                if 0 < i < segments:

                    x += random.randint(-10, 10)
                    y += random.randint(-10, 10)

                points.append((int(x), int(y)))

            for i in range(len(points) - 1):

                AnimationUtils.beam(

                    frame,

                    points[i],

                    points[i + 1],

                    (255, 255, 255),

                    4

                )

                AnimationUtils.beam(

                    frame,

                    points[i],

                    points[i + 1],

                    (0, 220, 255),

                    2

                )

                AnimationUtils.glow_circle(

                    frame,

                    points[i],

                    3,

                    (255, 255, 255)

                )

    # ---------------------------------
    # Count
    # ---------------------------------

    def count(self):

        return len(self.bolts)