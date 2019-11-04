"""
Reverse bits of an 32 bit unsigned integer

3
        00000000000000000000000000000011
=>        11000000000000000000000000000000
3221225472

"""

def reverse_bits(input_int):
    bit_str = bin(input_int)
    int_str = ''
    bit_str = bit_str[2:].zfill(32)
    for s in bit_str:
        int_str = s + int_str
    return int(int_str, 2)


print(reverse_bits(288))
print(reverse_bits(2))
print(reverse_bits(3))

