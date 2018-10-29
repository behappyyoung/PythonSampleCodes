import sys
in_str = sys.stdin.read().strip()

print(in_str)

suffix_tree = []
active_node = 0
active_edge = None
active_length = 0
remainder = 0
current_leaf = 1


class Node(object):

    def __init__(self, suffix_node, start_index, end_index):
        self.suffix_node = suffix_node
        self.start_index = start_index
        self.end_index = end_index

    def __repr__(self):
        return "Node String: %s" % self.suffix_node

    def add_ch(self, ch):
        self.suffix_node = self.suffix_node + ch

    def remove_substr(self, substr):
        self.suffix_node = self.suffix_node.split(substr)[1]


def char_in_str(ch, s_list):
    for s in s_list:
        if ch == s[0]:
            return s
    return False


def add_char(ch, s_list):
    new_list = {}
    for s in s_list:
        new_str = s + ch
        print(s, ch, new_str)
        new_list[new_str] = s_list.get(s)
    return new_list


def split_str(sub_list_str):
    ## split
    print(current_leaf, sub_list_str)
    suffix_tree[active_edge] = current_leaf + 1

    # current_leaf = current_leaf + 1
    # suffix_tree[s] = current_leaf


def update_suffix_tree(cur_ch):
    for i in suffix_tree:
        print i.Node.suffix_node


for cur_ch in in_str:
    update_suffix_tree(cur_ch)


print(suffix_tree, active_node, active_edge, active_length, remainder)