# LeetCode 23 - Merge k sorted lists
#
# Given an array of linked-lists lists, each linked list is sorted in ascending order.
# Merge all the linked-lists into one sort linked-list and return it.
#
# Constraints:
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] is sorted in ascending order.
# The sum of lists[i].length won't exceed 10^4.

from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Pulled from answer 21, Merge Sorted Lists
def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if not l1:
        return l2

    if not l2:
        return l1

    # Determine where we are going to start regarding the output
    output = None

    if l1.val < l2.val:
        output = l1
        l1 = l1.next
    else:
        output = l2
        l2 = l2.next

    # Now we can start assembling the rest of the output
    previous_node = output

    while l1 or l2:
        # Handle the cases where we have values in one list but not the other
        if not l1 and l2:
            previous_node.next = l2
            previous_node = l2
            l2 = l2.next
            continue
        if l1 and not l2:
            previous_node.next = l1
            previous_node = l1
            l1 = l1.next
            continue

        # Handle the case where we have values in both lists
        if l1.val < l2.val or l1.val == l2.val:
            previous_node.next = l1
            previous_node = l1
            l1 = l1.next
        else:
            previous_node.next = l2
            previous_node = l2
            l2 = l2.next

    return output


def mergeKLists(lists: List[ListNode]) -> ListNode:
    if not lists:
        return None

    if len(lists) == 1:
        return lists[0]

    output = lists[0]

    for index, node in enumerate(lists):
        if index == 0:
            continue

        output = mergeTwoLists(output, node)

    return output


# Tests
c1 = ListNode(5, None)
b1 = ListNode(4, c1)
a1 = ListNode(1, b1)

c2 = ListNode(4, None)
b2 = ListNode(3, c2)
a2 = ListNode(1, b2)

b3 = ListNode(6, None)
a3 = ListNode(2, b3)

sortedNode = mergeKLists([a1, a2, a3])

# Expected output is 1,1,2,3,4,4,5,6
while sortedNode:
    print(sortedNode.val)
    sortedNode = sortedNode.next
