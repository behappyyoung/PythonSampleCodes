"""
Write a function that takes an unsigned integer and returns the number of 1 bits it has.

00000000000000000000000000001011

3

"""

def number_of_1bits(input_int):
    bit_int = bin(input_int)
    number_of_bit = 0
    for i in bit_int:
        if i=='1':
            number_of_bit += 1
    return number_of_bit


def number_of_1bits_without_bin(input_int):
    number_of_bit = 0
    while input_int:
        number_of_bit += input_int & 1
        input_int >>= 1
    return number_of_bit


def hammingWeight(n):
    sum = 0
    while n != 0:
        sum += 1
        n &= (n - 1)
    return sum


print(number_of_1bits(288))
print(number_of_1bits_without_bin(288))
print(hammingWeight(288))
print(number_of_1bits(2))
print(number_of_1bits_without_bin(2))

print(number_of_1bits(999))
print(number_of_1bits_without_bin(999))
print(hammingWeight(999))

