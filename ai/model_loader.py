import os
import joblib
import pandas as pd
DATASET_PATH = "dataset/gesture_dataset.csv"

class ModelLoader:

    def __init__(self, model_path="models/gesture_model.pkl"):

        self.model_path = model_path
        self.model = None

        self.load_model()

    # ----------------------------------------
    # Load Model
    # ----------------------------------------

    def load_model(self):

        if not os.path.exists(self.model_path):
            raise FileNotFoundError(
                f"Model not found:\n{self.model_path}"
            )

        self.model = joblib.load(self.model_path)

        dataset = pd.read_csv(DATASET_PATH)
        self.feature_columns = dataset.drop("label", axis=1).columns

        print(f"[AI] Model Loaded: {self.model_path}")

    def get_model(self):
        return self.model

    def get_feature_columns(self):
        return self.feature_columns