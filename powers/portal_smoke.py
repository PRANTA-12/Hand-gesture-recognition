import math
import random
import cv2


class PortalSmoke:

    def __init__(self):

        self.particles = []

        self.colors = [

            (30, 80, 255),
            (40, 120, 255),
            (60, 150, 255),
            (80, 170, 255)

        ]

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

        self.particles.clear()

    # ---------------------------------
    # Reset
    # ---------------------------------

    def reset(self):

        self.particles.clear()

    # ---------------------------------
    # Emit
    # ---------------------------------

    def emit(self, center, radius):

        if radius is None or radius < 20:
            return

        for _ in range(random.randint(2, 4)):

            angle = random.uniform(0, math.pi * 2)

            spawn_radius = radius + random.randint(-6, 6)

            x = center[0] + math.cos(angle) * spawn_radius
            y = center[1] + math.sin(angle) * spawn_radius

            speed = random.uniform(8, 20)

            vx = math.cos(angle) * speed
            vy = math.sin(angle) * speed

            max_life = random.uniform(0.8, 1.4)

            self.particles.append({

                "x": x,
                "y": y,

                "vx": vx,
                "vy": vy,

                "life": max_life,
                "max_life": max_life,

                "size": random.randint(8, 16),

                "grow": random.uniform(6, 12),

                "color": random.choice(self.colors)

            })

    # ---------------------------------
    # Update
    # ---------------------------------

    def update(self, dt):

        alive = []

        for p in self.particles:

            p["life"] -= dt

            if p["life"] <= 0:
                continue

            p["x"] += p["vx"] * dt
            p["y"] += p["vy"] * dt

            p["vx"] *= 0.98
            p["vy"] *= 0.98

            p["size"] += p["grow"] * dt

            alive.append(p)

        self.particles = alive

    # ---------------------------------
    # Draw
    # ---------------------------------

    def draw(
        self,
        frame,
        center=None,
        radius=None
    ):

        if not self.particles:
            return

        overlay = frame.copy()

        for p in self.particles:

            alpha = p["life"] / p["max_life"]

            color = (

                int(p["color"][0] * alpha),

                int(p["color"][1] * alpha),

                int(p["color"][2] * alpha)

            )

            cv2.circle(

                overlay,

                (int(p["x"]), int(p["y"])),

                int(p["size"]),

                color,

                -1,

                cv2.LINE_AA

            )

        cv2.addWeighted(

            overlay,

            0.28,

            frame,

            0.72,

            0,

            frame

        )