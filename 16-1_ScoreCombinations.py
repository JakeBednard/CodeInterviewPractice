combos = {}

def combinations(n):
    if n < 0:
        return 0
    elif str(n) in combos:
        return combos[str(n)]
    elif n == 0:
        return 1
    else:
        sum = combinations(n-2) + combinations(n-3) + combinations(n-7)
        combos[str(n)] = sum
        return sum

print(combinations(55))