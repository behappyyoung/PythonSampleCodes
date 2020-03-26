"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

  3
   / \
  9  20
    /  \
   15   7


"""
from _BinaryTree import TreeNode, print_btree

def buildTree(preorder, inorder):
    if not inorder or not preorder:
        return None
    head_node = TreeNode(preorder[0])
    inorder_index = inorder.index(head_node.val)
    head_node.left = buildTree(preorder[1:inorder_index+1], inorder[:inorder_index])
    head_node.right = buildTree(preorder[inorder_index+1:], inorder[inorder_index+1:])
    return head_node

h = buildTree([3,9,20,15,7], [9,3,15,20,7])
print_btree(h)
