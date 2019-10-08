"""
    quick sort
    quick_sort ( 1/2 of array by pivot ) => recursive
    O(nlogn)
"""


def partition(arr, start, end):
    i = (start - 1)
    pivot = arr[end]  # pivot
    for j in range(start, end):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            # move smaller element to next smaller element position
            # put element on that position into current position
            arr[i], arr[j] = arr[j], arr[i]

    # move pivot element to next smaller element position
    # put element on that position into pivot position
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1


def quick_sort(arr, start, end):
    if start < end:
        # pi is partitioning index
        pi = partition(arr, start, end)

        # sort before partition and after partition
        quick_sort(arr, start, pi - 1)
        quick_sort(arr, pi + 1, end)


# test
test_arr = [5, 12, 13, 10, 7, 6, 9]
quick_sort(test_arr, 0, len(test_arr) - 1)
print('sorted :', test_arr)
test_arr2 = [20, 30, 50, 90, 100, 200, 300, 1, 8]
quick_sort(test_arr2, 0, len(test_arr2) - 1)
print('sorted :', test_arr2)