import sys
in_str = sys.stdin.read().strip()

import re
in_str = re.sub(r'\W+', '', in_str)

import timeit
start = timeit.default_timer()

l = len(in_str)
print(in_str, '==============', l)


def create_bwt():
    sorted_list=[]
    new_s = in_str
    for i in range(0,l):
        new_s = new_s[-1]+new_s[:-1]
        sorted_list.append(new_s)
    sorted_list.sort()
    # print(sorted_list)
    L = ''
    F = ''
    for i in range(0, len(sorted_list)):
        if sorted_list[i] == in_str:
            I = i
        L = L + sorted_list[i][-1]
        F = F + sorted_list[i][0]
    return F, L, I


def get_sorted_rows(s, s_list, forward=0):
    s_l = len(s_list)
    row_list = []
    min = 'z'
    for i in range(0,s_l):
        cur_list = s_list[i] + forward if s_list[i] + forward < l else s_list[i] + forward - l
        cur = s[cur_list]
        if cur <= min:
            min = cur

    print(min)
    for i in range(0, s_l):
        cur_list = s_list[i] + forward if s_list[i] + forward < l else s_list[i] + forward - l
        cur = s[cur_list]
        if cur == min:
            row_list.append(i)

    return row_list


def get_row_list(s_list):

    new_pos_list = s_list

    for i in range(0, len(new_pos_list)):
        old_pos_list = new_pos_list
        new_pos_list = get_sorted_rows(in_str, old_pos_list, i)
        print(new_pos_list)
        if len(new_pos_list) == 1 or new_pos_list == old_pos_list:
            return new_pos_list


def create_bwt_without_list():
    sorted_list = []
    start_pos_list = []

    for i in range(0, l):
        start_pos_list.append(i)

    print(start_pos_list)

    new_pos_list = start_pos_list
    my_f_list = []
    while len(start_pos_list):
        my_f_list.extend(get_row_list(new_pos_list))
        for i in new_pos_list:
            start_pos_list.remove(i)

        new_pos_list = start_pos_list
        print(new_pos_list)

    print(my_f_list)
    L = ''
    F = ''
    I = 0
    for i in range(0, len(sorted_list)):
        if sorted_list[i] == in_str:
            I = i
        L = L + sorted_list[i][-1]
        F = F + sorted_list[i][0]
    return F, L, I


(str_F, str_L, init_I) = create_bwt()

print(str_F, str_L, init_I)
print(create_bwt_without_list())


def find_T_from_F(str, k):
    for i in range(0, l):
        if str == str_F[i]:
            if k == 0:
                return i
            k = k - 1
    return -1


def find_T():
    l_dict = {}
    t = []
    for i in range(0, l):
        cur = str_L[i]
        if l_dict.get(cur):
            t.append(find_T_from_F(cur, l_dict[cur]))
            l_dict[cur] = l_dict[cur] + 1
        else:
            t.append(find_T_from_F(cur, 0))
            l_dict[cur] = 1

    return t


t = find_T()

print(t)


def revert_bwt(t_list, I):
    s = ''
    cur = I
    for i in range(l, 0, -1):
        cur = t_list[cur]
        s = str_F[cur] + s
        # print(cur, s)
    return s


print(revert_bwt(t, init_I))
stop = timeit.default_timer()
print(stop-start)
