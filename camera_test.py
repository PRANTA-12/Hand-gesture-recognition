import cv2
import time

camera = cv2.VideoCapture(0)

prev = time.time()

while True:

    ret, frame = camera.read()

    if not ret:
        break

    now = time.time()
    fps = 1 / (now - prev)
    prev = now

    cv2.putText(
        frame,
        f"FPS : {int(fps)}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("Camera Test", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()