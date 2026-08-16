class AnimationManager:

    def __init__(self):

        self.effects = []

    # -----------------------------
    # Register
    # -----------------------------

    def register(
        self,
        effect,
        max_count=None,
        particle_attr=None
    ):

        self.effects.append({

            "effect": effect,

            "max_count": max_count,

            "particle_attr": particle_attr

        })

    # -----------------------------
    # Remove
    # -----------------------------

    def unregister(self, effect):

        self.effects = [

            item

            for item in self.effects

            if item["effect"] != effect

        ]

    # -----------------------------
    # Remove all
    # -----------------------------

    def clear(self):

        for item in self.effects:

            effect = item["effect"]

            if hasattr(effect, "clear"):

                effect.clear()

    # -----------------------------
    # Reset all
    # -----------------------------

    def reset(self):

        for item in self.effects:

            effect = item["effect"]

            if hasattr(effect, "reset"):

                effect.reset()

    # -----------------------------
    # Emit
    # -----------------------------

    def emit(
        self,
        center,
        radius
    ):

        for item in self.effects:

            effect = item["effect"]

            limit = item["max_count"]

            attr = item["particle_attr"]

            if limit is not None and attr is not None:

                container = getattr(
                    effect,
                    attr,
                    None
                )

                if container is not None:

                    if len(container) >= limit:
                        continue

            if hasattr(effect, "emit"):

                try:

                    effect.emit(
                        center,
                        radius
                    )

                except TypeError:

                    pass

    # -----------------------------
    # Update all
    # -----------------------------

    def update(self, *args):

        frame = None
        dt = None

        if len(args) == 2:
            frame, dt = args

        elif len(args) == 1:
            dt = args[0]

        for item in self.effects:

            effect = item["effect"]

            if hasattr(effect, "is_active"):

                if not effect.is_active():
                    continue

            if hasattr(effect, "update"):

                try:

                    if frame is not None:
                        effect.update(frame, dt)
                    else:
                        effect.update(dt)

                except TypeError:

                    try:
                        effect.update(frame)

                    except TypeError:

                        try:
                            effect.update()

                        except TypeError:
                            pass
    # -----------------------------
    # Draw all
    # -----------------------------

    def draw(
        self,
        frame,
        center=None,
        radius=None
    ):

        for item in self.effects:

            effect = item["effect"]

            if hasattr(effect, "is_active"):

                if not effect.is_active():
                    continue

            if hasattr(effect, "draw"):

                try:

                    if center is not None and radius is not None:

                        effect.draw(
                            frame,
                            center,
                            radius
                        )

                    else:

                        effect.draw(frame)

                except TypeError:

                    pass

    # -----------------------------
    # Count
    # -----------------------------

    def count(self):

        return len(self.effects)

    # -----------------------------
    # Get Effect
    # -----------------------------

    def get(self, index):

        if 0 <= index < len(self.effects):

            return self.effects[index]["effect"]

        return None

    # -----------------------------
    # Iterate
    # -----------------------------

    def __iter__(self):

        for item in self.effects:

            yield item["effect"]