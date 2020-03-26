"""
Consider a sequence of numbers a0, a1, ..., an, in which an element is equal to the sum of squared digits of the previous element. The sequence ends once an element that has already been in the sequence appears again.

Given the first element a0, find the length of the sequence.
a0 = 16
a1 = 12 + 62 = 37
a2 = 32 + 72 = 58
a3 = 52 + 82 = 89
a4 = 82 + 92 = 145
a5 = 12 + 42 + 52 = 42
a6 = 42 + 22 = 20
a7 = 22 + 02 = 4
a8 = 42 = 16, which has already occurred before (a0)
Thus, there are 9 elements in the sequence.

"""


def squareDigitsSequence(a0):
    c_dict = {}

    def getSequence(n):
        s_sum = 0
        l = list(map(int, str(n)))
        for i in l:
            s_sum += i * i
        # print('sum', n, l, s_sum)
        return s_sum

    cn = a0
    while cn not in c_dict:
        c_s = getSequence(cn)
        c_dict[cn] = c_s
        cn = c_s
    return len(c_dict)+1


print(squareDigitsSequence(103))