"""

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]

"""

def postorderTraversal(root):
    tree_arr = []
    if not root:
        return []

    if root.left is not None:
        tree_arr.extend(postorderTraversal(root.left))

    if root.right is not None:
        tree_arr.extend(postorderTraversal(root.right))
    tree_arr.append(root.val)
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
print(postorderTraversal(t))