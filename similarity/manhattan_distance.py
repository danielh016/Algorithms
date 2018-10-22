""" manhattan_distance.py
https://en.wikipedia.org/wiki/Taxicab_geometry
Also called Taxicab geometry
19, Oct, 2018
Daniel Hu
"""


def manhattan_distance(a, b):
    # a, b are the 2 vectors, can be n dimensional
    d = 0  # distance
    for i in range(0, len(a)):
        d += abs(a[i] - b[i])

    return d
