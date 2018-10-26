""" dam_lev_distance
Damerau-Levenshtein Distance
https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance
2018/10/27
Daniel Hu
"""


def dam_lev_distance(token, correct_wd):
    # insertion / deletion / replacement / transposition / match
    i = 1
    d = 1
    r = 1
    t = 1
    m = 0

    dy = [[0]]

    for j in range(1, len(correct_wd)+1):
        dy.append([i * j])
    for k in range(1, len(token)+1):
        dy[0].append(d * k)

    for j in range(1, len(correct_wd)+1):
        for k in range(1, len(token)+1):
            match = r
            if token[k-1] == correct_wd[j-1]:
                match = m
            dy[j].append(min(dy[j][k-1] + d, dy[j-1][k] + i, dy[j-1][k-1] + match))

            if j>1 and k>1:
                if token[k-1] == correct_wd[j-2] and token[k-2] == correct_wd[j-1]:
                    dy[j][k] = min(dy[j][k], dy[j-2][k-2] + t)

    return dy[len(correct_wd)][len(token)]
