"""
Given a non-empty array of integers,
every element appears twice except for one. Find that single one.
Input: [4,1,2,1,2]
Output: 4

Your algorithm should have a linear runtime complexity.
    with dict will be easy
Could you implement it without using extra memory?

"""

def find_single(arr):
    l = len(arr)
    if l == 1:
        return arr[0]
    s = arr[0]
    for i in range(1, l):
        s = s ^ arr[i]
    return s

print(find_single([2,2,1]))