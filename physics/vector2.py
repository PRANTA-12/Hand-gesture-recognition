import math


class Vector2:

    def __init__(self, x=0.0, y=0.0):

        self.x = float(x)
        self.y = float(y)

    # ---------------------------------
    # String Representation
    # ---------------------------------

    def __repr__(self):

        return f"Vector2({self.x:.2f}, {self.y:.2f})"

    # ---------------------------------
    # Copy
    # ---------------------------------

    def copy(self):

        return Vector2(self.x, self.y)

    # ---------------------------------
    # Tuple
    # ---------------------------------

    def tuple(self):

        return (self.x, self.y)

    # ---------------------------------
    # Magnitude
    # ---------------------------------

    def magnitude(self):

        x = self.x
        y = self.y

        return math.sqrt(x * x + y * y)

    # ---------------------------------
    # Length
    # ---------------------------------

    def length(self):

        return self.magnitude()

    # ---------------------------------
    # Normalize
    # ---------------------------------

    def normalize(self):

        length = self.magnitude()

        if length == 0:
            return Vector2()

        inv = 1.0 / length

        return Vector2(
            self.x * inv,
            self.y * inv
        ) 
    # ---------------------------------
    # Distance
    # ---------------------------------

    def distance_to(self, other):

        x = self.x
        y = self.y

        dx = x - other.x
        dy = y - other.y

        return math.sqrt(dx * dx + dy * dy)

    # ---------------------------------
    # Dot Product
    # ---------------------------------

    def dot(self, other):

        x = self.x
        y = self.y

        return x * other.x + y * other.y

    # ---------------------------------
    # Angle
    # ---------------------------------

    def angle(self):

        x = self.x
        y = self.y

        return math.degrees(math.atan2(y, x))

    # ---------------------------------
    # Rotate
    # ---------------------------------

    def rotate(self, degrees):

        r = math.radians(degrees)

        cos_a = math.cos(r)
        sin_a = math.sin(r)

        x = self.x
        y = self.y

        return Vector2(
            x * cos_a - y * sin_a,
            x * sin_a + y * cos_a
        )
    # ---------------------------------
    # Lerp
    # ---------------------------------

    def lerp(
        self,
        other,
        t
    ):

        x = self.x
        y = self.y

        return Vector2(
            x + (other.x - x) * t,
            y + (other.y - y) * t
        )

    # ---------------------------------
    # Clamp
    # ---------------------------------

    def clamp(self, max_length):

        length = self.magnitude()

        if length <= max_length:
            return self.copy()

        scale = max_length / length

        return Vector2(
            self.x * scale,
            self.y * scale
        )

    # ---------------------------------
    # Reflect
    # ---------------------------------

    def reflect(self, normal):

        n = normal.normalize()

        return self - n * (2 * self.dot(n))

    # ---------------------------------
    # Operators
    # ---------------------------------

    def __add__(self, other):

        return Vector2(

            self.x + other.x,

            self.y + other.y

        )

    def __sub__(self, other):

        return Vector2(

            self.x - other.x,

            self.y - other.y

        )

    def __mul__(self, value):

        if isinstance(value, Vector2):

            return Vector2(

                self.x * value.x,

                self.y * value.y

            )

        return Vector2(

            self.x * value,

            self.y * value

        )

    def __truediv__(self, value):

        if value == 0:

            return Vector2()

        return Vector2(

            self.x / value,

            self.y / value

        )

    def __neg__(self):

        return Vector2(

            -self.x,

            -self.y

        )

    def __eq__(self, other):

        return (

            self.x == other.x and

            self.y == other.y

        )

    # ---------------------------------
    # Utility
    # ---------------------------------

    @staticmethod
    def zero():

        return Vector2(0, 0)

    @staticmethod
    def one():

        return Vector2(1, 1)

    @staticmethod
    def up():

        return Vector2(0, -1)

    @staticmethod
    def down():

        return Vector2(0, 1)

    @staticmethod
    def left():

        return Vector2(-1, 0)

    @staticmethod
    def right():

        return Vector2(1, 0)

    @staticmethod
    def from_angle(angle, length=1):

        r = math.radians(angle)

        return Vector2(

            math.cos(r) * length,

            math.sin(r) * length

        )