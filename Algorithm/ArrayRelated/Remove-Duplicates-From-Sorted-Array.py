"""
Remove duplicates from Sorted Array
Given a sorted array, remove the duplicates in place such that each element appears only once and return the new length.

Note that even though we want you to return the new length, make sure to change the original array as well in place

Do not allocate extra space for another array, you must do this in place with constant memory.

Given input array A = [1,1,2],
Your function should return length = 2, and A is now [1,2]


"""

def remove_duplicate(arr):
    len_arr = len(arr)
    i = len_arr - 1
    j = i - 1
    while i > 0:
        print(i, j, arr)
        if arr[i] == arr[j]:
            arr.pop(i)
            i -= 1
            j = i-1
        else:
            j -= 1

        if j == -1:
            i -= 1
            j = i-1
    print(arr)
    return len(arr)


# test
input_arr = [1, 1, 2, 2, 3]

print(remove_duplicate(input_arr))
