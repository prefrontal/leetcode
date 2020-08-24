# LeetCode 24 - Swap Nodes In Pairs
#
# Given a linked list, swap every two adjacent nodes and return its head.
# You may not modify the values in the list's nodes, only nodes itself may be changed.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    # If we get this far then we have at least two nodes
    start = head    
    head = head.next
    last_end = None

    while start and start.next:
        first = start
        second = start.next
        third = start.next.next

        second.next = first
        first.next = third
        start = third

        if last_end:
            last_end.next = second

        last_end = first

    return head


# Tests
# Given 1->2->3->4, you should return the list as 2->1->4->3.

e = ListNode(5, None)
d = ListNode(4, e)
c = ListNode(3, d)
b = ListNode(2, c)
a = ListNode(1, b)

swapped = swapPairs(a)

while swapped:
    print(swapped.val)
    swapped = swapped.next
