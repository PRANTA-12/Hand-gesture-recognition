from animation import Animation
from animation_state import AnimationState


class ContinuousAnimation(Animation):

    def __init__(self):

        super().__init__(duration=999999)

        self.state = AnimationState.IDLE

    def start(self, position):

        self.position = position

        self.active = True

        self.state = AnimationState.ACTIVE

    def move(self, position):

        self.position = position

    def stop(self):

        self.active = False

        self.state = AnimationState.IDLE