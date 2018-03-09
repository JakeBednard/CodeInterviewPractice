class Parity(object):

    """
    Assume input is a maximum of 64-bit integer.
    Use dynamic programming to memoize prior solutions.
    Break into 16 bit chunks to optimize solution.
    """

    def __init__(self):
        self.lookup = {}  # Dict hashmap to cache values

    def compute_parity(self, value):

        # If value is greater than 16-bit int, recursively chunk it.
        if value > (2 ** 16 - 1):
            return (
                self.compute_parity(value & 0xFFFF) ^
                self.compute_parity(value >> 16 & 0xFFFF) ^
                self.compute_parity(value >> 32 & 0xFFFF) ^
                self.compute_parity(value >> 48 & 0xFFFF)
            )

        # Check to see if we already cached the current value
        elif value in self.lookup:
            return self.lookup[str(value)]

        # Calculate parity of integer
        else:
            lookup_key = str(value)

            result = 0
            while value:
                result ^= value & 1
                value >>= 1

            self.lookup[lookup_key] = result

            return result


if __name__ == "__main__":
    """Tests all inputs up (-1 * 2**64-1) to 2**64-1"""

    def naive_parity(x):
        result = 0
        while x:
            result ^= x & 1
            x >>= 1
        return result

    test = Parity()
    for i in range(-1 * (2**64 - 1), 2**64 - 1):
        if naive_parity(i) != test.compute_parity(i):
            # If we failed, notify and display value
            print("Failed:", bin(i))
