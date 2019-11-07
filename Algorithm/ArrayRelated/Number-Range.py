"""
Given an array of non negative integers A, and a range (B, C),
find the number of continuous subsequences in the array which have sum S in the range [B, C] or B <= S <= C

Continuous subsequence is defined as all the numbers A[i], A[i + 1], .... A[j]
where 0 <= i <= j < size(A)

A : [10, 5, 1, 0, 2]
(B, C) : (6, 8)

==> 3

as [5, 1], [5, 1, 0], [5, 1, 0, 2] are the only 3 continuous subsequence with their sum in the range [6, 8]

number_range ==> time limit exceed ( n**2)

"""

def number_range(arr, r_min, r_max):
    sum_count = 0
    arr_len = len(arr)
    for i in range(arr_len):
        c_sum = arr[i]
        if c_sum <= r_max:
            if r_min <= c_sum :
                sum_count += 1
            for j in range(i+1, arr_len):
                c_sum += arr[j]
                # print(i, j, c_sum)
                if r_min <= c_sum <= r_max:
                    sum_count += 1
                elif c_sum > r_max:
                    break
    return sum_count



def find_subarray_less(arr, max_num):
    start = 0
    end = 0
    count = 0
    c_sum = arr[0]
    while start < len(arr)-1:
        # print(start, end, c_sum, count)
        if c_sum <= max_num:
            count += 1
            if end < len(arr)-1:
                end += 1
                c_sum += arr[end]
            else:
                start += 1
                end = start
                c_sum = arr[start]
        else:
            start += 1
            end = start
            c_sum = arr[start]
    # print(start, c_sum, count)
    if arr[-1]<max_num:
        count += 1
    return count

def number_range_s(arr, l_min, r_max):
    max_count = find_subarray_less(arr, r_max)
    min_count = find_subarray_less(arr, l_min-1)
    # print(min_count, max_count)
    return max_count-min_count

# test
input_arr = [10, 5, 1, 0, 2]
input_min = 6
input_max = 8
print(number_range(input_arr, input_min, input_max))
print(number_range_s(input_arr, input_min, input_max))
input_arr = [ 80, 97, 78, 45, 23, 38, 38, 93, 83, 16, 91, 69, 18, 82, 60, 50, 61, 70, 15, 6, 52, 90 ]
input_min = 99
input_max = 269
print(number_range(input_arr, input_min, input_max))
print(number_range_s(input_arr, input_min, input_max))
input_arr = [ 76, 22, 81, 77, 95, 23, 27, 35, 24, 38, 15, 90, 19, 46, 53, 6, 77, 96, 100, 85, 43, 16, 73, 18, 7, 66 ]
input_min = 98
input_max = 290
print(number_range(input_arr, input_min, input_max))
print(number_range_s(input_arr, input_min, input_max))
input_arr = [ 80, 34, 71, 40, 62, 30, 93, 11, 22, 59, 80, 61, 91, 94, 77, 27, 78, 72, 45, 53, 37 ]
input_min = 34
input_max = 612
print(number_range(input_arr, input_min, input_max))
print(number_range_s(input_arr, input_min, input_max))
input_arr = [1]
input_min = 0
input_max = 0
print(number_range(input_arr, input_min, input_max))
print(number_range_s(input_arr, input_min, input_max))