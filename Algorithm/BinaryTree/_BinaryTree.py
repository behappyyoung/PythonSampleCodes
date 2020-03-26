# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    # def __repr__(self):
    #         return "TreeNode"

    def __str__(self):
            return str(self.val)

def print_btree(root):
    current_level = [root]
    while current_level:
        print(' '.join('-' if node == '-' else str(node.val) for node in current_level))
        next_level = list()
        for n in current_level:
            if n == '-':
                continue
            if n.left:
                next_level.append(n.left)
            else:
                next_level.append('-')
            if n.right:
                next_level.append(n.right)
            else:
                next_level.append('-')
        current_level = next_level

# def serialize_btree(root):
#     r_arr = list()
#     while root:
#             c_root = root
#             r_arr.append(c_root.val)
#             while c_root.next:
#                 c_root = c_root.next
#                 r_arr.append(c_root.val)
#             r_arr.append('#')
#             root = root.left
#     return r_arr
#
# def deserialize_btree(arr):
#     if not arr:
#         return []
#     def make_btree(c_arr, level):
#         node = TreeNode(c_arr[0])
#
#         for i in range(1, len(arr)):
#             node.left = TreeNode(arr[i]) if arr[i] != '#' else None
#
