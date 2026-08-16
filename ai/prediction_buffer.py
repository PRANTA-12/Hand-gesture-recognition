from collections import deque, Counter


class PredictionBuffer:
    """
    Buffers AI gesture predictions and returns
    the most frequent prediction to reduce flickering.
    """

    def __init__(self, size=5):
        self.size = size
        self.buffer = deque(maxlen=size)

    # ---------------------------------------
    # Add a new prediction
    # ---------------------------------------

    def update(self, prediction):

        if prediction is None:
            prediction = "UNKNOWN"

        self.buffer.append(prediction)

        return self.get_prediction()

    # ---------------------------------------
    # Get Stable Prediction
    # ---------------------------------------

    def get_prediction(self):

        if len(self.buffer) == 0:
            return "UNKNOWN"

        counter = Counter(self.buffer)

        stable_prediction = counter.most_common(1)[0][0]

        return stable_prediction

    # ---------------------------------------
    # Clear Buffer
    # ---------------------------------------

    def clear(self):

        self.buffer.clear()

    # ---------------------------------------
    # Buffer Size
    # ---------------------------------------

    def __len__(self):

        return len(self.buffer)

    # ---------------------------------------
    # Current Buffer
    # ---------------------------------------

    def get_buffer(self):

        return list(self.buffer)

    # ---------------------------------------
    # Debug Print
    # ---------------------------------------

    def print_buffer(self):

        print("Prediction Buffer:", list(self.buffer))