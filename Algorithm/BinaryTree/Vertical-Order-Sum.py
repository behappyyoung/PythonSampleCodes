"""

"""


def vertical_sum_btree(root):
    s_arr = list()
    current_level = [root]
    while current_level:
        next_level = list()
        has_next = False
        c_sum = 0
        for n in current_level:
            c_sum += n.val
            if n.left:
                has_next = True
                next_level.append(n.left)
            if n.right:
                has_next = True
                next_level.append(n.right)
        current_level = next_level
        s_arr.append(c_sum)

    return s_arr



from _BinaryTree import TreeNode, print_btree

t = TreeNode(1)
t.left = TreeNode(2)
t3 = TreeNode(3)
t.right = t3
t7 = TreeNode(5)
t3.right = t7
t3.left = TreeNode(4)
t7.right = TreeNode(9)
print_btree(t)
vs = vertical_sum_btree(t)
print(vs)
