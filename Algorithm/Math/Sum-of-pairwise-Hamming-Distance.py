"""
Hamming distance between two non-negative integers is defined as the number of positions at which the corresponding bits are different.

For example,

HammingDistance(2, 7) = 2, as only the first and the third bit differs in the binary representation of 2 (010) and 7 (111).

Given an array of N non-negative integers, find the sum of hamming distances of all pairs of integers in the array.
Return the answer modulo 1000000007.

Example

Let f(x, y) be the hamming distance defined above.

A=[2, 4, 6]

We return,
f(2, 2) + f(2, 4) + f(2, 6) +
f(4, 2) + f(4, 4) + f(4, 6) +
f(6, 2) + f(6, 4) + f(6, 6) =

0 + 2 + 1
2 + 0 + 1
1 + 1 + 0 = 8

# hamming_distance, sum_hamming_distance : takes too long
# sum_hamming_distance_s : too much memory
"""
def get_binary(i):
    bin = ''
    while i != 0:
        bin = str(i%2) + bin
        i /=2
    return bin

def hamming_distance(x, y):
    bin_x =  get_binary(x)  # = format(x, 'b')
    bin_y =  get_binary(y)  # = format(y, 'b')
    size_x = len(bin_x)
    size_y = len(bin_y)
    if size_y > size_x :
        for i in range(size_x, size_y):
            bin_x = '0' + bin_x
            size_x += 1
    else:
        for i in range(size_y, size_x):
            bin_y = '0' + bin_y
            size_y += 1
    hammingdistance = 0
    for i in range(size_x):
        if bin_x[i] != bin_y[i]:
            hammingdistance += 1

    return hammingdistance


def hamming_distance_s(n1, n2):
    x = n1 ^ n2
    setBits = 0

    while (x > 0):
        setBits += x & 1
        x >>= 1

    return setBits

def sum_hamming_distance(arr):
    total_distance = 0
    for i in range(len(arr)-1):
        for j in range(i, len(arr)):
                total_distance += hamming_distance_s(arr[i], arr[j])
    return total_distance * 2


def sum_hamming_distance_s(arr):
    total_distance = 0
    hd_dict = {}
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            c_att = str(arr[i]) + ':' + str(arr[j])
            if hasattr(hd_dict, c_att):
                c_hd = hd_dict.get(c_att)
            else:
                c_hd = hamming_distance_s(arr[i], arr[j])
                hd_dict[c_att] = c_hd
            total_distance += c_hd
    return total_distance * 2

# test

# print(hamming_distance(2, 7))
# print(hamming_distance(2, 6))
# print(hamming_distance(2, 8))

# print(hamming_distance(6, 900000000000))
# print(sum_hamming_distance([2, 4, 6, 9, 7, 300, 200000000]))
print(sum_hamming_distance_s([2, 4, 6, 11, 2]))
print(sum_hamming_distance_s([2, 4, 6, 9, 7, 300, 200000000]))
