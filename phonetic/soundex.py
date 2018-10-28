""" soundex.py
https://en.wikipedia.org/wiki/Soundex
2018/10/27
Daniel Hu
"""


def soundex(word):
    word = word.upper()
    replace = (('BFPV', '1'),
                ('CGJKQSXZ', '2'),
                ('DT', '3'),
                ('L', '4'),
                ('MN', '5'),
                ('R', '6'))

    last = None
    soundex_code = "" + word[0] + ""
    count = 1
    for word_set, sub in replace:
        if word[0] in word_set:
            last = sub
            break
        else:
            last = None

    for char in word[1:]:
        for word_set, sub in replace:
            if char in word_set:
                if sub != last:
                    soundex_code += sub
                    count += 1
                last = sub
                break
        else:
            last = None

        if count == 4:
            break

    soundex_code += "0" * (4-count)

    return soundex_code

print(soundex("heterogeneity"))
