import cv2

class PowerHUD:

    def draw(self, frame, current_action):

        text = str(current_action)

        cv2.putText(
            frame,
            f"Active Power : {text}",
            (20, 510),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 255),
            2
        )