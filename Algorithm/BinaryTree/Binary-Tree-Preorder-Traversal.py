"""

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]

"""


def preorder_traverse(node):
    tree_arr = []
    if not node:
        return []
    tree_arr.append(node.val)
    if node.left is not None:
            # tree_arr.append(node.left.val)
            tree_arr.extend(preorder_traverse(node.left))
    if node.right is not None:
            # tree_arr.append(node.right.val)
            tree_arr.extend(preorder_traverse(node.right))
    return tree_arr

from _BinaryTree import TreeNode, print_btree

t = TreeNode(1)
t2 = TreeNode(2)
t.left = t2
t2.right = TreeNode(22)
t3 = TreeNode(3)
t.right = t3
t7 = TreeNode(7)
t3.right = t7
t3.left = TreeNode(6)
t7.right = TreeNode(9)

print_btree(t)
print(preorder_traverse(t))