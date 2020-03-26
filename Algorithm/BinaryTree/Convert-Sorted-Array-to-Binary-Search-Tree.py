"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which
the depth of the two subtrees of every node never differ by more than 1.
Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5


"""

def sortedArray_to_BST(nums):

    def helper(arr):
        if not arr:
            return None
        l = len(arr)
        if l == 1:
            return TreeNode(arr[0])

        m = l // 2
        print(arr, m)

        root = TreeNode(arr[m])
        root.left = helper(arr[:m])
        root.right = helper(arr[m+1:])

        # print_btree(root)
        return root

    return helper(nums)

from _BinaryTree import TreeNode, print_btree

input_array = [-10,-3,0,5,9]
bst = sortedArray_to_BST(input_array)
print_btree(bst)

print_btree(TreeNode('[]'))