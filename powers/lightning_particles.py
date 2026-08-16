from powers.lightning_particle import LightningParticle


class LightningParticles:

    def __init__(self):

        self.particles = []

    # ---------------------------------
    # Emit
    # ---------------------------------

    def emit(
        self,
        position,
        count=8
    ):

        for _ in range(count):

            particle = LightningParticle()

            particle.start(position)

            self.particles.append(
                particle
            )

    # ---------------------------------
    # Update
    # ---------------------------------

    def update(
        self,
        dt
    ):

        for particle in self.particles[:]:

            particle.update(dt)

            if not particle.is_alive():

                self.particles.remove(
                    particle
                )

    # ---------------------------------
    # Draw
    # ---------------------------------

    def draw(
        self,
        frame
    ):

        for particle in self.particles:

            particle.draw(frame)

    # ---------------------------------
    # Clear
    # ---------------------------------

    def clear(self):

        self.particles.clear()

    # ---------------------------------
    # Alive Count
    # ---------------------------------

    def alive_count(self):

        return len(self.particles)

    # ---------------------------------
    # Is Empty
    # ---------------------------------

    def is_empty(self):

        return len(self.particles) == 0