import time

previous_time = 0


def calculate_fps():
    global previous_time

    current_time = time.time()

    if previous_time == 0:
        previous_time = current_time
        return 0

    fps = 1 / (current_time - previous_time)

    previous_time = current_time

    return int(fps)