import cv2

class StatusBar:

    def draw(self, frame, fps, energy, power):

        h, w = frame.shape[:2]

        cv2.rectangle(
            frame,
            (0, h - 35),
            (w, h),
            (30, 30, 30),
            -1
        )

        cv2.putText(
            frame,
            f"FPS : {int(fps)}",
            (20, h - 12),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0,255,0),
            2
        )

        cv2.putText(
            frame,
            f"Energy : {int(energy)}",
            (180, h - 12),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255,255,0),
            2
        )

        cv2.putText(
            frame,
            f"Power : {power if power else 'NONE'}",
            (400, h - 12),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0,255,255),
            2
        )