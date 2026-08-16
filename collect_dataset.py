import cv2
import csv
import os
from hand_detector import HandDetector
from feature_extractor import extract_features

def hand_moved(current, previous):

    if previous is None:
        return True

    total = 0

    for i in range(21):

        dx = current[i][1] - previous[i][1]
        dy = current[i][2] - previous[i][2]

        total += abs(dx) + abs(dy)

    return total > 60

detector = HandDetector()

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Camera Error")
    exit()

csv_file = "dataset/gestures.csv"  

os.makedirs("dataset", exist_ok=True)

if not os.path.exists(csv_file):

    with open(csv_file, "w", newline="") as f:

        writer = csv.writer(f)

        header = []

        for i in range(21):
            header.append(f"x{i}")
            header.append(f"y{i}")

        header.append("label")

        writer.writerow(header)

label = input("Enter Gesture Name: ").upper()
sample_count = 0
frame_count = 0
previous_landmarks = None

print("Collecting:", label)
print("Press 'S' to save a sample")
print("Press 'N' to change gesture")
print("Press 'Q' to quit")

with open(csv_file, "a", newline="") as file:

    writer = csv.writer(file)

    while True:
        success, frame = camera.read()

        if not success:
            break

        frame = cv2.flip(frame, 1)

        frame = detector.findHands(frame)
        frame_count += 1

        lmList = detector.findPosition(frame)
        ##print("Landmarks:", len(lmList))

        if len(lmList) >= 21:

            cv2.putText(
                frame,
                f"Gesture : {label}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                f"Samples : {sample_count}/300",
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 255, 0),
                2
            )
        cv2.imshow("Dataset Collector", frame)

        key = cv2.waitKey(1) & 0xFF

        if (
            len(lmList) >= 21
            and frame_count % 5 == 0
            and hand_moved(lmList, previous_landmarks)
        ):

            row = []

            features = extract_features(lmList)

            row.extend(features)

            row.append(label)

            writer.writerow(row)

            file.flush()          # <-- IMPORTANT
            os.fsync(file.fileno())  # <-- Force save to disk

            sample_count += 1

            print(f"✅ Sample {sample_count} Saved!")

            previous_landmarks = [point[:] for point in lmList]

        if key == ord("n"):

            label = input("\nEnter New Gesture Name: ").upper()

            sample_count = 0
            frame_count = 0
            previous_landmarks = None

            print("Now Collecting:", label)    

        if key == ord("q"):
          break

camera.release()
cv2.destroyAllWindows()    