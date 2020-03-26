"""
Given an array of integers, A of length N, find the length of longest subsequence which is first increasing then decreasing.

Input Format:

The first and the only argument contains an integer array, A.
Output Format:

Return an integer representing the answer as described in the problem statement.
Constraints:

1 <= N <= 3000
1 <= A[i] <= 1e7
Example:

Input 1:
    A = [1, 2, 1]

Output 1:
    3

Explanation 1:
    [1, 2, 1] is the longest subsequence.

Input 2:
    [1, 11, 2, 10, 4, 5, 2, 1]

Output 2:
    6

Explanation 2:
    [1 2 10 4 2 1] is the longest subsequence.

A : [1 3 5 6 4 8 4 3 2 1]  => 9

"""

def longest_subsequence(arr):
    if not arr:
        return 0
    up_list = {}
    down_list = {}
    def get_max(arr, n):
        if n==1:
            return 1
        c_max = 1
        for i in range(1, n):
            pre_max = get_max(arr, i)
            if arr[i - 1] < arr[n - 1] and pre_max + 1 > c_max:
                c_max = pre_max + 1
        up_list[n-1] = c_max
        return c_max

    l = len(arr)
    def get_min(arr, n):
        if n==l:
            return 1
        c_min = 1
        for i in range(l-1, n, -1):
            pre_min = get_min(arr, i)
            if arr[i] < arr[n] and pre_min + 1 > c_min:
                c_min = pre_min + 1
        down_list[n] = c_min
        return c_min

    get_max(arr, len(arr))
    get_min(arr, 0)
    t_max = 1
    print(up_list, down_list)
    for i in range(2, len(arr)):
        t_max = max(t_max, up_list[i]+ down_list[i]-1)
    return t_max

print(longest_subsequence([1, 11, 2, 10, 4, 5, 2, 1]))
print(longest_subsequence([1, 3, 5, 6, 4, 8, 4, 3, 2, 1]))
# print(longest_subsequence([1, 11, 2, 10, 4, 5, 2, 1]))