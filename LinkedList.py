class LinkedList:

    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def __init__(self):
        self.head = None

    def add(self, value):
        if not self.head:
            self.head = self.Node(value)
        else:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next

            pointer.next = self.Node(value)

    def remove(self, value):
        if self.head.value == value:
            if self.head.next:
                self.head = self.head.next
            else:
                self.head = None
            return

        pointer = self.head
        while pointer.next and pointer.next.value != value:
            pointer = pointer.next

        if not pointer.next:
            return
        elif not pointer.next.next:
            pointer.next = None
        else:
            pointer.next = pointer.next.next

    def reverse(self):

        current_node = self.head
        previous_node = None

        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        self.head = previous_node

        return

    def remove_duplicates(self):
        """Assumes sorted list"""
        trailer_node = self.head
        current_node = self.head

        while trailer_node:
            while current_node.next:
                if trailer_node.value == current_node.next.value:
                    current_node.next = current_node.next.next
                current_node = current_node.next
            trailer_node = trailer_node.next
            current_node = trailer_node

    def remove_duplicates_dynamic(self):

        values = set()
        previous = self.head
        current = self.head

        while current:
            if current.value in values:
                previous.next = current.next
                current = current.next
            else:
                values.add(current.value)
                previous = current
                current = current.next

    def __str__(self):

        pointer = self.head
        values = []

        while pointer:
            values.append(pointer.value)
            pointer = pointer.next

        return values.__str__()

if __name__ == '__main__':
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(4)
    ll.add(3)
    ll.add(3)
    ll.add(4)
    ll.add(3)
    ll.add(3)
    ll.add(4)
    ll.add(4)
    ll.add(4)
    ll.add(5)
    ll.add(5)
    ll.add(5)

    ll.remove_duplicates_dynamic()
    print(ll)

