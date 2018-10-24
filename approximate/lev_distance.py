""" lev_distance.py
Levenshtein Distance
https://en.wikipedia.org/wiki/Levenshtein_distance
2018/10/25
Daniel Hu
"""


def lev_distance(token, correct_word):
    input_str = token
    compare_str = correct_word

    # Set the parameter of the method.
    i = 1  # insertion
    d = 1  # deletion
    r = 1  # replacement
    m = 0  # match

    in_len = len(input_str)
    com_len = len(compare_str)

    dy = [[0]]  # dynamic programming list

    for j in range(1, com_len+1):
        dy.append([j * i])
    for k in range(1, in_len+1):
        dy[0].append(k * d)

    for j in range(1, com_len+1):
        for k in range(1, in_len+1):
            match = r
            if input_str[k-1] == compare_str[j-1]:
                match = m
            dy[j].append(min(dy[j][k-1] + d, dy[j-1][k] + i, dy[j-1][k-1] + match))

    return dy[com_len][in_len]
