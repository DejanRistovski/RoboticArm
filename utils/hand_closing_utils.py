import numpy as np

def distance(l1, l2):
    return abs(pow(l1[0] - l2[0], 2) + pow(l1[1] - l2[1], 2))

def check_closed(lms) -> bool:
    distances = []
    first = lms[9]
    distances.append(distance(first, lms[4]))
    distances.append(distance(first, lms[8]))
    distances.append(distance(first, lms[12]))
    distances.append(distance(first, lms[16]))
    distances.append(distance(first, lms[20]))
    dist = np.sum(distances)

    if dist <= 10000:
        return True
    return False