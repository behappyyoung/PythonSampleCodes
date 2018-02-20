import sys
in_str = sys.stdin.read().strip()

l = len(in_str)
print(in_str, '==============', l)


def create_bwt(s):
    sorted_list=[]
    new_s = s
    for i in range(0,l):
        new_s = new_s[-1]+new_s[:-1]
        sorted_list.append(new_s)
    sorted_list.sort()
    # print(sorted_list)
    L = ''
    F = ''
    for i in range(0, len(sorted_list)):
        if sorted_list[i] == s:
            I = i
        L = L + sorted_list[i][-1]
        F = F + sorted_list[i][0]
    return F, L, I


def get_sorted_rows(s):
    return False


def create_bwt_without_list(s):
    return False


(str_F, str_L, init_I) = create_bwt(in_str)

print(str_F, str_L, init_I)


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