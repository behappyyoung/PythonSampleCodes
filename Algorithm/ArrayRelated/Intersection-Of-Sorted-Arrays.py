"""
Find the intersection of two sorted arrays.
OR in other words,
Given 2 sorted arrays, find all the elements which occur in both the arrays.

Input :
    A : [1 2 3 3 4 5 6]
    B : [3 3 5]

Output : [3 3 5]

Input :
    A : [1 2 3 3 4 5 6]
    B : [3 5]

Output : [3 5]


"""
def intersection_or_two_arrays(arr1, arr2):
    new_arr = []
    len_arr1 = len(arr1)
    len_arr2 = len(arr2)
    done = False
    i = 0
    j = 0
    while not done:
        if arr1[i] == arr2[j]:
            new_arr.append(arr1[i])
            if i >= len_arr1-1 or j >= len_arr2-1:
                done = True
            else:
                i += 1
                j += 1
        elif arr1[i] < arr2[j]:
            if i >= len_arr1-1:
                done = True
            else:
                i += 1

        else:
            if j >= len_arr2-1:
                done = True
            else:
                j += 1
    return new_arr

# test

print(intersection_or_two_arrays([1,5, 8, 10, 12], [6, 9]))
print(intersection_or_two_arrays([1,2,3, 3, 4, 5, 6], [3, 5]))

