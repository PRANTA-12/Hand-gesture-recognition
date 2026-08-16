from enum import Enum


class GestureState(Enum):

    NONE = 0

    DETECTING = 1

    CONFIRMED = 2

    LOST = 3