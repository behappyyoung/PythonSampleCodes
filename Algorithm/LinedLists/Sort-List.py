"""
Sort a linked list using insertion sort.

Input : 1 -> 5 -> 4 -> 3

Returned list : 1 -> 3 -> 4 -> 5

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# print node
def print_node(head_node):
    c_node = head_node
    print_str = ''
    while c_node is not None:
        print_str += '->' + str(c_node.val)
        c_node = c_node.next
    print(print_str)

##################################################
def insert_list(A, i_node):
    c_node = A
    if i_node.val < c_node.val  :
        i_node.next = A
        return i_node

    while c_node.next is not None:
        if i_node.val < c_node.next.val :
            i_node.next = c_node.next
            c_node.next = i_node
            return A
        c_node = c_node.next

    return A

def sort_list(A):
    if A.next is None:
        return A
    pre_node = A
    c_node = pre_node.next

    swap = True
    while swap:
        swap = False
        while c_node is not None:
            if c_node.val < pre_node.val:
                swap = True
                temp = c_node
                pre_node.next = c_node.next
                A = insert_list(A, temp)
                pre_node = A
                c_node = pre_node.next
            else:
                c_node = c_node.next
                pre_node = pre_node.next
            print_node(A)
        pre_node = A
        c_node = pre_node.next
    return A

#test

lnode = ListNode(6)
lnode.next = ListNode(2)
lnode.next.next = ListNode(3)
lnode.next.next.next = ListNode(4)
lnode.next.next.next.next = ListNode(7)
lnode.next.next.next.next.next = ListNode(5)
print_node(lnode)
print_node(sort_list(lnode))

