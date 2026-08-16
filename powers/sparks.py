import cv2
import random
from particle_pool import ParticlePool


class Sparks:

    def __init__(self):
        self.particle_pool = ParticlePool(200)
        self.sparks = []

    def emit(self, center):

        x, y = center

        for _ in range(3):

            particle = self.particle_pool.get()

            if particle is None:
                continue

            particle.x = x
            particle.y = y

            particle.vx = random.uniform(-5, 5)
            particle.vy = random.uniform(-5, 5)

            particle.life = random.randint(8, 15)
            particle.size = 2
            particle.color = (0, 255, 255)

            self.sparks.append(particle)

    def update(self, frame, dt):

        alive = []

        for spark in self.sparks:

            spark["x"] += spark["dx"] * dt * 60
            spark["y"] += spark["dy"] * dt * 60

            spark.life -= 1

            if spark.life > 0:

                cv2.circle(
                    frame,
                    (int(spark.x), int(spark.y)),
                    spark.size,
                    spark.color,
                    -1,
                    lineType=cv2.LINE_AA
                )

                alive.append(spark)

            else:
                self.particle_pool.release(spark)

        self.sparks = alive