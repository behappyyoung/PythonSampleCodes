
"""
Given a number N, find all factors of N.

Example:

N = 6 
factors = {1, 2, 3, 6}

## get_factors / get_factors_s : too slow ( time limit exceeded )

"""

user_input=input("\n enter integer : ")

try:
    user_int = int(user_input)
except:
    print("\n need integer input ")
    exit(1)

def get_factors(n):
    if n==1 :
        return [1]
    factors = [1]
    for i in range(2, n):
        if n % i == 0:
            factors.append(i)
    factors.append(n)
    return factors

def get_factors_s(n):
    if n==1 :
        return [1]
    factors = [1, n]
    for i in range(2, int(n/2)):
        if i not in factors:
            if n % i == 0:
                if i != int(n/i):
                    factors.extend([i, int(n/i)])
                else:
                    factors.append(i)
    factors.sort()
    return factors


def get_factors_s_s(n):
    if n==1 :
        return [1]
    factors = [1, n]
    for i in range(2, int(n**0.5)+1):
        if i not in factors:
            if n % i == 0:
                if i != int(n/i):
                    factors.extend([i, int(n/i)])
                else:
                    factors.append(i)
    factors.sort()
    return factors


print(get_factors_s_s(user_int))
