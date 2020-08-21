# LeetCode 19 - Remove Nth Node From End of List
#
# Given a linked list, remove the n-th node from the end of list and return its head.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    if not head or not n:
        return ListNode()

    # The plan is to keep track of the current node and the node that is lagging behind by n+1
    # nodes behind. When we get to the end, we can re-map the next value of that node to
    # remove the node of interest from the list.
    node_count = 0
    lead_node = head
    lag_node = None

    while lead_node:
        node_count += 1
        lead_node = lead_node.next

        if lag_node:
            lag_node = lag_node.next

        # We look for the n+1 node because that is the node with the .next value we need to remap
        if node_count == n+1:
            lag_node = head

    if node_count == n:
        # This is a special case since there is no previous node that we can remap
        return head.next

    # In this branch we have a previous node where we can remap the .next value
    lag_node.next = lag_node.next.next
    return head

# Tests
a = ListNode(5, None)
b = ListNode(4, a)
c = ListNode(3, b)
d = ListNode(2, c)
e = ListNode(1, d)

output_list = removeNthFromEnd(e, 2)

while output_list:
    print(output_list.val)
    output_list = output_list.next
