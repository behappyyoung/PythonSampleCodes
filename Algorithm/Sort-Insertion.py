"""
    Insertion sort
    for small, kind of sorted array
    "stable" (maintain the relative order of records with equal keys )
    O(n^2)
"""

def insertion_sort(arr):
    # Traverse through 1 to len(input_array)
    for i in range(1, len(arr)):
        current_element = arr[i]
        j = i - 1
        # Move elements of input_array[0..i-1], that are
        # greater than current_element, to one position ahead of their current position
        while j >=0 and current_element < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        # when it's done, put current element in that position
        arr[j + 1] = current_element

input_array = [12, 11, 13, 5, 6, 9, 200, 2]
insertion_sort(input_array)
print('after sort :', input_array)