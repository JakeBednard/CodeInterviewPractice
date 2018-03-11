"""
Implement a Naive Stack based on Python List
Avoid using built-ins.
"""

class stack(object):

    def __init__(self):
        self._stack = []
        self._max = -1
        self._length = -1
        self.head = -1

    def __len__(self):
        return self._length + 1

    def push(self, value):
        """Push value on to top of stack"""
        self._stack.append(value)
        self._length += 1
        if value > self._max:
            self._max = value
        return

    def pop(self):
        """Remove value from top of stack. If no value, returns none"""
        if self._length != -1:
            value = self._stack[self._length]
            self._length -= 1
            if self._max == value:
                self._max = -1
            return value

        else:
            return None

    def max(self):
        """Determine max value, if not defined, recheck list for validity, else return -1"""
        if self._max == -1:
            for i in self._stack[:len(self)]:
                if i > self._max:
                    self._max = i

        return self._max

# Test
test = stack()
print(len(test) == 0)
test.push(13)
test.push(2)
test.push(333)
test.push(33)
print(len(test))
print("max", test.max())
print(test.pop())
print(test.pop())
print(test.pop())
print(test.pop())
print(test.pop())
print("max", test.max())
