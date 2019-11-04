"""
# https://www.interviewbit.com/problems/implement-power-function/

Implement pow(x, n) % d.

In other words, given x, n and d,

find (x^n % d)


"""
from datetime import datetime

def power_function(x, y):
    if y == 0:
        return 1
    temp = power_function(x, y / 2)
    if y % 2 == 0:
        return temp * temp
    else:
        return x * temp * temp


def power_mod(x, n, d):
    remainder = power_function(x, n)
    if remainder < 0:
        return d + remainder
    while remainder >= d:
        devided = remainder/d
        if devided == 1:
            remainder = 0
        else:
            remainder = remainder - (devided * d)

    return remainder


def power_mod_s(x, n, d):
    x = x - (d * (x / d))
    if n == 1:
        return x
    if n == 0:
        return 1 if x != 0 else 0
    extra = x if n - (2 * (n / 2)) == 1 else 1
    remainder = extra * power_mod_s(x * x, n / 2, d)
    return remainder - (d * (remainder / d))


print(power_mod(2, 3, 3))
print(power_mod(2, 3, 2))
print(power_mod(-1, 1, 20))
print(power_mod(-1, 2, 20))
print(power_mod(-1, 3, 20))


print(power_mod_s(2, 3, 3))
print(power_mod_s(2, 3, 2))
print(power_mod_s(-1, 1, 20))
print(power_mod_s(-1, 2, 20))
print(power_mod_s(-1, 3, 20))

start_time = datetime.now()
print(power_mod(710459, 415354, 647354))
end_time = datetime.now()
print(end_time - start_time)

start_time = datetime.now()
print(power_mod_s(710459, 415354, 647354))
end_time = datetime.now()
print(end_time - start_time)

start_time = datetime.now()
print(power_mod_s(71045970, 41535484, 64735492))
end_time = datetime.now()
print(end_time - start_time)



