class ObjectPool:

    def __init__(self, particle_class, size):

        self.pool = [
            particle_class()
            for _ in range(size)
        ]

    # ---------------------------------
    # Get Free Object
    # ---------------------------------

    def get(self):

        for obj in self.pool:

            if not obj.is_alive():
                return obj

        return None

    # ---------------------------------
    # Active Objects
    # ---------------------------------

    def active_objects(self):

        active = []

        for obj in self.pool:

            if obj.is_alive():
                active.append(obj)

        return active

    # ---------------------------------
    # Active Count
    # ---------------------------------

    def active_count(self):

        count = 0

        for obj in self.pool:

            if obj.is_alive():
                count += 1

        return count

    # ---------------------------------
    # Reset Pool
    # ---------------------------------

    def reset(self):

        for obj in self.pool:

            obj.reset()

    # ---------------------------------
    # Clear Pool
    # ---------------------------------

    def clear(self):

        for obj in self.pool:

            obj.destroy()

    # ---------------------------------
    # Pool Size
    # ---------------------------------

    def size(self):

        return len(self.pool)