import math

def extract_features(lmList):

    if len(lmList) < 21:
        return []

    wrist_x = lmList[0][1]
    wrist_y = lmList[0][2]

    middle_x = lmList[9][1]
    middle_y = lmList[9][2]

    hand_size = math.sqrt(
        (middle_x - wrist_x) ** 2 +
        (middle_y - wrist_y) ** 2
    )

    if hand_size < 1:
        hand_size = 1

    features = []

    for point in lmList:

        x = (point[1] - wrist_x) / hand_size
        y = (point[2] - wrist_y) / hand_size

        features.append(x)
        features.append(y)

    return features