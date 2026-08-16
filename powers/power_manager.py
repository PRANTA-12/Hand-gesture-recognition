class PowerManager:

    def __init__(self):

        self.powers = {}
        self.active_powers = set()

    # --------------------------------
    # Register Power
    # --------------------------------

    def register(self, name, power):

        self.powers[name] = power

    # --------------------------------
    # Get Power
    # --------------------------------

    def get(self, name):

        return self.powers.get(name)

    # --------------------------------
    # Activate Power
    # --------------------------------

    def activate(self, name):

        if name not in self.powers:
            return

        self.active_powers.add(name)

    # --------------------------------
    # Stop One Power
    # --------------------------------

    def stop(self, name):

        power = self.powers.get(name)

        if power is None:
            return

        if hasattr(power, "stop"):
            power.stop()

        self.active_powers.discard(name)

    # --------------------------------
    # Stop All Powers
    # --------------------------------

    def stop_all(self):

        for name in list(self.active_powers):

            power = self.powers.get(name)

            if power and hasattr(power, "stop"):
                power.stop()

        self.active_powers.clear()

    # --------------------------------
    # Is Active
    # --------------------------------

    def is_active(self, name):

        return name in self.active_powers

    # --------------------------------
    # Current Power
    # --------------------------------

    def current_power(self):

        return list(self.active_powers)

    # --------------------------------
    # Update
    # --------------------------------

    def update(self, frame, dt):

        for name in list(self.active_powers):

            power = self.powers.get(name)

            if power is None:
                continue

            if hasattr(power, "is_active"):

                if not power.is_active():
                    continue

            if hasattr(power, "update"):

                try:
                    power.update(frame, dt)

                except TypeError:

                    try:
                        power.update(dt)

                    except TypeError:

                        try:
                            power.update(frame)

                        except TypeError:
                            pass

    # --------------------------------
    # Draw
    # --------------------------------

    def draw(self, frame):

        for name in list(self.active_powers):

            power = self.powers.get(name)

            if power is None:
                continue

            if hasattr(power, "is_active"):

                if not power.is_active():
                    continue

            if hasattr(power, "draw"):

                try:
                    power.draw(frame)

                except TypeError:
                    pass        

        

    # --------------------------------
    # Reset
    # --------------------------------

    def reset(self):

        for power in self.powers.values():

            if hasattr(power, "reset"):
                power.reset()

        self.active_powers.clear()

    # --------------------------------
    # Clear
    # --------------------------------

    def clear(self):

        self.stop_all()

        self.powers.clear()

    # --------------------------------
    # Count
    # --------------------------------

    def count(self):

        return len(self.powers)

    # --------------------------------
    # Names
    # --------------------------------

    def names(self):

        return list(self.powers.keys())

    # --------------------------------
    # Iterator
    # --------------------------------

    def __iter__(self):

        return iter(self.powers.values())