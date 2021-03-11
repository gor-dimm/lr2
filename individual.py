from math import hypot


def distance(p1, p2):
    return hypot(p1[0] - p2[0], p1[1] - p2[1])


print(distance((3, 3), (4, 2)))