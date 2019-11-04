"""
Find if Given number is power of 2 or not.
More specifically, find if given number can be expressed as 2^k where k >= 1
2, 4, 8, 16, 32,,,
return 1 if the number is a power of 2 else return 0

Input : 128
Output : 1

power_of_two    ==> Time Limit Exceeded.
"""
def power_of_two(str):
    int_str = int(str)
    if int_str == 2:
        return 1
    i = 2
    while i < int_str:
        i *= 2
        print(i)
        if i == int_str:
            return 1
        elif i > int_str:
            return 0
    return 0

def power_of_two_s(input_int):
    if input_int == 1:
        return 0
    bin_str = bin(input_int)
    if bin_str[2] != '1':
        return 0
    for i in range(3, len(bin_str)):
        if bin_str[i] == '1':
            return 0
    return 1

print(power_of_two_s(256030000302310049348232710))
print(power_of_two_s(128))
print(power_of_two_s(124))
