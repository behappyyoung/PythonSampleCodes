"""
Remove duplicates from Sorted Array
Given a sorted array, remove the duplicates in place such that each element can appear atmost twice and return the new length.

Note that even though we want you to return the new length, make sure to change the original array as well in place

Do not allocate extra space for another array, you must do this in place with constant memory.

Given input array A = [1,1,1,2],

Your function should return length = 3, and A is now [1,1,2]

"""

def remove_duplicate_two(arr):
    len_arr = len(arr)
    i = len_arr - 1
    j = i - 1
    same_times = 0
    while i > 0:
        print(i, j, arr, same_times)
        if arr[i] == arr[j]:
            same_times += 1
            if same_times >= 2:
                arr.pop(i)
                i -= 1
                j = i-1
        else:
            same_times = 0
        j -= 1

        if j == -1:
            i -= 1
            j = i-1
    print(arr)
    return len(arr)


# test
input_arr = [1, 1, 1, 2, 2, 2, 3]

print(remove_duplicate_two(input_arr))

input_arr = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3 ]

# print(remove_duplicate_two(input_arr))