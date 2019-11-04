"""
Given a positive integer which fits in a 32 bit signed integer, find if it can be expressed as A^P where P > 1 and A > 0. A and P both should be integers.

Example

Input : 4
Output : True
as 2^2 = 4.

# power_of_two_integers : takes too long

"""

user_input=input("\n is this number power of any integer? : ")

try:
    user_int = int(user_input)
except:
    print("\n need integer input ")
    exit(1)

def power_of_two_integers(userInt):
    if userInt == 1:
        return True
    for i in range(userInt):
        if i*i == userInt:
            return True
    return False


def power_of_two_integers_s(userInt, start, end):
    if userInt == 1:
        return True
    m = (start + end)/2
    squre = m * m
    if m == start or m == end:
        print(start, end, m, squre, userInt)
        return squre == userInt
    elif squre == userInt:
        return True
    elif squre > userInt:
        new_end = m
        return power_of_two_integers_s(userInt, start, m)
    else:
        new_start = m
        return power_of_two_integers_s(userInt, m, end)

# test
print(power_of_two_integers_s(user_int, 1, user_int))
