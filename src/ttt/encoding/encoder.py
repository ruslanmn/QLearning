def encode(state, base):
    res = 0
    i = 0
    for row in state:
        for e in row:
            res += e * base**i
            i += 1
    return res


def encode3(state):
    return encode(state, 3)
