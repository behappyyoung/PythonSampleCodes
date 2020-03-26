"""
Given an array nums, write a function to move all 0 s to the end of it
while maintaining the relative order of the non-zero elements.

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

"""

def move_zeros(nums):
    i = 0
    p = -1
    while i < len(nums):
        if nums[i] == 0:
            if p == -1:
                p = i
        else:
            if p >= 0:
                nums[i], nums[p] = nums[p], nums[i]
                i = p
                p = -1
        print(i, nums, p)
        i += 1
# test
test_array = [2, 1, 3, 0, 0, 0, 1, 5, 4]
print(test_array, move_zeros(test_array))
