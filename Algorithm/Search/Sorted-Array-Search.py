"""
    Sorted Array Binary Search

"""
from datetime import datetime

def sorted_array_search(arr, x, start, end):
    m = start + (end-start) // 2

    if arr[m] == x:
        return m
    elif arr[m] > x:
        if start == m:
            return -1
        else:
            return sorted_array_search(arr, x, start, m)
    else:
        if end == m+1:
            if arr[end] ==x:
                return end
            else:
                return -1
        else:
            return sorted_array_search(arr, x, m, end)


def sorted_array_search_s(arr, x):
    l = 0
    r = len(arr)-1
    while l < r:
        m = l + (r-l)//2
        if arr[m] == x:
            return m
        elif arr[m] < x:
            l = m + 1
        else:
            r = m


def sorted_array_search_for_compare(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# input_arr = [0,1,2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 100, 102, 103, 104, 200, 300, 311, 312, 313, 314, 400, 1000]

input_arr = []
for i in range(1000000):
    input_arr.append(i)
print('array created')

# start_time = datetime.now()
# print(sorted_array_search(input_arr, 90000000, 0, len(input_arr)-1))
# end_time = datetime.now()
# print(end_time - start_time)

input_arr = [1, 2, 3]
start_time = datetime.now()
print(sorted_array_search_s(input_arr, 1))
end_time = datetime.now()
print(end_time - start_time)

# start_time = datetime.now()
# print(sorted_array_search_for_compare(input_arr, 90000000))
# end_time = datetime.now()
# print(end_time - start_time)



