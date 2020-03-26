"""
https://www.interviewbit.com/problems/add-one-to-number/

If the vector has [1, 2, 3]

the returned vector should be [1, 2, 4]

as 123 + 1 = 124.


add_one_to_number : too slow for large array
add_one_to_number_s

"""
def add_one_to_number(arr):
    sum = 0
    size_a = len(arr)-1

    for i in range(len(arr)):
        sum += (10 ** size_a) * arr[i]
        size_a -= 1
    sum += 1
    str_sum = str(sum)
    return_arr = [int(str_sum[0])]
    for i in range(1, len(str_sum)):
        return_arr.append(int(str_sum[i]))
    return return_arr


def add_one_to_number_s(digits):
    i = len(digits) - 1
    overflow = 1
    while i >= 0 and overflow == 1:
        c_sum = digits[i] + overflow
        if c_sum == 10:
            digits[i] = 0
            overflow = 1
            i -= 1
        else:
            digits[i] = c_sum
            overflow = 0

    if overflow == 1:
        digits.insert(0, 1)

    return digits


# test
test_array = [2, 1, 3, 4, 1, 2, 1, 5, 4]
print(test_array, add_one_to_number_s(test_array))
test_array = [2]
print(test_array, add_one_to_number_s(test_array))
test_array = [9, 9, 9]
print(test_array)
print(add_one_to_number_s(test_array))
test_array = [0, 0, 0, 2, 2, 9]
print(test_array)
print(add_one_to_number_s(test_array))
test_array = [0]
print(test_array, add_one_to_number_s(test_array))