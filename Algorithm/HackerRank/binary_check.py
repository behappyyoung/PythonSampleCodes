def check_binary(node, min, max):
    if node is None:
        return True
    if node.data <= min or node.data >= max:
        return False
    
    if node.left is not None:
        if not check_binary(node.left, min , node.data):
            return False
    if node.right is not None:
        if not check_binary(node.right, node.data, max):
            return False
        
    return True


def check_binary_search_tree_(root):
    return check_binary(root, 0, 100000)
