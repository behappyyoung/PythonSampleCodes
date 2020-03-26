"""
Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.

"""


def removeNthFromEnd(head, n: int):
    count = 0
    c_head = head
    while c_head is not None:
        c_head = c_head.next
        count += 1

    if count <= n:
        return head
    c_head = head
    i = 0
    while i < (count - n):
        print(i, count, n, c_head)
        c_head = c_head.next
        i += 1

    c_head.next = c_head.next.next
    return head

from _LinkedLists import ListNode, print_node

lnode = ListNode(1)
lnode.next = ListNode(2)
lnode.next.next = ListNode(4)
print_node(lnode)
print(removeNthFromEnd(lnode, 2))
print_node(lnode)