class GestureFusion:

    def __init__(self):
        self.last = "UNKNOWN"



    def fuse(self, ai_gesture, rule_gesture, confidence):

        # AI is very confident
        if confidence >= 0.80:
            self.last = ai_gesture
            return ai_gesture

        # Rule recognizer agrees
        if (
            rule_gesture != "UNKNOWN"
            and ai_gesture == rule_gesture
        ):
            self.last = ai_gesture
            return ai_gesture

        # Medium confidence
        if confidence >= 0.60:
            self.last = ai_gesture
            return ai_gesture

        # Keep previous stable gesture
        return self.last