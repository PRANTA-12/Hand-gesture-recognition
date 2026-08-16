import math


class CollisionManager:

    def __init__(self):

        self.objects = []

    # ---------------------------------
    # Register Object
    # ---------------------------------

    def add(self, obj):

        if obj not in self.objects:
            self.objects.append(obj)

    # ---------------------------------
    # Remove Object
    # ---------------------------------

    def remove(self, obj):

        if obj in self.objects:
            self.objects.remove(obj)

    # ---------------------------------
    # Clear
    # ---------------------------------

    def clear(self):

        self.objects.clear()

    # ---------------------------------
    # Update
    # ---------------------------------

    def update(self):

        total = len(self.objects)

        for i in range(total):

            a = self.objects[i]

            if not getattr(a, "active", True):
                continue

            for j in range(i + 1, total):

                b = self.objects[j]

                if not getattr(b, "active", True):
                    continue

                if self.check_collision(a, b):

                    self.resolve_collision(a, b)

    # ---------------------------------
    # Circle Collision
    # ---------------------------------

    def check_collision(self, a, b):

        ax = a.position.x
        ay = a.position.y

        bx = b.position.x
        by = b.position.y

        dx = ax - bx
        dy = ay - by

        distance = math.sqrt(
            dx * dx +
            dy * dy
        )

        return distance <= (
            a.radius +
            b.radius
        )

    # ---------------------------------
    # Resolve
    # ---------------------------------

    def resolve_collision(self, a, b):

        if hasattr(a, "on_collision"):
            a.on_collision(b)

        if hasattr(b, "on_collision"):
            b.on_collision(a)

    # ---------------------------------
    # Screen Collision
    # ---------------------------------

    def screen_collision(
        self,
        width,
        height
    ):

        for obj in self.objects:

            if not getattr(obj, "active", True):
                continue

            if obj.position.x < obj.radius:

                obj.position.x = obj.radius

                obj.velocity.x *= -obj.bounce

            elif obj.position.x > width - obj.radius:

                obj.position.x = width - obj.radius

                obj.velocity.x *= -obj.bounce

            if obj.position.y < obj.radius:

                obj.position.y = obj.radius

                obj.velocity.y *= -obj.bounce

            elif obj.position.y > height - obj.radius:

                obj.position.y = height - obj.radius

                obj.velocity.y *= -obj.bounce

    # ---------------------------------
    # Get All
    # ---------------------------------

    def get_objects(self):

        return self.objects

    # ---------------------------------
    # Count
    # ---------------------------------

    def count(self):

        return len(self.objects)
    def check_point_collision(
        self,
        point,
        obj
    ):

        px, py = point

        dx = px - obj.position.x
        dy = py - obj.position.y

        return math.sqrt(
            dx * dx +
            dy * dy
            ) <= obj.radius
    
    def check_screen_bounds(
        self,
        obj,
        width,
        height
    ):

        return (
            obj.position.x < 0 or
            obj.position.x > width or
            obj.position.y < 0 or
            obj.position.y > height
        )
    
    def ray_collision(
        self,
        start,
        end,
        obj
    ):

        x1, y1 = start
        x2, y2 = end

        ox = obj.position.x
        oy = obj.position.y

        dx = x2 - x1
        dy = y2 - y1

        if dx == 0 and dy == 0:
            return False

        t = (
            (ox - x1) * dx +
            (oy - y1) * dy
        ) / (
            dx * dx +
            dy * dy
        )

        t = max(0, min(1, t))

        cx = x1 + dx * t
        cy = y1 + dy * t

        dist = math.hypot(
            ox - cx,
            oy - cy
        )

        return dist <= obj.radius
    # ---------------------------------
    # Reset
    # ---------------------------------

    def reset(self):

        self.clear()