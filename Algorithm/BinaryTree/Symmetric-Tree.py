"""
1
   / \
  2   2
 / \ / \
3  4 4  3

True

1
   / \
  2   2
   \   \
   3    3

False

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

t = TreeNode(2)
t.left = TreeNode(1)
t3 = TreeNode(16)
t.right = t3
t7 = TreeNode(17)
t3.right = t7
t3.left = TreeNode(3)
t7.right = TreeNode(19)

print_btree(t)
print(isSymmetric(t))


t = TreeNode(10)
t2 = TreeNode(15)
t3 = TreeNode(15)
t.right = t3
t.left = t2
t2.left = TreeNode(9)
t2.right = TreeNode(19)
t3.left = TreeNode(19)
t3.right = TreeNode(9)

print_btree(t)
print(isSymmetric(t))