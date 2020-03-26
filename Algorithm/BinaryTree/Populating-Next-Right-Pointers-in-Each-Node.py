"""
#https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/994/

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.
The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node.
If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A),
your function should populate each next pointer to point to its next right node, just like in Figure B.

The serialized output is in level order as connected by the next pointers,
with '#' signifying the end of each level.


"""

# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __str__(self):
            return str(self.val)

def print_btree(root):
    current_level = [root]
    while current_level:
        print(' '.join('-' if node == '-' else str(node.val) +':'+ str(node.next) for node in current_level))
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

def connect(root):
    """
    :type root: Node
    :rtype: Node
    """
    top = root
    left = top.left
    c_next = top
    while left:
        left.next = c_next.right
        c_next = c_next.next
        if c_next:
            left = left.next
            left.next = c_next.left
            left = left.next
        else:
            top = top.left
            left = top.left
            c_next = top
    r_arr = list()
    while root:
            c_root = root
            r_arr.append(c_root.val)
            while c_root.next:
                c_root = c_root.next
                r_arr.append(c_root.val)
            r_arr.append('#')
            root = root.left
    return r_arr

t = Node(1)
t2 = Node(2)
t.left = t2
t3 = Node(3)
t.right = t3
t4 = Node(4)
t5 = Node(5)
t2.left = t4
t2.right = t5
t6 = Node(6)
t7 = Node(7)
t3.left = t6
t3.right = t7


#
t4.left = Node(8)
t4.right = Node(9)
t5.left = Node(10)
t5.right = Node(11)
t6.left = Node(12)
t6.right = Node(13)
t7.left = Node(14)
t7.right = Node(15)
# print_btree(t)
# print(connect(t))
# print_btree(t)


def connectNotPerfectTree(root):
    """
    :type root: Node
    :rtype: Node
    """
    top = root
    left = top.left
    c_next = top
    skip = False
    while left:
        if c_next.left and c_next.right:
            left.next = c_next.right
        else:
            skip = True
        c_next = c_next.next
        if c_next:
            if not skip:
                left = left.next
            if c_next.left:
                left.next = c_next.left
            else:
                left.next = c_next.right
            left = left.next
        else:
            top = top.left
            if top.left:
                left = top.left
            else:
                left = top.right
            c_next = top
        skip = False
    r_arr = list()
    while root:
            c_root = root
            r_arr.append(c_root.val)
            while c_root.next:
                c_root = c_root.next
                r_arr.append(c_root.val)
            r_arr.append('#')
            root = root.left
    return r_arr



t = Node(1)
t2 = Node(2)
t.left = t2
t3 = Node(3)
t.right = t3
t4 = Node(4)
t5 = Node(5)
t2.left = t4
t2.right = t5
t6 = Node(6)
t7 = Node(7)
# t3.left = t6
t3.right = t7


#
t4.left = Node(8)
# t4.right = Node(9)
t5.left = Node(10)
t5.right = Node(11)
t6.left = Node(12)
t6.right = Node(13)
# t7.left = Node(14)
t7.right = Node(15)
print_btree(t)
print(connectNotPerfectTree(t))
print_btree(t)