"""
Reverse a linked list



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

def reverse_link_list(head_node):

    c_node = head_node
    next_node = head_node.next
    while c_node.next is not None:
        c_node.next = next_node.next
        next_node.next = head_node
        head_node = next_node
        next_node = c_node.next

    return head_node

#test


lnode = ListNode('1')
lnode.next = ListNode('2')
lnode.next.next = ListNode('3')
lnode.next.next.next = ListNode('4')
lnode.next.next.next.next = ListNode('5')
print_node(lnode)
print_node(reverse_link_list(lnode))

