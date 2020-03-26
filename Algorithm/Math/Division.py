"""
 divide without division

"""


def division(dividend, divisor):
    positive = (dividend < 0) is (divisor < 0)

    dd = abs(dividend)
    dr = abs(divisor)
    count = 0
    while dr <= dd:

        multi = 1
        temp = dr
        while (temp << 1) <= dd:
            temp <<= 1
            multi <<= 1
        dd -= temp
        count += multi
        print(count, multi, temp)
    if positive:
        return min(count, 2**31-1)
    else:
        return max(-count, -2**31)


print(division(70, -3))
