"""
We define f(X, Y) as number of different corresponding bits in binary representation of X and Y.
For example, f(2, 7) = 2, since binary representation of 2 and 7 are 010 and 111, respectively.
The first and the third bit differ, so f(2, 7) = 2.



A=[1, 3, 5]

We return

f(1, 1) + f(1, 3) + f(1, 5) +
f(3, 1) + f(3, 3) + f(3, 5) +
f(5, 1) + f(5, 3) + f(5, 5) =

0 + 1 + 1 +
1 + 0 + 2 +
1 + 2 + 0 = 8

different_bits_sum => time exceeded


"""
def get_different_bits_sum(int1, int2):
    int1_bin = bin(int1)[2:]
    int2_bin = bin(int2)[2:]
    sum = 0
    max_length = max(len(int1_bin), len(int2_bin))
    int1_bin = int1_bin.zfill(max_length)
    int2_bin = int2_bin.zfill(max_length)
    for i in range(max_length):
        if int1_bin[i] != int2_bin[i]:
            sum += 1
    return sum

def different_bits_sum(arr):
    total_sum = 0
    for i in range(len(arr)-1):
        for j in range(i, len(arr)):
            total_sum += get_different_bits_sum(arr[i], arr[j])
    return total_sum*2


def different_bits_sum_s(arr):
    total_sum = 0
    total_num_arr = len(arr)
    str_arr = []
    for c_int in arr:
        str_arr.append(bin(c_int)[2:].zfill(32))

    for i in range(32):
        total_one = 0
        for j in range(total_num_arr):
            if str_arr[j][i] == '1':
                total_one += 1
        total_sum += total_one * (total_num_arr - total_one) *2

    return total_sum


def different_bits_sum_s_s(arr):
    total_sum = 0
    total_num_arr = len(arr)

    for i in range(32):
        total_one = 0
        for j in range(total_num_arr):

            if arr[j] & (1<<i) != 0:
                total_one += 1
        total_sum += total_one * (total_num_arr - total_one) *2

    return total_sum

print(different_bits_sum([2, 7]))
print(different_bits_sum([1, 3, 5]))
print(different_bits_sum([1, 3, 4, 5, 20]))


print(different_bits_sum_s([2, 7]))
print(different_bits_sum_s([1, 3, 5]))
print(different_bits_sum_s([1, 3, 4, 5, 20]))


print(different_bits_sum_s_s([2, 7]))
print(different_bits_sum_s_s([1, 3, 5]))
print(different_bits_sum_s_s([1, 3, 4, 5, 20]))