"""

Given a binary search tree, write a function to find the kth smallest element in the tree

Input :
  2
 / \
1   3

and k = 2

Return : 2

As 2 is the second smallest element in the BST tree.

1 <= k <= Total


"""


def find_kth_bst(root, k):
    # Using Inorder Traversal.
    tree_arr = []
    def inorder_traversal(t):
        if t.left is not None:
            inorder_traversal(t.left)
        tree_arr.append(t.val)
        if t.right is not None:
            inorder_traversal(t.right)

    inorder_traversal(root)
    print(tree_arr)
    return tree_arr[k-1]

from _BinaryTree import TreeNode, print_btree

t = TreeNode(3)
t.left = TreeNode(2)
t5 = TreeNode(5)
t.right = t5
t7 = TreeNode(7)
t5.right = t7
t5.left = TreeNode(4)
t7.right = TreeNode(9)


print_btree(t)
# print(find_small(t))

print(find_kth_bst(t, 4))