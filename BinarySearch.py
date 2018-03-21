def binary_search(value, values):
    mid = int(len(values) / 2)
    if not values:
        return False
    elif value == values[mid]:
        return True
    elif value < values[mid]:
        return binary_search(value, values[:mid])
    else:
        return binary_search(value, values[mid+1:])

values = [1,2,3,4,5,6,10]
print(binary_search(6, values))