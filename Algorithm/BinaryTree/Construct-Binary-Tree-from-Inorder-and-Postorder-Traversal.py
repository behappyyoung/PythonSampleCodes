"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

  3
   / \
  9  20
    /  \
   15   7


"""
from _BinaryTree import TreeNode, print_btree

def buildTree(inorder, postorder):
    if not inorder or not postorder:
        return None

    head_node = TreeNode(postorder.pop())

    inorder_index = inorder.index(head_node.val)
    # print(inorder, postorder, inorder_index, head_node.val)
    head_node.left = buildTree(inorder[:inorder_index], postorder[:inorder_index])
    head_node.right = buildTree(inorder[inorder_index+1:], postorder[inorder_index:])
    return head_node

h = buildTree([9,3,15,20,7], [9,15,7,20,3])
print_btree(h)

h = buildTree([1,9,2,3,15,20,7], [1,2,9,15,7,20,3])
print_btree(h)