class EffectStateManager:
    def __init__(self):

        # Currently active effects
        self.current_single = None
        self.current_two_hand = None

    # ===================================================
    # SINGLE HAND
    # ===================================================

    def set_single(self, effect_name):

        changed = effect_name != self.current_single

        if changed:
            self.current_single = effect_name

        return changed

    def get_single(self):

        return self.current_single

    def clear_single(self):

        self.current_single = None

    # ===================================================
    # TWO HAND
    # ===================================================

    def set_two_hand(self, effect_name):

        changed = effect_name != self.current_two_hand

        if changed:
            self.current_two_hand = effect_name

        return changed

    def get_two_hand(self):

        return self.current_two_hand

    def clear_two_hand(self):

        self.current_two_hand = None

    # ===================================================
    # RESET
    # ===================================================

    def reset(self):

        self.current_single = None
        self.current_two_hand = None