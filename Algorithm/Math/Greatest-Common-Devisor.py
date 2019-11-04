"""
Given 2 non negative integers m and n, find gcd(m, n)

GCD of 2 integers m and n is defined as the greatest integer g such that g is a divisor of both m and n.
Both m and n fit in a 32 bit signed integer.

Example

m : 6
n : 9

GCD(m, n) : 3

"""
def greatest_common_devisor(m, n):
    if m == 0:
        return n
    elif n == 0:
        return m
    min_i = min(m, n)
    gcd = 1
    for i in range(1, min_i+1):
        if m % i == 0 and n % i == 0:
            gcd = i
    return gcd

def greatest_common_devisor_s(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

# test
print(greatest_common_devisor(6, 9))
print(greatest_common_devisor(61, 99))
print(greatest_common_devisor(9, 99))
print(greatest_common_devisor_s(6, 9))
print(greatest_common_devisor_s(61, 99))
print(greatest_common_devisor_s(9, 99))