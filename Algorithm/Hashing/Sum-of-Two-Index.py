"""
You have an array of n elements, and a sum.
Check if any 2 elements in the array sum to the given sum.
Expected time complexity O(n).

A[] = { 1 , 5 , 4 , 4 , 3 , 8};
X=8;

output.. indeces list


"""


def sum_exist_hash(arr, s):
    check_dict = {}
    for i in range(len(arr)):
        if check_dict.get(str(arr[i])) is not None:
            return [i+1, check_dict[str(arr[i])]+1]
        if check_dict.get(str(s - arr[i])) is None:
            check_dict[str(s - arr[i])] = i
        print(i, check_dict)
    return False


input_arr = [4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1, 9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8]
total = -3

# print(sum_exist_hash(input_arr, total))

input_arr = [ 8, 1, -9, -5, 8, -6, 1, -10, 1, 9, 7, 5, -7, 6, 3, 0, 6, -2, 6, 9, 4, 7, 1, -5, -3, 10, -3, -3, -4, 7, -6, 6, -9, 4, 5, 2, -2, 0, -8, 2, -10, 3, -5, 2, -3, -1, -8, 10, 5, -1, 2, 1, 9, -1, -2, 8, -7, -7, -9, -10, -1, -9, 5, -8, -4, -10, 1, 2, 7 ]
total = -2

print(sum_exist_hash(input_arr, total))