import cv2
import random
from particle_pool import ParticlePool


class Smoke:

    def __init__(self):
        self.particle_pool = ParticlePool(200)
        self.smoke = []

    def emit(self, center):

        x, y = center

        particle = self.particle_pool.get()

        if particle is None:
            return

        particle.x = x
        particle.y = y

        # Use vx/vy instead of dx/dy
        particle.vx = random.uniform(-1.5, 1.5)
        particle.vy = random.uniform(-2.5, -0.5)

        # Reuse existing fields
        particle.size = random.randint(6, 12)
        particle.life = random.randint(20, 40)

        self.smoke.append(particle)

    def update(self, frame, dt):

        alive = []

        for s in self.smoke:

            s["x"] += s["dx"] * dt * 60
            s["y"] += s["dy"] * dt * 60

            s["radius"] += 12 * dt
            s.life -= 1

            if s.life > 0:

                overlay = frame.copy()

                cv2.circle(
                    overlay,
                    (int(s.x), int(s.y)),
                    int(s.size),
                    (180, 180, 180),
                    -1,
                    lineType=cv2.LINE_AA
                )

                cv2.addWeighted(
                    overlay,
                    0.15,
                    frame,
                    0.85,
                    0,
                    frame
                )

                alive.append(s)

            else:
                self.particle_pool.release(s)

        self.smoke = alive