class BaseAnimation:
    """
    Base class for all animations.

    Every animation should inherit from this class so they all
    expose the same interface to AnimationManager.
    """

    def __init__(self):

        self.active = False

    # ---------------------------------
    # Start Animation
    # ---------------------------------

    def start(self, *args, **kwargs):

        self.active = True

    # ---------------------------------
    # Stop Animation
    # ---------------------------------

    def stop(self):

        self.active = False

    # ---------------------------------
    # Reset Animation
    # ---------------------------------

    def reset(self):

        pass

    # ---------------------------------
    # Clear Animation
    # ---------------------------------

    def clear(self):

        pass

    # ---------------------------------
    # Emit Particles / Objects
    # ---------------------------------

    def emit(self, *args, **kwargs):

        pass

    # ---------------------------------
    # Update Animation
    # ---------------------------------

    def update(self, dt):

        pass

    # ---------------------------------
    # Draw Animation
    # ---------------------------------

    def draw(
        self,
        frame,
        center=None,
        radius=None
    ):

        pass

    # ---------------------------------
    # Active State
    # ---------------------------------

    def is_active(self):

        return self.active

    # ---------------------------------
    # Enable / Disable
    # ---------------------------------

    def set_active(self, value):

        self.active = bool(value)

    # ---------------------------------
    # String Representation
    # ---------------------------------

    def __repr__(self):

        return f"{self.__class__.__name__}(active={self.active})"