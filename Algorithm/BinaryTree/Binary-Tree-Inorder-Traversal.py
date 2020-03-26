"""

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]

"""

def inorderTraversal(root):
    tree_arr = []
    if not root:
        return []

    if root.left is not None:
        tree_arr.extend(inorderTraversal(root.left))
    tree_arr.append(root.val)
    if root.right is not None:
        tree_arr.extend(inorderTraversal(root.right))
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