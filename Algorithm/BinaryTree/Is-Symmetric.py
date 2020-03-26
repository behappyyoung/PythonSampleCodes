"""
Given a binary tree t, determine whether it is symmetric around its center,
 i.e. each side mirrors the other.
Return 0 / 1 ( 0 for false, 1 for true ) for this problem

Input :
          1
         / \
        2   2

Return : True or 1

Input 2 :
          3
        /  \
       2     2
      /\    / \
    1  3  3   2

Return : False or 0


"""


def isSymmetric(root):

    def helper(left_node, right_node):
        if not left_node and not right_node:
            return True
        elif not left_node and right_node:
            return False
        elif left_node and not right_node:
            return False

        if left_node.val != right_node.val:
            return False

        if not helper(left_node.right, right_node.left):
            return False

        if not helper(left_node.left, right_node.right):
            return False

        return True

    return helper(root.left, root.right)

from _BinaryTree import TreeNode, print_btree

t = TreeNode(1)
t2 = TreeNode(2)
t.left = t2
t3 = TreeNode(2)
t.right = t3
t7 = TreeNode(7)
t3.right = t7
t2.left = t7
t7.right = TreeNode(9)
t7.left = TreeNode(9)

print_btree(t)
print(isSymmetric(t))