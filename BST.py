class BST(object):

    class Node(object):
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right

    def __init__(self):
        self.head = None

    def insert(self, value):
        if self.head is None:
            self.head = self.Node(value)
        else:
            self.insert_helper(self.head, value)
        return

    def insert_helper(self, pointer, value):
        if value < pointer.value:
            if pointer.left is None:
                pointer.left = self.Node(value)
            else:
                self.insert_helper(pointer.left, value)
        else:
            if pointer.right is None:
                pointer.right = self.Node(value)
            else:
                self.insert_helper(pointer.right, value)
        return

    def remove(self, value):
        if self.head is None:
            return 1
        else:
            return self.remove_helper(self.head, value)

    def remove_helper(self, pointer, value):
        # TODO Implement
        return

    def max(self):
        pointer = self.head
        while pointer.right is not None:
            pointer = pointer.right
        return pointer.value

    def min(self):
        pointer = self.head
        while pointer.left is not None:
            pointer = pointer.left
        return pointer.value

    def height_helper(self, pointer):
        if pointer is None:
            return 0
        elif pointer.left is None and pointer.right is None:
            return 1
        else:
            left = 1 + self.height_helper(pointer.left)
            right = 1 + self.height_helper(pointer.right)
            return left if left > right else right

    def height(self):
        return self.height_helper(self.head) - 1

    def is_height_balanced(self):

        def height_balanced_helper(pointer):
            if pointer is None:
                return True

            left = self.height_helper(pointer.left)
            right = self.height_helper(pointer.right)

            if abs(left-right) < 2:
                return True and height_balanced_helper(pointer.left) and height_balanced_helper(pointer.right)
            else:
                return False

        return height_balanced_helper(self.head)


if __name__ == "__main__":
    # Test
    tree = BST()
    values = [5,3,2,4,1,7,9]
    for value in values:
        tree.insert(value)

    print(tree.is_height_balanced())