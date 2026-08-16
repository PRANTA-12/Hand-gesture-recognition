"""
Base Power Class
----------------
Every power (Portal, Rasengan, Fireball, etc.)
inherits from this class.

Benefits:
- Common active/inactive state
- Common start/stop methods
- Easy performance optimization
- Cleaner architecture
"""

class BasePower:

    def __init__(self):

        # Whether the effect is currently active
        self.active = False

        # Optional pause state
        self.paused = False

    # ---------------------------------
    # Start Effect
    # ---------------------------------

    def start(self):

        self.active = True
        self.paused = False

    # ---------------------------------
    # Stop Effect
    # ---------------------------------

    def stop(self):

        self.active = False

    # ---------------------------------
    # Pause Effect
    # ---------------------------------

    def pause(self):

        self.paused = True

    # ---------------------------------
    # Resume Effect
    # ---------------------------------

    def resume(self):

        if self.active:
            self.paused = False

    # ---------------------------------
    # Reset
    # ---------------------------------

    def reset(self):

        self.active = False
        self.paused = False

    # ---------------------------------
    # State Checks
    # ---------------------------------

    def is_active(self):

        return self.active

    def is_paused(self):

        return self.paused

    # ---------------------------------
    # Update
    # ---------------------------------

    def update(self, *args, **kwargs):

        if not self.active:
            return

        if self.paused:
            return

    # ---------------------------------
    # Draw
    # ---------------------------------

    def draw(self, *args, **kwargs):

        if not self.active:
            return