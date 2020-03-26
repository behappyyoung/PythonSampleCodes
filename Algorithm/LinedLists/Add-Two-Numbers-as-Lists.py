"""
You are given two linked lists representing two non-negative numbers.
The digits are stored in reverse order and each of their nodes contain a single digit.
 Add the two numbers and return it as a linked list.

For example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)

Output: 7 -> 0 -> 8

342 + 465 = 807


"""


def addTwoNumbers(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = l1
        overflow = 0
        pre = l1
        while l1 is not None and l2 is not None:
            c_sum = l1.val + l2.val + overflow
            if c_sum >= 10:
                c_sum -= 10
                overflow = 1
            l1.val = c_sum
            pre = l1
            l1 = l1.next
            l2 = l2.next

        if l2 is not None:
            pre.next = l2
            l1 = pre.next

        while l1 is not None:
            c_sum = l1.val + overflow
            if c_sum >= 10:
                c_sum -= 10
                overflow = 1
            l1.val = c_sum
            pre = l1
            l1 = l1.next

        if overflow:
            pre.next = ListNode(1)

        return head
#test
from _LinkedLists import ListNode, print_node

lnode = ListNode(1)
lnode.next = ListNode(2)
lnode.next.next = ListNode(4)


lnode2 = ListNode(1)
lnode2.next = ListNode(2)
lnode2.next.next = ListNode(5)

print_node(lnode)
print_node(lnode2)
# print_node(addTwoNumbers(lnode, lnode2))

lnode = ListNode(9)
lnode.next = ListNode(9)
lnode.next.next = ListNode(9)

lnode2 = ListNode(1)

print_node(lnode2)
print_node(lnode)
# print_node(addTwoNumbers(lnode, lnode2))

print_node(addTwoNumbers(lnode2, lnode))
