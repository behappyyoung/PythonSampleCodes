"""
Given a BST node, return the node which has value just greater than the given node.
                103

        98              105

    97       99


 96                 101

            100             102


 (t, 97)    => 98
 (t, 99)    => 100
==> inorder traversal O(n)

==> O(h)

    def getSuccessor(self, A, B):
        root = A
        succ = root
        while root.val != B:
            if B < root.val:
                succ = root
                root = root.left
            else:
                root = root.right
        if root.right != None:
            root = root.right
            while root.left!=None:
                    root = root.left
            return root
        else:
            if succ.val <= B:
                return None
            else:
                return succ

"""
def find_next_greater(A, B):
    root = A
    c_node = root
    while c_node.val != B:
        if c_node.val < B:
            root = c_node
            c_node = c_node.right
        else:
            c_node = c_node.left

    if c_node.right:
        c_node = c_node.right
        while c_node.left:
            c_node = c_node.left
        return c_node
    else:
        return c_node


from _BinaryTree import TreeNode, print_btree

t = TreeNode(2)
t.left = TreeNode(1)
t6 = TreeNode(6)
t.right = t6
t7 = TreeNode(7)
t6.right = t7
t3 = TreeNode(3)
t6.left = t3
t3.right = TreeNode(4)
t7.right = TreeNode(9)

print_btree(t)
r_t = find_next_greater(t, 2)
print_btree(r_t)