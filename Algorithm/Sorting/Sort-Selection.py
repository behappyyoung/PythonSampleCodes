"""
    Selection sort
    for small, kind of sorted array
    "stable" (maintain the relative order of records with equal keys )
    O(n^2)
"""

def selection_sort(arr):
    # Traverse through 0 to len(input_array)
    for i in range(len(arr)):
        min_index = i
        # find index of min of array
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # swap min with current position ( right most of sorted array )
        arr[i], arr[min_index] = arr[min_index], arr[i]

# testing
input_array = [12, 11, 13, 5, 6, 9, 200, 2]
selection_sort(input_array)
print('after sort :', input_array)
test_arr = [20, 30, 50, 90, 100, -200, 300, 1, 8]
selection_sort(test_arr)
print('after sort :', test_arr)