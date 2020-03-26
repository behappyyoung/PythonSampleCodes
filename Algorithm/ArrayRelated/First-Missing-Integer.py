"""
Given an unsorted integer array, find the first missing positive integer.

Example:

Given [1,2,0] return 3,

[3,4,-1,1] return 2,

[-8, -7, -6] returns 1

Your algorithm should run in O(n) time and use constant space.

firstMissingPositive => Time Limit Exceeded.

"""
def firstMissingPositive(A):
    l = [i + 1 for i in range(len(A) + 1)]
    print(l)
    for i in range(len(A)):
        if A[i] in l:
            l.remove(A[i])

    return l[0]


def firstMissingPositive_s(A):
    l = [0 for i in range(len(A)+1)]
    print(l)
    for i in range(len(A)):
        if 0< A[i] <= len(A):
            l[A[i]-1] = 1
    print(l)
    for i in range(len(l)):
        if l[i] == 0:
            return i+1

print(firstMissingPositive_s([ 1, 2, 3, 4, 5, 6 ]))