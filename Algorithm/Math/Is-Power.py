"""

Given a positive integer which fits in a 32 bit signed integer,
find if it can be expressed as A^P where P > 1 and A > 0. A and P both should be integers.

2*2*2*2 = 2**4 = 16

isPower => memory exceeded

"""
def isPower(n):
    for i in range(2, n//2+1):
        j = i
        s = j
        if n % i == 0:
            while s < n:
                s *= j
                if s == n:
                    return True
                print(i, j, s)
    return False


def isPower_s(n):
    import math
    for i in range(2, int(math.sqrt(n))+1):
        j = i
        s = j
        if n % i == 0:
            while s < n:
                s *= j
                if s == n:
                    return True
                print(i, j, s)
    return False

print(isPower(125))

print(isPower(4))
print(isPower(1024000000))
print(isPower_s(1024000000))