"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists, and should also be sorted.

For example,
5 -> 8 -> 20
  4 -> 11 -> 15

4 -> 5 -> 8 -> 11 -> 15 -> 20


"""

def merge_two_sorted_lists(head_node, head_node2):
    if head_node2 is None:
        return head_node
    if head_node is None:
        return head_node2
    if head_node.val <= head_node2.val:
        c_node = head_node
        head_node = head_node.next
    else:
        c_node = head_node2
        head_node2 = head_node2.next
    return_node = c_node

    while c_node.next is not None:
        if head_node.val <= head_node2.val:
            c_node.next = head_node
            head_node = head_node.next
        else:
            c_node.next = head_node2
            head_node2 = head_node2.next
        c_node = c_node.next

    if head_node:
        c_node.next = head_node
    if head_node2:
        c_node.next = head_node2

    return return_node

def merge_two(main, sub):
            done = False
            return_node = main
            while sub and main.next:
                if sub.val < main.next.val:
                    temp = sub
                    sub = sub.next
                    temp.next = main.next.next
                    main.next.next = temp
                main = main.next
            return return_node

#test

from _LinkedLists import ListNode, print_node

lnode = ListNode(3)
lnode.next = ListNode(8)
lnode.next.next = ListNode(9)
lnode.next.next.next = ListNode(12)
lnode.next.next.next.next = ListNode(20)

lnode2 = ListNode(1)
lnode2.next = ListNode(4)
lnode2.next.next = ListNode(10)
lnode2.next.next.next = ListNode(30)

print_node(lnode)
print_node(lnode2)

# print_node(merge_two_sorted_lists(lnode, lnode2))
print_node(merge_two(lnode2, lnode))


lnode = ListNode(3)
lnode.next = ListNode(8)
lnode.next.next = ListNode(9)
lnode.next.next.next = ListNode(12)
lnode.next.next.next.next = ListNode(30)

lnode2 = ListNode(1)
lnode2.next = ListNode(8)
lnode2.next.next = ListNode(10)
lnode2.next.next.next = ListNode(30)

print_node(lnode)
print_node(lnode2)

print_node(merge_two_sorted_lists(lnode, lnode2))