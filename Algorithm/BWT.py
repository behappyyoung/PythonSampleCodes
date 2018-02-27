
class BWT:

    def __init__(self):
        self.in_str = ''
        self.str_L = ''
        self.str_F = ''
        self.L = ''
        self.F = ''
        self.init_I = 0
        self.str_l = 0
        self.sorted_list = []
        self.re_str = ''

    def get_str(self, str):
        self.in_str = str
        self.str_l = len(str)

    def create_bwt(self):
        new_s = self.in_str
        for i in range(0, self.str_l):
            new_s = new_s[-1]+new_s[:-1]
            self.sorted_list.append(new_s)
        self.sorted_list.sort()
        for i in range(0, self.str_l):
            if self.sorted_list[i] == self.in_str:
                self.init_I = i
            self.str_L = self.str_L + self.sorted_list[i][-1]
            self.str_F = self.str_F + self.sorted_list[i][0]

    def get_sorted_rows(self, s, s_list, forward=0):
        s_l = len(s_list)
        row_list = []
        min = 'z'
        for i in range(0, s_l):
            cur_list = s_list[i] + forward if s_list[i] + forward < self.str_l else s_list[i] + forward - self.str_l
            cur = s[cur_list]
            if cur <= min:
                min = cur

        print(min)
        for i in range(0, s_l):
            cur_list = s_list[i] + forward if s_list[i] + forward < self.str_l else s_list[i] + forward - self.str_l
            cur = s[cur_list]
            if cur == min:
                row_list.append(i)

        return row_list

    def get_row_list(self, s_list):

        new_pos_list = s_list

        for i in range(0, len(new_pos_list)):
            old_pos_list = new_pos_list
            new_pos_list = self.get_sorted_rows(self.in_str, old_pos_list, i)
            print(new_pos_list)
            if len(new_pos_list) == 1 or new_pos_list == old_pos_list:
                return new_pos_list

    def create_bwt_without_list(self):
        start_pos_list = []

        for i in range(0, self.str_l):
            start_pos_list.append(i)

        print(start_pos_list)

        new_pos_list = start_pos_list
        my_f_list = []
        while len(start_pos_list):
            my_f_list.extend(self.get_row_list(new_pos_list))
            for i in new_pos_list:
                start_pos_list.remove(i)

            new_pos_list = start_pos_list
            print(new_pos_list)

        print(my_f_list)
        for i in range(0, self.str_l):
            if self.sorted_list[i] == self.in_str:
                self.init_I = i
            self.str_L = self.str_L + self.sorted_list[i][-1]
            self.str_F = self.str_F + self.sorted_list[i][0]

    def find_T_from_F(self, str, k):
        for i in range(0, self.str_l):
            if str == self.str_F[i]:
                if k == 0:
                    return i
                k = k - 1
        return -1

    def find_T(self):
        l_dict = {}
        t = []
        for i in range(0, self.str_l):
            cur = self.str_L[i]
            if l_dict.get(cur):
                t.append(self.find_T_from_F(cur, l_dict[cur]))
                l_dict[cur] = l_dict[cur] + 1
            else:
                t.append(self.find_T_from_F(cur, 0))
                l_dict[cur] = 1

        return t

    def revert_bwt(self):
        t_list = self.find_T()
        s = ''
        cur = self.init_I
        for i in range(self.str_l, 0, -1):
            cur = t_list[cur]
            s = self.str_F[cur] + s
        self.re_str = s

