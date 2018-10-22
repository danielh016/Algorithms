""" euclidean_distance.py
https://en.wikipedia.org/wiki/Euclidean_distance
Calculate the distance between two point on N Dimension
18, Oct, 2018
Daniel Hu
"""


def euclidean_distance(a, b):
    d = 0 # distance
    for i in range(0, len(a)):
        d += (a[i]-b[i])**2

    return d**.5
