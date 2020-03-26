"""
Input  : arr[] = {3, 10, 2, 1, 20}
Output : Length of LIS = 3
The longest increasing subsequence is 3, 10, 20

Input  : arr[] = {3, 2}
Output : Length of LIS = 1
The longest increasing subsequences are {3} and {2}

Input : arr[] = {50, 3, 10, 7, 40, 80}
Output : Length of LIS = 4
The longest increasing subsequence is {3, 7, 40, 80}

"""
# global t_max

def longest_subsequence(arr):
    if not arr:
        return 0
    global t_max
    t_max = 1
    # max_list = {}
    def helper(arr, n):
        global t_max
        if n==1:
            return 1
        c_max = 1
        for i in range(1, n):
            pre_max = helper(arr, i)
            if arr[i - 1] < arr[n - 1] and pre_max + 1 > c_max:
                c_max = pre_max + 1
        t_max = max(c_max, t_max)
        # max_list[n] = c_max
        # print(n, c_max, max_list)
        return c_max

    helper(arr, len(arr))

    return t_max


# print(longest_subsequence([1, 3, 5, 6, 4, 8]))
print(longest_subsequence([ 3, 4,5,6,10, 17, 20, 21, 22, 4, 8, 9 ,11, 8, 6, 4, 2]))