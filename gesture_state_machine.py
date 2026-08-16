from gesture_state import GestureState


class GestureStateMachine:

    def __init__(self):

        self.state = GestureState.NONE
        self.current = "UNKNOWN"
        self.counter = 0

    def update(self, gesture):

        if gesture == self.current:

            self.counter += 1

        else:

            self.current = gesture
            self.counter = 1

        if self.counter >= 5:

            self.state = GestureState.CONFIRMED

        else:

            self.state = GestureState.DETECTING

        return self.current, self.state

    def reset(self):

        self.state = GestureState.NONE
        self.current = "UNKNOWN"
        self.counter = 0