class GestureManager:

    def __init__(self):
        self.left_hand = None
        self.right_hand = None

    def update(self, hands, hand_types):

        self.left_hand = None
        self.right_hand = None

        for hand, hand_type in zip(hands, hand_types):

            if hand_type == "Left":
                self.left_hand = hand

            elif hand_type == "Right":
                self.right_hand = hand

    def get_left(self):
        return self.left_hand

    def get_right(self):
        return self.right_hand

    def has_left(self):
        return self.left_hand is not None

    def has_right(self):
        return self.right_hand is not None