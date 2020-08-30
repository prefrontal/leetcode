# LeetCode 92 - Reverse Linked Sublist
#
# Reverse a linked list from position m to n. Do it in one-pass.
# Note: 1 ≤ m ≤ n ≤ length of list.

import time

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head: ListNode, m: int, n: int) -> ListNode:
    if not head or not head.next or m == n:
        return head

    node_count = 0
    pre_rev_node = None
    previous_node = None
    current_node = head

    while current_node:
        node_count += 1

        if node_count < m and m > 1:
            pre_rev_node = current_node
            previous_node = current_node
        elif node_count >= m and node_count <= n:
            if node_count == n:
                if pre_rev_node:
                    pre_rev_node.next.next = current_node.next
                    pre_rev_node.next = current_node
                else:
                    head.next = current_node.next
                    head = current_node

            temp_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = temp_node

            continue

        current_node = current_node.next

    return head


# Tests
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL

e = ListNode(5, None)
d = ListNode(4, e)
c = ListNode(3, d)
b = ListNode(2, c)
a = ListNode(1, b)

rev = reverseBetween(a, 2, 4)

while rev:
    print(rev.val)
    rev = rev.next
    time.sleep(.1)
