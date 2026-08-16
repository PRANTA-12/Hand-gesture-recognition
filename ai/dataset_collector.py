import csv
import os
from ai.feature_extractor import FeatureExtractor

class DatasetCollector:

    def __init__(self, filename="dataset/gesture_dataset.csv"):
        self.extractor = FeatureExtractor()
        self.filename = filename

        os.makedirs(os.path.dirname(filename), exist_ok=True)

        if not os.path.exists(filename):
            self.create_csv()

        self.recording = False
        self.current_label = None
        self.total_samples = 0

        self.frame_count = 0
        self.save_interval = 3


    # ---------------------------------------
    # Create CSV with Header
    # ---------------------------------------

    def create_csv(self):

        header = []

        for i in range(21):
            header.append(f"x{i}")
            header.append(f"y{i}")
            header.append(f"z{i}")

        header.append("label")

        with open(self.filename, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow(header)

    def start_recording(self, label):
        self.recording = True
        self.current_label = label
        print(f"Recording started: {label}")  

    def stop_recording(self):

        self.recording = False
        self.current_label = None  

    def update(self, lmList):
        
        if not self.recording:
            return

        self.frame_count += 1

        if self.frame_count < self.save_interval:
            return

        self.frame_count = 0

        if self.save(lmList, self.current_label):
            self.total_samples += 1           

    # ---------------------------------------
    # Convert Landmarks -> Feature List
    # ---------------------------------------

    def extract_features(self, lmList):
       
        if lmList is None:
            return None
        

        if len(lmList) < 21:
            return None

        features = []

        for point in lmList:

            # Expected format:
            # [id, x, y, z]

            if len(point) >= 4:

                features.extend([
                    float(point[1]),
                    float(point[2]),
                    float(point[3])
                ])

            else:

                return None

        return features

    # ---------------------------------------
    # Save One Sample
    # ---------------------------------------

    def save(self, lmList, label):

        features = self.extractor.extract(lmList)
        
        if features is None:
            print("Features are None")
            return False

        row = features + [label]

        with open(self.filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(row)

        return True