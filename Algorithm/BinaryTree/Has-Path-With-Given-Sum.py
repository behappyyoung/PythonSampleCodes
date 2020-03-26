"""
Given a binary tree t and an integer s,
determine whether there is a root to leaf path in t such that the sum of vertex values equals s


"""

def hasPathWithGivenSum(t, s):
    lhasSum = False
    rhasSum = False

    if not t:
        return False
    elif t.left == None and t.right == None:
        return t.val == s

    if t.left:
        lhasSum = hasPathWithGivenSum(t.left, s - t.val)
    if t.right:
        print(t.val)
        rhasSum = hasPathWithGivenSum(t.right, s - t.val)

    return lhasSum or rhasSum

from _BinaryTree import TreeNode, print_btree

t = TreeNode(1)
t.left = TreeNode(2)
t3 = TreeNode(3)
t.right = t3
t7 = TreeNode(7)
t3.right = t7
t3.left = TreeNode(6)
t7.right = TreeNode(9)

print_btree(t)
print(hasPathWithGivenSum(t, 10))