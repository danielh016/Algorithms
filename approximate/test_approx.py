""" test_approx.py
2018/10/25
"""

import time
from lev_distance import lev_distance
from bigram import bigram


def test_lev(token):
    start = time.time()
    f = open("dict.txt", "r")
    min_distance = 100
    approx_word = ""
    print("calculating...")
    for x in f:
        word = x.rstrip('\n')
        distance = lev_distance(token, word)
        if distance < min_distance:
            approx_word = word
            min_distance = distance
    end = time.time()

    print("Token: " + token + ", Predict: " + approx_word + ", Distance: " + str(min_distance))
    print("Runtime: " + str(end - start))


def test_bigram(token):
    start = time.time()
    f = open("dict.txt", "r")
    min_distance = 100
    approx_word = ""
    print("calculating...")
    for x in f:
        word = x.rstrip('\n')
        distance = bigram(token, word)
        if distance < min_distance:
            approx_word = word
            min_distance = distance
    end = time.time()

    print("Token: " + token + ", Predict: " + approx_word + ", Distance: " + str(min_distance))
    print("Runtime: " + str(end - start))


test_lev("helo")
test_bigram("helo")
