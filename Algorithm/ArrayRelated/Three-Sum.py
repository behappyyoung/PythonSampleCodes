"""

# https://www.interviewbit.com/problems/3-sum/

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers.

given array S = {-1 2 1 -4},
and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)


three_sum ==> time limit exceeded

"""
def three_sum(arr, target):
    min_sum = arr[0] + arr[1] + arr[2]
    min_distance = min_sum - target
    len_arr = len(arr)

    for i in range(len_arr-2):
        for j in range(i+1, len_arr-1):
            for k in range(j+1, len_arr):
                c_sum = arr[i] + arr[j] + arr[k]
                if c_sum == target:
                    return target
                c_distance = abs(c_sum - target)

                if abs(c_distance) < abs(min_distance):
                    min_distance = c_distance
                    min_sum = c_sum

    return min_sum


def three_sum_s(arr, target):
    arr.sort()
    min_sum = arr[0] + arr[1] + arr[2]
    min_distance = min_sum - target
    len_arr = len(arr)
    for i in range(len_arr-2):
        l = i + 1
        r = len_arr - 1
        while l < r:
            c_sum = arr[i] + arr[l] + arr[r]
            if c_sum == target:
                return target
            c_distance = c_sum - target
            if abs(c_distance) < abs(min_distance):
                min_distance = c_distance
                min_sum = c_sum
            if c_sum < target:
                l += 1
            else:
                r -= 1

    return min_sum


# test

# print(three_sum([1,5, 8, 10, 12], 5))
# print(three_sum([-1, 2, 1, -4], 1))
input_arr = [ 9, -8, -10, -7, 7, -8, 2, -7, 4, 7, 0, -3, -4, -5, -1, -4, 5, 8, 1, 9, -2, 5, 10, -5, -7, -1, -6, 4, 1, -5, 3, 8, -4, -10, -9, -3, 10, 0, 7, 9, -8, 10, -9, 7, 8, 0, 6, -6, -7, 6, -4, 2, 0, 10, 1, -2, 5, -2 ]
input_target = 0
# print(three_sum(input_arr, input_target))
# print(three_sum_s(input_arr, input_target))
input_arr = [ -4, -8, -10, -9, -1, 1, -2, 0, -8, -2 ]
input_target = 0
print(three_sum(input_arr, input_target))
print(three_sum_s(input_arr, input_target))