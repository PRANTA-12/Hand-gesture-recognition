class GestureController:

    def __init__(
        self,
        effects,
        energy_ball,
        particle_engine,
        sparks,
        smoke,
        cooldown,
        energy,
    ):
        self.effects = effects
        self.energy_ball = energy_ball
        self.particle_engine = particle_engine
        self.sparks = sparks
        self.smoke = smoke
        self.cooldown = cooldown
        self.energy = energy

    def handle(self, name, frame, position, landmarks, previous_gesture):

        if (
            name == "PINCH"
            and previous_gesture != "PINCH"
            and self.cooldown.ready("PINCH")
            and self.energy.use(5)
        ):
            self.cooldown.trigger("PINCH")

            self.effects.draw_glow(frame, position)
            self.effects.draw_rotating_ring(frame, position)

            self.energy_ball.draw(frame, position)

            self.particle_engine.emit(position)
            self.sparks.emit(position)
            self.smoke.emit(position)