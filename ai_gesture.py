import time
import joblib
import numpy as np
from ai.feature_extractor import FeatureExtractor


class AIGestureRecognizer:

    def __init__(self):

        import warnings
        warnings.filterwarnings("ignore", category=UserWarning)

        self.model = joblib.load("models/gesture_model.pkl")
        self.model.n_jobs = 1  # avoid multi-core dispatch overhead on single-row predictions
        self.extractor = FeatureExtractor()

    def predict(self, lmList):

        if len(lmList) < 21:
            return "UNKNOWN", 0.0

        features = self.extractor.extract(lmList)

        if features is None:
            return "UNKNOWN", 0.0

        features_array = np.asarray(features, dtype=np.float64).reshape(1, -1)

        probabilities = self.model.predict_proba(features_array)[0]

        best_index = probabilities.argmax()
        prediction = self.model.classes_[best_index]
        confidence = probabilities[best_index]
        if confidence < 0.75:
            return "UNKNOWN", confidence

        return prediction, confidence

    