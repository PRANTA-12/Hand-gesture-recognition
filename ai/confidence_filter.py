class ConfidenceFilter:
    """
    Filters AI predictions based on confidence.

    If the confidence is lower than the threshold,
    return UNKNOWN.
    Otherwise return the original prediction.
    """

    def __init__(self, threshold=0.80):
        self.threshold = threshold

    def filter(self, prediction, confidence):

        if prediction is None:
            return "UNKNOWN"

        if confidence < self.threshold:
            return "UNKNOWN"

        return prediction

    def set_threshold(self, threshold):
        self.threshold = threshold

    def get_threshold(self):
        return self.threshold

    def reset(self):
        pass