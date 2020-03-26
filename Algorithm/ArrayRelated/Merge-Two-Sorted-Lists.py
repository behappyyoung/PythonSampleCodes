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

def merge_list_s(arr1, arr2):
    k = 0
    i = 0
    j = 0
    l1 = len(arr1)
    l2 = len(arr2)
    new_arr = [None]*(l1+l2)
    while i < l1 and j < l2:
        if arr1[i] <= arr2[j]:
            new_arr[k] = arr1[i]
            k += 1
            i += 1
        else:
            new_arr[k] = arr2[j]
            k += 1
            j += 1

    while i < l1:
            new_arr[k] = arr1[i]
            k += 1
            i += 1
    while j < l2:
            new_arr[k] = arr2[j]
            k += 1
            j += 1
    return new_arr

def merge_list_with_limit(nums1, nums2, m, n):
    k = 0
    i = 0
    j = 0
    new_arr = [None] * (m + n)
    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            new_arr[k] = nums1[i]
            k += 1
            i += 1
        else:
            new_arr[k] = nums2[j]
            k += 1
            j += 1

    while i < m:
        new_arr[k] = nums1[i]
        k += 1
        i += 1
    while j < n:
        new_arr[k] = nums2[j]
        k += 1
        j += 1
    return new_arr


def merge_list_with_limit_using_nums1(nums1, nums2, m, n):
    k = 0
    i = 0
    j = 0
    if not nums2:
        nums1 = nums1[:m]
    new_arr = nums1[:m]
    while i < m and j < n:
        if new_arr[i] <= nums2[j]:
            nums1[k] = new_arr[i]
            k += 1
            i += 1
        else:
            nums1[k] = nums2[j]
            k += 1
            j += 1

    while i < m:
        nums1[k] = new_arr[i]
        k += 1
        i += 1
    while j < n:
        nums1[k] = nums2[j]
        k += 1
        j += 1
    return nums1

# test
#
# print(merge_list([1,5, 8, 10, 12], [6, 9]))
# print(merge_list([-4, -2, 3], [-1, 8]))
# print(merge_list([-4, 3], [-2, -2]))
# print(merge_list_s([1,5, 8, 10, 12], [6, 9]))
# print(merge_list_s([-4, -2, 3], [-1, 8]))
# print(merge_list_s([-4, 3], [-2, -2]))
print(merge_list_with_limit([1,2,3,0,0,0], [2,5,6], 3, 3))
print(merge_list_with_limit_using_nums1([1,2,3,0,0,0], [2,5,6], 3, 3))
print(merge_list_with_limit_using_nums1([1,2,3,4, 5], [], 5, 0))