"""
[4, 1, 3, 6, 7, 1, 13, 3, 5, 9]

==>
[6, 3, 6, 7, 13, 13, -1, 5, 9, -1]

"""

def get_next_big_number(arr):
    if not arr:
        return []
    s = list()              # set of value, location
    l = len(arr)
    r_arr = [-1]*l
    s.append((arr[0], 0)) # set of value, location
    for i in range(1, l):
        cur = arr[i]
        while s and s[-1][0] < cur:
                pre = s.pop()
                r_arr[pre[1]] = cur
        s.append((cur, i))

    for rem in s:
        r_arr[rem[1]] = -1

    return r_arr


s = [4, 1, 3, 6, 7, 1, 13, 3, 5, 9]
print(get_next_big_number(s))
s = [2, 1, 1, 1, 1, 4, 5, 1, 1, 2, 9, 1]
print(get_next_big_number(s))