# LeetCode 83 - Remove Duplicates from Sorted List
#
# Given a sorted linked list, delete all duplicates such that each element appear only once.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    last_node = head
    last_unique = head

    # Iterate through the list. If the current value matches the last unique value, then we will
    # just re-link it to the next node so we can move linearly through the list
    while last_node:
        if last_unique.val == last_node.val:
            last_unique.next = last_node.next
        else:
            last_unique.next = last_node
            last_unique = last_node

        last_node = last_node.next

    return head


# Tests
# Input: 1->1->2->3->3
# Output: 1->2->3

e = ListNode(3, None)
d = ListNode(3, e)
c = ListNode(2, d)
b = ListNode(1, c)
a = ListNode(1, b)

rev = deleteDuplicates(a)

while rev:
    print(rev.val)
    rev = rev.next
