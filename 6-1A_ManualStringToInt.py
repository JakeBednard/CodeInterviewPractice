def string_to_int(value):
    """
    Manually Convert String to Int
    Assume only numeric chars in string
    """

    # Determine if output should be negative
    is_negative = False
    if value[0:1] == '-':
        is_negative = True
        value = value[1:]

    output = 0
    for exp, i in enumerate(reversed(value)):
        output += (ord(i) - ord('0')) * (10 ** exp)

    return output if not is_negative else -1 * output


# Test
print(string_to_int("133"))
print(string_to_int("-133"))
