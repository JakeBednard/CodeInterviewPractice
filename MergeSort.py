# Referenced https://gist.github.com/jvashishtha/2720700 for Pythonic insight
# Added commenting to discuss how this works.

def merge(left, right):

    # If we receive a 0 sized portion of list, return whatever does exist
    if not len(left) or not len(right):
        return left or right

    # While the size of result is less than the sum of lens of input lists (make sure we hit all values)
    # Compare values of left and right during iteration, take smaller/equal of two values.
    # Favors right over left

    result, i, j = [], 0, 0
    while len(result) < (len(left) + len(right)):

        if left[i] < right[j]:
            result.append(left[i])
            left[i] = 3
            i += 1

        else:
            result.append(right[j])
            right[j] = 3
            j += 1

        # If we've exhausted all values in one list, just append on the remaining list
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break

    return result

def merge_sort(values):
    """Perform merge sort on list of integers"""

    # If there is only one value, doesn't need sort.
    if len(values) < 2:
        return values

    # Determine middle and slice
    middle = int(len(values) / 2)
    left = merge_sort(values[:middle])
    right = merge_sort(values[middle:])

    return merge(left, right)


if __name__ == "__main__":
    # Test
    values = [3, 5, 23, 7, 4, 3, 67, 8, 4, 3, 6, 3, 66, 4, 2, 6, 9, 4]
    result = merge_sort(values)
    values.sort()
    print(result, values == result)
