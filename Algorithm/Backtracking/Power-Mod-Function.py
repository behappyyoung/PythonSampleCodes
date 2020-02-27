"""
# https://www.interviewbit.com/problems/implement-power-function/

Implement pow(x, n) % d.

In other words, given x, n and d,

find (x^n % d)

 #####  (x**n) % d ==  (x**(n//2) * x**(n//2)) % d

"""


def power_mod(x, n, d):
    if n == 0:
        return 1 if x != 0 else 0

    half_mod = power_mod(x, n // 2, d)
    if n % 2 == 0:  # even number
        return (half_mod * half_mod) % d
    else:
        return (half_mod * half_mod * (x % d)) % d




print(power_mod(2, 3, 2))
print(power_mod(-1, 2, 20))
print(power_mod(-1, 3, 20))

# start_time = datetime.now()
print(power_mod(710459, 415354, 647354))
# end_time = datetime.now()
# print(end_time - start_time)
#
# start_time = datetime.now()
# print(power_mod_s(710459, 415354, 647354))
# end_time = datetime.now()
# print(end_time - start_time)
#
# start_time = datetime.now()
print(power_mod(71045970, 41535484, 64735492))
# end_time = datetime.now()
# print(end_time - start_time)



