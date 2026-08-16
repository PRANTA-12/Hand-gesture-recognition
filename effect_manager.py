class EffectManager:

    def __init__(self):
        self.effects = []

    def register(self, effect):

        if effect not in self.effects:
            self.effects.append(effect)

    def update(self, frame, dt):

        effects = self.effects

        for effect in effects:

            if hasattr(effect, "active") and not effect.active:
                continue

            effect.update(frame, dt)

    def reset(self):

        for effect in self.effects:

            if hasattr(effect, "reset"):
                effect.reset()

    def clear(self):

        self.effects.clear()

    def count(self):

        return len(self.effects)