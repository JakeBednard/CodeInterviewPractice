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

if __name__ == "__main__":
    # Test
    tree = BST()
    values = [1,54,3,2,5,1,3,56,3,7,5,4,3,0,2,5,5]
    for value in values:
        tree.insert(value)

    print(tree.max())
    print(tree.min())