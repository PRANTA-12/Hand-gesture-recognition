import math


class FeatureExtractor:
    """
    Converts MediaPipe hand landmarks into normalized AI features.
    """

    def __init__(self):
        pass

    # --------------------------------------------------
    # Normalize landmarks
    # --------------------------------------------------

    def normalize(self, lmList):

        if lmList is None:
            return None

        if len(lmList) < 21:
            return None

        # Wrist coordinates (Landmark 0)
        base_x = float(lmList[0][1])
        base_y = float(lmList[0][2])
        base_z = float(lmList[0][3])

        points = []

        # Convert to wrist-relative coordinates
        for point in lmList:

            x = float(point[1]) - base_x
            y = float(point[2]) - base_y
            z = float(point[3]) - base_z

            points.append([x, y, z])

        # ----------------------------------------
        # Find maximum distance from wrist
        # ----------------------------------------

        max_distance = 0.0

        for p in points:

            distance = math.sqrt(
                p[0] ** 2 +
                p[1] ** 2 +
                p[2] ** 2
            )

            if distance > max_distance:
                max_distance = distance

        if max_distance == 0:
            max_distance = 1.0

        # ----------------------------------------
        # Scale normalization
        # ----------------------------------------

        features = []

        for p in points:

            features.extend([
                p[0] / max_distance,
                p[1] / max_distance,
                p[2] / max_distance
            ])

        return features

    # --------------------------------------------------
    # Feature extraction alias
    # --------------------------------------------------

    def extract(self, lmList):
        return self.normalize(lmList)