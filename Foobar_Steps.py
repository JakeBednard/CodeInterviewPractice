def answer(n):

    poss = [1] + [0] * n

    for k in range(1, n + 1):
        for i in range(n, k - 1, -1):
            poss[i] += poss[i - k]

    return poss[n] - 1
