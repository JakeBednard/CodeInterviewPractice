def int_to_string(value):
    """
    Manually Convert String to Int
    Assume only numeric chars in string
    """

    is_negative = False
    if value < 0:
        is_negative = True
        value *= -1

    output = []
    while value:
        value, i = divmod(value, 10)
        output.append((chr(i + ord('0'))))

    return ('-' if is_negative else '') + "".join(reversed(output))


print(int_to_string(133))
print(int_to_string(-133))