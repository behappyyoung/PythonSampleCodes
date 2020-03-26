"""
Given a sorted linked list, delete all duplicates such that each element appear only once.


For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3


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
        print_str += '->' + c_node.val
        c_node = c_node.next
    print(print_str)

########################

def remove_duplicate(head_node):
    c_node = head_node
    exist_dict={c_node.val: True}

    while c_node.next is not None:
        next_node = c_node.next
        if next_node.val in exist_dict:
            c_node.next = next_node.next
        else:
            exist_dict[next_node.val]=True
            c_node = next_node

    return head_node

#test


lnode = ListNode('1')
lnode.next = ListNode('2')
lnode.next.next = ListNode('1')
lnode.next.next.next = ListNode('2')
lnode.next.next.next.next = ListNode('1')
print_node(lnode)
print_node(remove_duplicate(lnode))
print_node(lnode)

# lnode = ListNode('10')
# lnode.next = ListNode('7')
# lnode.next.next = ListNode('10')
# print_node(lnode)
# print(remove_duplicate(lnode))
# print_node(lnode)