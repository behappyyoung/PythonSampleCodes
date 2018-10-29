class SuffixTree(object):

    def __init__(self, in_str):
        global g_end
        g_end = 1
        self.suffix_tree = []
        self.active_node = 0
        self.active_edge = 0
        self.active_length = 0
        self.remainder = 0
        self.current_leaf = 1
        self.current_edge = 0
        self.in_str = in_str

    def __repr__(self):
        # global g_end
        return "in string:%s, tree:%s, end: %s, node:%s, edge:%s, length:%s, remainder%s" \
               % (self.in_str, self.suffix_tree,g_end,  self.active_node, self.active_edge, self.active_length, self.remainder)

    class Node(object):
        def __init__(self, suffix_node, start_index, end_index, node_start, node_end=None):
            self.suffix_node = suffix_node
            self.start_index = start_index
            self.end_index = end_index
            self.node_start = node_start
            self.node_end = node_end

        def __repr__(self):
            global g_end
            return "Node String: %s, start index: %d, end index: %s, node start: %s, node end: %s" \
                   % (self.suffix_node, self.start_index, self.end_index if self.end_index else g_end, self.node_start, self.end_index if self.end_index else g_end)

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

    def update_suffix_tree(self, cur_index):
        global g_end
        new_input = True
        new_node = False
        cur_char = self.in_str[cur_index]
        g_end = g_end + 1
        for i in self.suffix_tree:

            i.suffix_node = i.suffix_node + cur_char

            if self.active_edge != 0:
                if self.active_edge == i.node_start:
                    if self.active_length > 0:
                        if self.in_str[self.active_edge:self.active_edge+self.active_length] == self.in_str[i.node_start:i.node_start+self.active_length]:
                            self.active_length = self.active_length + 1
                            self.remainder = self.remainder + 1
                        else:

                            # split

                            if self.remainder > 1:
                                self.active_edge = self.active_edge + 1
                                self.active_length = self.active_length - 1
                                self.remainder = self.remainder - 1
                            else:
                                i.node_end = i.node_start + self.active_length
                                self.active_length = self.active_length - 1
                                self.remainder = self.remainder - 1
                                self.active_edge = 0
                    else:
                        self.active_length = self.active_length + 1
                        self.remainder = self.remainder + 1

            elif self.in_str[i.node_start] == self.in_str[cur_index]:
                    new_input = False
                # if i.suffix_node[:self.active_length+1]:
                    self.active_edge = cur_index
                    self.active_length = self.active_length + 1
                    self.remainder = self.remainder + 1

        print('add', cur_char, new_input)
        if new_input:

            new_node = self.Node(cur_char, self.active_node, None, cur_index, None)
            self.suffix_tree.append(new_node)

        else:

            if self.suffix_tree[self.active_node]:
                pass

    def build_suffix(self):
        new_node = self.Node(self.in_str[0], 0, None, 0, None)
        self.suffix_tree.append(new_node)
        for i in range(1, len(self.in_str)):
            self.update_suffix_tree(i)

    def find_substring(self, substring):
        for i in self.suffix_tree:
            print(i)