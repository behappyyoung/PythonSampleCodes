"""
Given two arrays, write a function to compute their intersection.

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]



"""
def intersection_or_two_arrays(arr1, arr2):
    new_arr = []
    arr1.sort()
    arr2.sort()
    len_arr1 = len(arr1)
    len_arr2 = len(arr2)
    i = 0
    j = 0
    print(arr1, arr2)
    while i < len_arr1:
        while i<len_arr1 and j<len_arr2:
            # print(i, j, arr1[i], arr2[j])
            if arr1[i] == arr2[j]:
                if j not in new_arr:
                    new_arr.append(j)
                i += 1
            j += 1
        i += 1
        j = 0
    new_arr = [arr2[j] for j in new_arr]
    return new_arr

# test
# print(intersection_or_two_arrays( [1], [1,1]))
print(intersection_or_two_arrays( [1, 2, 2, 1], [2,2]))
# print(intersection_or_two_arrays( [4,9,5], [9,4,9,8,4]))
# print(intersection_or_two_arrays([1,2,3, 3, 4, 5, 6], [3, 5]))
# print(intersection_or_two_arrays([-2147483648,1,2,3], [1,-2147483648,-2147483648]))

a1 = [43,85,49,2,83,2,39,99,15,70,39,27,71,3,88,5,19,5,68,34,7,41,84,2,13,85,12,54,7,9,13,19,92]
a2 = [10,8,53,63,58,83,26,10,58,3,61,56,55,38,81,29,69,55,86,23,91,44,9,98,41,48,41,16,42,72,6,4,2,81,42,84,4,13]
print(intersection_or_two_arrays(a1, a2))