"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

  2
   / \
  1   3

Input: [2,1,3]
Output: true

 5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

 20
    /  \
  10    30
       /  \
      5    40

false

"""


def isBST(root):
    def helper(node, lower=float('-inf'), upper=float('inf')):
        if not node:
            return True
        c_val = node.val
        if c_val <= lower or c_val >= upper:
            return False
        if not helper(node.right, c_val, upper):
            return False
        if not helper(node.left, lower, c_val):
            return False
        return True

    return helper(root)

from _BinaryTree import TreeNode, print_btree

t = TreeNode(2)
t.left = TreeNode(1)
t3 = TreeNode(16)
t.right = t3
t7 = TreeNode(17)
t3.right = t7
t3.left = TreeNode(3)
t7.right = TreeNode(19)

print_btree(t)
print(isBST(t))


t = TreeNode(10)
t.left = TreeNode(5)
t2 = TreeNode(15)
t.right = t2
t2.left = TreeNode(9)
t2.right = TreeNode(19)

print_btree(t)
print(isBST(t))