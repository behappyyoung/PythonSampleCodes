"""
Given a binary tree, determine if it is height-balanced.
Height-balanced binary tree :
is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1

Return 0 / 1 ( 0 for false, 1 for true ) for this problem

Input :
          1
         / \
        2   3

Return : True or 1

Input 2 :
         3
        /
       2
      /
     1

Return : False or 0
         Because for the root node, left subtree has depth 2 and right subtree has depth 0.
         Difference = 2 > 1.

"""


def isBalanced(root):
    if not root:
        return True
    if root.left is None and root.right is not None:
        if root.right.left is None and root.right.right is not None:
            if root.right.right.left or root.right.right.right:
                return False
        elif root.right.left is not None and root.right.right is None:
            if root.right.left.left or root.right.left.right:
                return False
    elif root.left is not None and root.right is None:
        if root.left.left is None and root.left.right is not None:
            if root.left.right.left or root.left.right.right:
                return False
        elif root.left.left is not None and root.left.right is None:
            if root.left.left.left or root.left.left.right:
                return False
    else:
        # print(root.val, isBalanced(root.left), root.val, isBalanced(root.right))
        if isBalanced(root.left) and isBalanced(root.right):
            return True
        else:
            return False

from _BinaryTree import TreeNode, print_btree

t = TreeNode(1)
t.left = TreeNode(2)
t3 = TreeNode(3)
t.right = t3
t7 = TreeNode(7)
t3.right = t7
t3.left = TreeNode(6)
t7.right = TreeNode(9)

print_btree(t)
print(isBalanced(t))