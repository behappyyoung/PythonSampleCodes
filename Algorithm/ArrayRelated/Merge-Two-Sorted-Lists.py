"""
Given two sorted integer arrays A and B, merge B into A as one sorted array.
Input :
         A : [1 5 8]
         B : [6 9]

Modified A : [1 5 6 8 9]

"""
def merge_list(arr1, arr2):
    starting = 0
    new_arr = []
    for i in range(len(arr1)):
        if starting == len(arr2):
            new_arr.extend(arr1[i:])
            break
        for j in range(starting, len(arr2)):
            if arr1[i] >= arr2[j]:
                new_arr.append(arr2[j])
                starting = j+1
        new_arr.append(arr1[i])
    new_arr.extend(arr2[starting:])
    return new_arr

# test

print(merge_list([1,5, 8, 10, 12], [6, 9]))
print(merge_list([-4, -2, 3], [-1, 8]))
print(merge_list([-4, 3], [-2, -2]))