"""

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.



"""

def three_sum_zero(arr):
    arr.sort()
    len_arr = len(arr)
    return_arr = []
    print(arr)
    for i in range(len_arr-2):
        l = i + 1
        r = len_arr - 1
        while l < r:
            c_sum = arr[i] + arr[l] + arr[r]
            if c_sum == 0:
                if [arr[i], arr[l], arr[r]] not in return_arr:
                    return_arr.append([arr[i], arr[l], arr[r]])
                l += 1
            elif c_sum < 0:
                l += 1
            else:
                r -= 1

    return return_arr


# test
input_arr = [-1, 0, 1, 2, -1, -4]
input_arr = [ 1, -4, 0, 0, 5, -5, 1, 0, -2, 4, -4, 1, -1, -4, 3, 4, -1, -1, -3 ]
# input_arr = [ 9, -8, -10, -7, 7, -8, 2, -7, 4, 7, 0, -3, -4, -5, -1, -4, 5, 8, 1, 9, -2, 5, 10, -5, -7, -1, -6, 4, 1, -5, 3, 8, -4, -10, -9, -3, 10, 0, 7, 9, -8, 10, -9, 7, 8, 0, 6, -6, -7, 6, -4, 2, 0, 10, 1, -2, 5, -2 ]
print(three_sum_zero(input_arr))
# input_arr = [ -4, -8, -10, -9, -1, 1, -2, 0, -8, -2 ]
