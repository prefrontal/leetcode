# LeetCode 206 - Reverse Linked List
#
# Reverse a singly linked list.

import time

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    next_node = None

    while head:
        temp_node = head.next
        head.next = next_node
        next_node = head

        head = temp_node

    return next_node

# Testing
# Given 1->2->3->4, you should return the list as 4->3->2->1.

d = ListNode(4, None)
c = ListNode(3, d)
b = ListNode(2, c)
a = ListNode(1, b)

rev = reverseList(a)

while rev:
    print(rev.val)
    rev = rev.next