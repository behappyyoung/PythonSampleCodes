"""
# https://www.interviewbit.com/problems/rearrange-array/

Rearrange a given array so that Arr[i] becomes Arr[Arr[i]] with O(1) extra space.

Example:

Input : [1, 0]
Return : [0, 1]

Input: [ 1 2 3 1]
arr[1] = 2
arr[2] = 3
arr[3] = 1
arr[1] = 2
Expected output is [2 3 1 2]

# rearrange, rearrange_s => use 'n' extra space
# rearrange_s_s => use O(1)  space

"""
def rearrange_array(arr):
    new_arr = []
    for i in range(len(arr)):
        new_arr.append(arr[arr[i]])
    return new_arr

def rearrange_array_s(arr):
    arr_value = {}
    for i in range(len(arr)):
        arr_value[arr[i]] = arr[arr[i]]
    for i in range(len(arr)):
        arr[i] = arr_value[arr[i]]
    return arr


def rearrange_array_s_s(arr):
    size_n = len(arr)
    for i in range(size_n):

        arr[i] =  arr[i]  + ( arr[arr[i]] * size_n )

    for i in range(len(arr)):
        new_value = arr[i] / size_n
        if new_value > size_n:
            new_value = new_value % size_n
        arr[i] = new_value

    return arr

# test
test_arr = [1,2, 3,3,2]
print(test_arr)
print('=>')
print(rearrange_array_s(test_arr))
test_arr = [ 4, 0, 2, 1, 3 ]
print(test_arr)
print('=>')
print(rearrange_array_s(test_arr))
#
test_arr = [1,2, 3,3,2]
print(test_arr)
print('=>')
print(rearrange_array_s_s(test_arr))
test_arr = [ 4, 0, 2, 1, 3 ]
print(test_arr)
print('=>')
print(rearrange_array_s_s(test_arr))