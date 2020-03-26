"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer,
or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

"""


def serialize_btree(root):
    current_level = [root]
    s_arr = []
    fake_node = TreeNode(None)
    while current_level:
        next_level = list()
        has_next = False
        for n in current_level:
            s_arr.append(n.val)
            if n.left:
                has_next = True
                next_level.append(n.left)
            else:
                next_level.append(fake_node)
            if n.right:
                has_next = True
                next_level.append(n.right)
            else:
                next_level.append(fake_node)
        if has_next:
            current_level = next_level
        else:
            current_level = None
    return s_arr

def deserialize_btree(arr):
    if not arr:
        return []
    root = TreeNode(arr[0])
    c_root = root
    i = 1
    q = list()
    while i < len(arr):
        c_root.left = TreeNode(arr[i])
        q.append(c_root.left)
        i += 1
        c_root.right = TreeNode(arr[i])
        q.append(c_root.right)
        i += 1
        c_root = q.pop(0)

    print_btree(root)
    return root

    # def build_tree(arr, current_count):
    #     if not arr:
    #         return []
    #     if len(arr) <= current_count:
    #         return None
    #     node = TreeNode(arr[current_count])
    #     current_count += 1
    #     node.left = build_tree(arr, current_count)
    #     current_count += 1
    #     node.right = build_tree(arr, current_count)
    #     current_count += 1
    #
    #     return node
    #
    # root = build_tree(arr, 0)
    # print_btree(root)
    # return root




from _BinaryTree import TreeNode, print_btree

t = TreeNode(1)
t.left = TreeNode(2)
t3 = TreeNode(3)
t.right = t3
t7 = TreeNode(5)
t3.right = t7
t3.left = TreeNode(4)
# t7.right = TreeNode(9)
print_btree(t)
st = serialize_btree(t)
print(st)
dt = deserialize_btree(st)
print(dt)
