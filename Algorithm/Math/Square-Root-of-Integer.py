
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
def get_sqrt_s(n):
    if n<=1 :
        return n

    l = 2
    r = n-1
    ans = 1
    while l <=r:
        m = l + (r-l)//2
        times = m * m
        if times == n:
            return m
        elif times < n:
            l = m + 1
            ans = m
        else:
            r = m - 1

    return ans

test_int = 2
print(test_int, get_sqrt_s(test_int))
test_int = 4356
print(test_int, get_sqrt_s(test_int))
test_int = 930675566
print(test_int, get_sqrt_s(test_int))
