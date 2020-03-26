"""

    3
   / \
  9  20
    /  \
   15   7

Output: [
  [3],
  [9,20],
  [15,7]
]

"""


def levelOrder(root):
    tree_arr = []
    if not root:
        return []
    current_level = [root]
    while current_level:

        tree_arr.append([x.val for x in current_level])
        next_level = []
        for c in current_level:
            if c.left:
                next_level.append(c.left)
            if c.right:
                next_level.append(c.right)
        current_level = next_level
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
print(inorderTraversal(t))