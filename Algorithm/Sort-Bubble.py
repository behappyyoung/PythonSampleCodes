"""
    Bubble sort
    for small, kind of sorted array
    intuitive, easy to implement
    "stable" (maintain the relative order of records with equal keys )
    O(n^2)
"""

def bubble_sort(arr):
    # Traverse through 0 to len(input_array)-1
    for i in range(len(arr)-1):
        swapped = False
        # Traverse through 0 to len(input_array)-i-1
        for j in range(len(arr)-i-1):
            # if arr[j+1] > arr[j] swap
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        # if there was no swap, it's sorted
        if not swapped:
            return

# testing
input_array = [12, 11, 13, 5, 6, 9, 200, 2]
bubble_sort(input_array)
print('after sort :', input_array)
test_arr = [20, 30, 50, 90, 100, -200, 300, 1, 8]
bubble_sort(test_arr)
print('after sort :', test_arr)