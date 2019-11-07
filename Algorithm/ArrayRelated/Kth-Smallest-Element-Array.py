"""
Find the kth smallest element in an unsorted array of non-negative integers.

You are not allowed to modify the array ( The array is read only ).
Try to do it using constant extra space.
A : [2 1 4 3 2]
k : 3

answer : 2
kth_element (n * k . worse n**2) ==> time limit exeeded


"""

def kth_element(arr, k):
    c_min = arr[0]
    for i in arr:
        if i < c_min:
            c_min = i

    next_min = c_min
    min_count = 0
    while min_count != k:
        for i in arr:
            if i == c_min:
                min_count += 1
                if min_count == k:
                    return c_min
            else:
                if i < c_min:
                    pass
                elif next_min == c_min:
                    next_min = i
                elif c_min < i < next_min:
                    next_min = i
        c_min = next_min

    return c_min


def kth_element_s(arr, k):
    c_min = arr[0]
    c_max = arr[0]
    for i in arr:
        if i < c_min:
            c_min = i
        if i > c_max:
            c_max = i
    c_mid = (c_max + c_min)//2
    count_smaller = 0
    count_equal = 0
    while c_min < c_mid:
        count_equal = 0
        count_smaller = 0
        for i in arr:
            if i < c_mid:
                count_smaller += 1
            elif i == c_mid:
                count_equal += 1
        if count_smaller >= k:
            c_max = c_mid
        else:
            if k <= count_smaller + count_equal:
                return c_mid
            c_min = c_mid
        # print(c_min, c_mid, c_max, count_smaller, count_equal)
        c_mid = (c_max + c_min) // 2

    # print(c_min, c_mid, c_max, count_smaller, count_equal)
    if count_smaller < k:
        return c_max
    else:
        return c_min
# test
# input_arr = [7, 10, 4, 3, 20, 15]
# k = 3
# print(kth_element(input_arr, k))
# print(kth_element_s(input_arr, k))

input_arr = [47, 7]
k = 2
print(kth_element_s(input_arr, k))
input_arr = [ 74, 90, 85, 58, 69, 77, 90, 85, 18, 36 ]
k = 1
# print(kth_element(input_arr, k))
print(kth_element_s(input_arr, k))
#
# input_arr = [ 8, 16, 80, 55, 32, 8, 38, 40, 65, 18, 15, 45, 50, 38, 54, 52, 23, 74, 81, 42, 28, 16, 66, 35, 91, 36, 44, 9, 85, 58, 59, 49, 75, 20, 87, 60, 17, 11, 39, 62, 20, 17, 46, 26, 81, 92 ]
# k = 9
# print(kth_element(input_arr, k))
# print(kth_element_s(input_arr, k))
# # for check
# input_arr.sort()
# print(input_arr, input_arr[k-1])

