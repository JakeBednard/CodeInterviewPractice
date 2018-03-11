"""Merge 2 prior sorted linked list into linked list"""

class node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def print_linked_list(head):
    temp = []
    while True:
        temp.append(head.value)
        head = head.next
        if head is None:
            break
    print(temp)


def merge_two_lists(l1, l2):
    head = node(-1, None)
    point = head
    while l1 or l2:
        if l1 and l2:
            if l1.value <= l2.value:
                point.next = node(l1.value)
                point = point.next
                l1 = l1.next
            elif l1.value > l2.value:
                point.next = node(l2.value)
                point = point.next
                l2 = l2.next
        elif l1 and not l2:
            point.next = node(l1.value)
            point = point.next
            l1 = l1.next
        elif not l1 and l2:
            point.next = node(l2.value)
            point = point.next
            l2 = l2.next

    return head.next

# Linked List 1
list1 = node(0)
point = list1
for i in [3,5,7,9,11,13,15,17]:
    point.next = node(i)
    point = point.next

# Linked List 2
list2 = node(1)
point = list2
for i in [2,2,3,4,5]:
    point.next = node(i)
    point = point.next

list3 = merge_two_lists(list1, list2)
print_linked_list(list3)
