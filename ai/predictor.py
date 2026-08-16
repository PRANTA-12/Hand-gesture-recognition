from ai.model_loader import ModelLoader
from ai.feature_extractor import FeatureExtractor

class AIPredictor:
    """
    Converts MediaPipe landmarks into features
    and predicts the gesture using the trained AI model.
    """

    def __init__(self):

        self.model = ModelLoader()
        self.random_forest = self.model.get_model()
        self.feature_columns = self.model.get_feature_columns()
        self.extractor = FeatureExtractor()

    # ---------------------------------------
    # Landmark -> Feature Vector
    # ---------------------------------------

    def extract_features(self, lmList):
        return self.extractor.extract(lmList)

    # ---------------------------------------
    # Predict Gesture
    # ---------------------------------------

    def predict(self, lmList):

        features = self.extract_features(lmList)

        if features is None:
            return None

        import pandas as pd

        df = pd.DataFrame(
            [features],
            columns=self.feature_columns
        )

        prediction = self.random_forest.predict(df)[0]

        return prediction

    # ---------------------------------------
    # Predict Gesture + Confidence
    # ---------------------------------------

    def predict_with_confidence(self, lmList):

        features = self.extract_features(lmList)

        if features is None:
            return None, 0.0

        import pandas as pd

        df = pd.DataFrame(
            [features],
            columns=self.feature_columns
        )

        prediction = self.random_forest.predict(df)[0]

        probabilities = self.random_forest.predict_proba(df)[0]

        confidence = float(max(probabilities))

        if confidence < 0.80:
            return "UNKNOWN", confidence

        return prediction, confidence