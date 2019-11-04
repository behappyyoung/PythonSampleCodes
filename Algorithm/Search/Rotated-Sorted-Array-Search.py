"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7  might become 4 5 6 7 0 1 2 ).

You are given a target value to search. If found in the array, return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Input : [4 5 6 7 0 1 2] and target = 4
Output : 0



"""
from datetime import datetime


def rotated_sorted_array_search(arr, x, start, end):
    m = (start + end) / 2
    print(start, end, m, arr[start], arr[end], arr[m], x)
    if arr[m] == x:
        return m
    elif x == arr[start]:
        return start
    elif x == arr[end]:
        return end
    elif start == m:
        return -1
    elif x < arr[m]:
        if arr[start] < x:       #  arr[start] < x < arr[m]
            return rotated_sorted_array_search(arr, x, start, m)
        elif x < arr[start]:            #  x < arr[start] < arr[m]
            if arr[start] < arr[m]:#  ==> the other side
                return rotated_sorted_array_search(arr, x, m, end)
            else:
                return rotated_sorted_array_search(arr, x, start, m)
    else:

        if x < arr[end]:      # [m] < x < [end]
            return rotated_sorted_array_search(arr, x, m, end)
        else:                   # [m] < [end] < x
            if arr[m] < arr[end]:   # ==> the other side
                return rotated_sorted_array_search(arr, x, start, m)
            else:
                return rotated_sorted_array_search(arr, x, m, end)


def rotated_sorted_array_search_for_comparison(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

input_arr = []
for i in range(10000, 1000000):
    input_arr.append(i)
for i in range(10000):
    input_arr.append(i)
print('array created \n')

start_time = datetime.now()
print(rotated_sorted_array_search(input_arr, 400, 0, len(input_arr)-1))
end_time = datetime.now()
print(end_time - start_time)

start_time = datetime.now()
print(rotated_sorted_array_search_for_comparison(input_arr, 400))
end_time = datetime.now()
print(end_time - start_time)

# start_time = datetime.now()
# print(power_mod_s(71045970, 41535484, 64735492))
# end_time = datetime.now()
# print(end_time - start_time)



