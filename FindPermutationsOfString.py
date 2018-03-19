def does_permutation_exist(input, blob):
    """Search for any permutation of input string in blob"""
    combination = [i for i in input]
    for i in range(len(blob)-len(combination)+1):
        found = True
        for j in range(len(combination)):
            if blob[i+j] not in combination:
                found = False
                break
        if found:
            return i

    return -1

blob = "DFDBCRGECAB"
input = "BCA"
result = does_permutation_exist(input, blob)

print(result)
