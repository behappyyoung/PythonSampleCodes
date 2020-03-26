"""

Given a binary search tree, write a function to find the kth smallest element in the tree

Input :
  2
 / \
1   3

and k = 2

Return : 2

As 2 is the second smallest element in the tree.

1 <= k <= Total

"""
class LinkNode:
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


def traverse(root):
    current_level = [root]
    while current_level:
        print(' '.join(str(node.val) for node in current_level))
        next_level = list()
        for n in current_level:
            if n.left:
                next_level.append(n.left)
            if n.right:
                next_level.append(n.right)
        current_level = next_level

def traverse_s(root):
    current_level = [root]
    while current_level:
        print(' '.join('-' if node == '-' else str(node.val) for node in current_level))
        next_level = list()
        for n in current_level:
            if n == '-':
                continue
            if n.left:
                next_level.append(n.left)
            else:
                next_level.append('-')
            if n.right:
                next_level.append(n.right)
            else:
                next_level.append('-')
        current_level = next_level


# ================================================

def add_linkedlist(head, new_value):
    head_pin = head
    newnode = LinkNode(new_value)
    swap = False
    while head.next and not swap:
        if new_value < head.next.val:
            newnode.next = head.next
            head.next = newnode
            swap = True
        else:
            head = head.next

    if not swap:
        head.next = newnode

    return head_pin

def make_linkedlist(l, root):
    if not root:
        return l

    l = add_linkedlist(l, root.val)

    if root.left:
        l = make_linkedlist(l, root.left)
    if root.right:
        l = make_linkedlist(l, root.right)

    return l

def find_kth(root, k):
    head = LinkNode(0)
    head = make_linkedlist(head, root)
    i = 0
    print_node(head)
    while i < k and head.next:
        head = head.next
        i += 1
    return head.val

from _BinaryTree import TreeNode, print_btree

t = TreeNode(10)
t.left = TreeNode(2)
t3 = TreeNode(13)
t.right = t3
t7 = TreeNode(7)
t3.right = t7
t3.left = TreeNode(6)
t7.left = TreeNode(9)


traverse_s(t)
# print(find_small(t))

print(find_kth(t, 4))