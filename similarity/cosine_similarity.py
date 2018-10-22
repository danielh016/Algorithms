""" cosine_similarity.py
https://en.wikipedia.org/wiki/Cosine_similarity
Common used similarity measuring method in Data Mining
20, Oct, 2018
Daniel Hu
"""


def cosine_similarity(a, b):
    dot_product = 0
    magnitude_a = 0
    magnitude_b = 0

    for i in range(0, len(a)):
        dot_product += a[i] * b[i]
        magnitude_a += a[i] ** 2
        magnitude_b += b[i] ** 2

    magnitude = (magnitude_a * magnitude_b) ** .5

    return dot_product / magnitude
