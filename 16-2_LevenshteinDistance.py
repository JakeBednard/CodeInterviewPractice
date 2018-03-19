def distance(a, b):

    def compute_distance(a_idx, b_idx):

        if a_idx < 0:
            return b_idx + 1
        elif b_idx < 0:
            return a_idx + 1

        if precomputed[a_idx][b_idx] == -1:
            if a[a_idx] == b[b_idx]:
                precomputed[a_idx][b_idx] = compute_distance(a_idx-1, b_idx-1)
            else:
                sub = compute_distance(a_idx-1, b_idx-1)
                add = compute_distance(a_idx, b_idx-1)
                delete = compute_distance(a_idx, b_idx-1)
                precomputed[a_idx][b_idx] = 1 + min(sub, add, delete)

        return precomputed[a_idx][b_idx]

    precomputed = [[-1] * len(b) for i in a]
    return compute_distance(len(a)-1, len(b)-1)

print(distance("Jake", "John"))
