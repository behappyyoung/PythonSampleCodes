
"""
Implement int sqrt(int x).

Compute and return the square root of x.

If x is not a perfect square, return floor(sqrt(x))

Example :

Input : 11
Output : 3

## get_sqrt : too slow

"""

def get_sqrt(n):
    if n<=1 :
        return n
    elif n==2:
        return 1
    for i in range(2, n):
        square = i * i
        if square == n:
            return i
        elif square > n:
            return i-1

# using binary search
def get_sqrt_s(n, start=None, end=None):
    if n<=1 :
        return n
    elif n==2:
        return 1
    if start and end:
        m = (start + end)/2
    else:
        start = 1
        m = int(n/2)
        end = n
    square = m * m
    if square == n:
        return m
    elif square > n:
        new_middle = (start + m) / 2
        if new_middle <= start:
            return start
        return get_sqrt_s(n, start, m)
    else:
        new_middle = (m + end) / 2
        if new_middle <= m:
            return m
        return get_sqrt_s(n, m, end)


test_int = 3
print(test_int, get_sqrt_s(test_int))
test_int = 10
print(test_int, get_sqrt_s(test_int))
test_int = 930675566
print(test_int, get_sqrt_s(test_int))
