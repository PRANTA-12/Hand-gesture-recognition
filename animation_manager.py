class AnimationManager:

    def __init__(self):
        self.animations = {}

    # -------------------------
    # Register
    # -------------------------

    def register(self, name, animation):

        self.animations[name] = animation

    # -------------------------
    # Start
    # -------------------------

    def start(self, name, position, angle=None):

        animation = self.animations.get(name)

        if animation is None:
            return

        if angle is None:
            animation.start(position)
        else:
            animation.start(position, angle)

    # -------------------------
    # Play
    # -------------------------

    def play(self, name, position, angle=None):

        animation = self.animations.get(name)

        if animation is None:
            return

        # --------------------------------
        # Stop other animations
        # --------------------------------

        for animation_name, other_animation in self.animations.items():

            if animation_name != name:

                if getattr(other_animation, "active", False):

                    if hasattr(other_animation, "stop"):
                        other_animation.stop()

        # --------------------------------
        # Start ONLY if not already active
        # --------------------------------

        if not getattr(animation, "active", False):

            if angle is None:
                animation.start(position)
            else:
                animation.start(position, angle)

            return

        # --------------------------------
        # Already active
        # DON'T restart
        # Just move it
        # --------------------------------

        if hasattr(animation, "move"):

            animation.move(position)

        # --------------------------------
        # Update angle if supported
        # --------------------------------

        if angle is not None and hasattr(animation, "set_angle"):

            animation.set_angle(angle)

    # -------------------------
    # Stop
    # -------------------------

    def stop(self, name):

        animation = self.animations.get(name)

        if animation:
            animation.stop()

    # -------------------------
    # Update
    # -------------------------

    def update(self, frame, dt):

        for animation in self.animations.values():

            if getattr(animation, "active", False):

                animation.update(frame, dt)

    # -------------------------
    # Move
    # -------------------------

    def move(self, name, position):

        animation = self.animations.get(name)

        if animation and hasattr(animation, "move"):

            animation.move(position)

    # -------------------------
    # Stop All
    # -------------------------

    def stop_all(self):

        for animation in self.animations.values():

            animation.stop()

    # -------------------------
    # Reset
    # -------------------------

    def reset(self):

        for animation in self.animations.values():

            if hasattr(animation, "reset"):

                animation.reset()

    # -------------------------
    # Clear
    # -------------------------

    def clear(self):

        self.animations.clear()

    # -------------------------
    # Count
    # -------------------------

    def count(self):

        return len(self.animations)

    # -------------------------
    # Is Active
    # -------------------------

    def is_active(self, name):

        animation = self.animations.get(name)

        return bool(animation and getattr(animation, "active", False))