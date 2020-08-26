# LeetCode 25 - Reverse Nodes in k-Group
#
# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
# k is a positive integer and is less than or equal to the length of the linked list. If the number
# of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    if val <= 1:
        return head

    # If we get this far then we have at least two nodes
    start = head    
    --- head = head.next
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
# Given this linked list: 1->2->3->4->5
# For k = 2, you should return: 2->1->4->3->5
# For k = 3, you should return: 3->2->1->4->5

e = ListNode(5, None)
d = ListNode(4, e)
c = ListNode(3, d)
b = ListNode(2, c)
a = ListNode(1, b)

swapped = swapPairs(a)

while swapped:
    print(swapped.val)
    swapped = swapped.next