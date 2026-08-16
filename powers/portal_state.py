from enum import Enum


class PortalState(Enum):

    IDLE = 0
    OPENING = 1
    ACTIVE = 2
    CLOSING = 3


class PortalStateMachine:

    def __init__(self):

        self.state = PortalState.IDLE

    def set_state(self, state):

        self.state = state

    def get_state(self):

        return self.state

    def is_idle(self):

        return self.state == PortalState.IDLE

    def is_opening(self):

        return self.state == PortalState.OPENING

    def is_active(self):

        return self.state == PortalState.ACTIVE

    def is_closing(self):

        return self.state == PortalState.CLOSING

    def start(self):

        if self.state == PortalState.IDLE:
            self.state = PortalState.OPENING

    def activate(self):

        if self.state == PortalState.OPENING:
            self.state = PortalState.ACTIVE

    def close(self):

        if self.state in (
            PortalState.OPENING,
            PortalState.ACTIVE
        ):
            self.state = PortalState.CLOSING

    def reset(self):

        self.state = PortalState.IDLE