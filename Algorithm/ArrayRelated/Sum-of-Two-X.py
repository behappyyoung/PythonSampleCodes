"""
You have an array of n elements, and a sum.
Check if any 2 elements in the array sum to the given sum.
Expected time complexity O(n).

A[] = { 1 , 5 , 4 , 4 , 3 , 8};
X=8;

sum_exist => n**2   ( i in check_arr =>n )
sum_sort ==> nlogn ( sort nlogn )
sum_newsort => n ( space N is higher )
sum_exist_hash ==> best ???

"""

def sum_exist(arr, s):
    check_arr = []
    for i in arr:
        if i in check_arr:
            return True
        check_arr.append(i)
    return False


def sum_exist_hash(arr, s):
    check_dict = {}
    for i in arr:
        if check_dict.get(str(s-i)):
            return True
        check_dict[str(s-i)] = i
    return False

def sum_exist_sort(arr, s):
    arr.sort()
    left = 0
    right = len(arr) -1
    while left < right:
        c_sum = arr[left] + arr[right]
        if c_sum == s:
            return True
        elif c_sum > s:
            right -= 1
        else:
            left += 1
    return False


def sum_exist_new_sort(arr, s):
    l = len(arr)
    max_a = 0
    for i in arr:
        if i > max_a:
            max_a = i

    hash_arr = [0] * (max(max_a, l) + 1)
    print(hash_arr)
    for i in arr:
        hash_arr[i] += 1
    new_sorted_arr = []
    for i in range(len(hash_arr)):
        for j in range(hash_arr[i]):
            new_sorted_arr.append(i)

    left = 0
    right = len(new_sorted_arr) - 1
    while left < right:
        c_sum = arr[left] + arr[right]
        if c_sum == s:
            return True
        elif c_sum > s:
            right -= 1
        else:
            left += 1

    return False


input_arr = [1,5,4,4,3,8, 20, 30]
print(sum_exist(input_arr, 33))
print(sum_exist_hash(input_arr, 33))
print(sum_exist_sort(input_arr, 33))
print(sum_exist_new_sort(input_arr, 33))

input_arr = [ 4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1, 9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8 ]
total = -3

print(sum_exist_hash(input_arr, total))