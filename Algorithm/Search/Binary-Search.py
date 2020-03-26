"""
Given a sorted (in ascending order) integer array nums of n elements and a target value,
write a function to search target in nums. If target exists, then return its index,
otherwise return -1.

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4

"""


def binary_search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    l = 0
    r = len(nums) - 1

    while l <= r:
        print(l, r)
        m = l + (r - l) // 2
        if nums[m] == target:
            return m

        elif nums[m] < target:
            l = m + 1
        else:
            r = m - 1

    return -1

s = [-1,0,3,5,9,12]
t = 5

print(binary_search(s, t))