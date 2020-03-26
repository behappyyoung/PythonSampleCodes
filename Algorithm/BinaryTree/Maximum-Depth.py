"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

output : 3

1 : 1
2 - 3 : 2
4 - 7 : 3
8 - 15: 4

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def traverse(root):
    current_level = [root]
    while current_level:
        print(' '.join(str(node.val) for node in current_level))
        next_level = list()
        for n in current_level:
            if n.left:
                next_level.append(n.left)
            if n.right:
                next_level.append(n.right)
        current_level = next_level


def max_depth(root):
    if not root:
        return 0
    if root.left is None and root.right is None:
        return 1
    else:
        depth = max(max_depth(root.left), max_depth(root.right)) + 1
        return depth

t = TreeNode(1)
t.left = TreeNode(2)
t3 = TreeNode(3)
t.right = t3
t7 = TreeNode(7)
t3.right = t7
t3.left = TreeNode(6)
t7.right = TreeNode(9)

traverse(t)
print(max_depth(t))