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

def remove_nth_node_from_last(head_node, n):

    c_node = head_node
    node_length = 0
    while c_node is not None:
        node_length += 1
        c_node = c_node.next
    if node_length <=1:
        return None
    elif node_length <= n:
        head_node = head_node.next
        return head_node

    c_node = head_node
    for i in range(node_length-n-1):
        c_node = c_node.next
    c_node.next = c_node.next.next
    return head_node

#test


lnode = ListNode('1')
lnode.next = ListNode('2')
lnode.next.next = ListNode('3')
lnode.next.next.next = ListNode('4')
lnode.next.next.next.next = ListNode('5')
print_node(lnode)
print_node(remove_nth_node_from_last(lnode, 5))

# lnode = ListNode('10')
# lnode.next = ListNode('7')
# lnode.next.next = ListNode('10')
# print_node(lnode)
# print(remove_duplicate(lnode))
# print_node(lnode)