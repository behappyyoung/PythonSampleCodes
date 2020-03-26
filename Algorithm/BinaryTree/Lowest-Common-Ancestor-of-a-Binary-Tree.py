"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5,
since a node can be a descendant of itself according to the LCA definition

"""


lca_node = None
def lca(root, p, q):
    if not root:
        return root

    def helper(node, p, q):
        global lca_node
        if not node:
            return False

        l = helper(node.left, p, q)

        r = helper(node.right, p, q)

        m = node.val == p or node.val == q

        print(node.val, l, r, lca_node)
        if l + r + m >= 2:
            lca_node = node
            print(node.val, l, r, lca_node)

        return l or r or m

    helper(root, p, q)
    return lca_node

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
print(lca(t, 6, 7))