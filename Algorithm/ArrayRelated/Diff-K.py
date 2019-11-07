"""

input
A : [1 3 5]
    k : 4
output
1 yes ( 5-1 = 4)

diff_k => Memory Limit Exceeded.

"""

def diff_k(arr, k):
    if len(arr) < 2:
        return 0
    elif len(arr) == 2:
        if arr[1] - arr[0] == k:
            return 1
        else:
            return 0
    if diff_k(arr[:-1], k):
        return 1
    else:
        for i in range(len(arr)-1):
            if arr[-1] - arr[i] == k:
                return 1

        return 0

def diff_k_s(arr, k):
    if len(arr) < 2:
        return 0
    elif len(arr) == 2:
        if arr[1] - arr[0] == k:
            return 1
        else:
            return 0
    r = len(arr) -1
    while r > 1:
        for l in range(r):
            c_diff = arr[r] - arr[l]
            if  c_diff == k:
                return 1
            elif c_diff < k:
                break
        r -= 1
    return 0
# test
input_arr = [1, 2, 4, 7, 9, 11]
k = 5
print(diff_k(input_arr, k))
print(diff_k_s(input_arr, k))



