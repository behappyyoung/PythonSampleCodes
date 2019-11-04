"""
    merge sort
    1. mergesort ( 1/2 of array) => recursive
    2. merge ( 2 * 1/2 of array => 1 )
    O(nlogn)
"""

def merge(arr, start, middle, end):
    # create a temp array
    temp = [0] * (end - start + 1)
    i = start
    j = middle + 1
    k = 0
    # compare two arrays  // add smaller ones to the temp array
    while i <= middle and j <= end:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1

        k += 1
    # add elements left in the left array if there is any
    while i <= middle:
        temp[k] = arr[i]
        i += 1
        k += 1
    # add elements left in the right array if there is any
    while j <= end:
        temp[k] = arr[j]
        j += 1
        k += 1

    # copy temp to original array interval
    for i in range(start, end+1):
        arr[i] = temp[i-start]

def merge_sort(arr, start, end):
    if start < end:
        middle = int((start+end)/2)
        merge_sort(arr, start, middle)
        merge_sort(arr, middle+1, end)
        merge(arr, start, middle, end)

# test
test_arr = [5, 12, 13, 10, 7, 6, 2]
merge_sort(test_arr, 0, len(test_arr) - 1)
print('sorted :', test_arr)
test_arr2 = [20, 30, 50, 90, 100, 200, 300, 1, 8]
merge_sort(test_arr2, 0, len(test_arr2) - 1)
print('sorted :', test_arr2)