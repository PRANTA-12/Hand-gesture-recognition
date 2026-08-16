import cv2


def draw_fire_icon(frame, x, y):

    # Outer glow
    cv2.circle(
        frame,
        (x, y),
        10,
        (0, 100, 255),
        -1,
        lineType=cv2.LINE_AA
    )

    # Middle flame
    cv2.circle(
        frame,
        (x, y),
        7,
        (0, 180, 255),
        -1,
        lineType=cv2.LINE_AA
    )

    # Hot core
    cv2.circle(
        frame,
        (x, y),
        3,
        (255, 255, 255),
        -1,
        lineType=cv2.LINE_AA
    )