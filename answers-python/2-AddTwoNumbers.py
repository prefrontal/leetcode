# LeetCode 2 - Add Two Numbers
#
# You are given two non-empty linked lists representing two non-negative integers. The digits are
# stored in reverse order and each of their nodes contain a single digit. Add the two numbers
# and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    # Don't modiy the function arguments
    list1 = l1
    list2 = l2

    magnitude = 1
    total = 0

    # Start off with the first digit in each list and go from there as long as
    # one or both lists still have digits to consider
    while list1 or list2:
        iteration_total = 0

        if list1:
            iteration_total += list1.val

            if not list1.next:
                list1 = None
            else:
                list1 = list1.next

        if list2:
            iteration_total += list2.val

            if not list2.next:
                list2 = None
            else:
                list2 = list2.next

        total += magnitude * iteration_total
        magnitude *= 10

    output = None
    for element in str(total):
        output = ListNode(int(element), output)

    return output


# Tests
# (2 -> 4 -> 3) + (5 -> 6 -> 4)
a = ListNode(3, None)
b = ListNode(4, a)
c = ListNode(2, b)

x = ListNode(4, None)
y = ListNode(6, x)
z = ListNode(5, y)

addition_output = addTwoNumbers(c, z)

# Expect 7-0-8 as the output
while addition_output:
    print(addition_output.val)
    addition_output = addition_output.next
