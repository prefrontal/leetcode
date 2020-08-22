# LeetCode 21 - Merge Sorted Lists
#
# Merge two sorted linked lists and return it as a new sorted list. The new list should be
# made by splicing together the nodes of the first two lists.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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


# Tests
c = ListNode(4, None)
b = ListNode(2, c)
a = ListNode(1, b)

z = ListNode(4, None)
y = ListNode(3, z)
x = ListNode(1, y)

sortedNode = mergeTwoLists(a, x)

# Expected output is 1->1->2->3->4->4
while sortedNode:
    print(sortedNode.val)
    sortedNode = sortedNode.next
