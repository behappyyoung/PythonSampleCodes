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

# double linked list
class DoubleNode:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

# def print_doublenode(head_node):
    