"""
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

# https://en.wikipedia.org/wiki/Roman_numerals#Roman_numeric_system

I, II, III, IIII, V, VI, VII, VIII, VIIII, X.
I, II, III, IV, V, VI, VII, VIII, IX, X.
X, XX, XXX, XL, L, LX, LXX, LXXX, XC, C.
C, CC, CCC, CD, D, DC, DCC, DCCC, CM, M.

39 = 30 + 9 = XXX + IX = XXXIX.
246 = 200 + 40 + 6 = CC + XL + VI = CCXLVI.
789 = 700 + 80 + 9 = DCC + LXXX + IX = DCCLXXXIX.
2,421 = 2000 + 400 + 20 + 1 = MM + CD + XX + I = MMCDXXI.
160 = 100 + 60 = C + LX = CLX
207 = 200 + 7 = CC + VII = CCVII
1,009 = 1,000 + 9 = M + IX = MIX
1,066 = 1,000 + 60 + 6 = M + LX + VI = MLXVI
1954 = 1,000 + 900 + 50 + 4 = M + CM + L + IV = MCMLIV
2014 = 2,000 + 10 + 4 = MM + X + IV = MMXIV

"""

def roman_to_integer(str):
    roman_number = 0
    temp_number = 0
    length = len(str)
    for i in range(length):
        if str[i] == 'M':
            if temp_number == 100:
                roman_number += 900
            else:
                roman_number += 1000
        elif str[i] == 'D':
            if temp_number == 100:
                roman_number += 400
            else:
                roman_number += 500
        elif str[i] == 'C':
            if i<length-1:
                if str[i+1] == 'D' or str[i+1] == 'M':
                    temp_number = 100
                else:
                    if temp_number == 10:
                        roman_number += 90
                    else:
                        roman_number += 100
            else:
                if temp_number == 10:
                    roman_number += 90
                else:
                    roman_number += 100
        elif str[i] == 'L':
            if temp_number == 10:
                roman_number += 40
            else:
                roman_number += 50
        elif str[i] == 'X':

            if i < length-1:
                if str[i+1] == 'C' or str[i+1] == 'L':
                    temp_number = 10
                else:
                    if temp_number == 1:
                        roman_number += 9
                    else:
                        roman_number += 10
            else:
                if temp_number == 1:
                    roman_number += 9
                else:
                    roman_number += 10
        elif str[i] == 'V':
            if temp_number == 1:
                roman_number += 4
            else:
                roman_number += 5
        elif str[i] == 'I':
            if i < length - 1:
                if str[i + 1] == 'V' or str[i + 1] == 'X':
                    temp_number = 1
                else:
                    roman_number += 1
            else:
                roman_number += 1
    return roman_number


def roman_to_integer_s(str):
        roman_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(str)):
            if i > 0 and roman_val[str[i]] > roman_val[str[i - 1]]:
                int_val += roman_val[str[i]] - 2 * roman_val[str[i - 1]]
            else:
                int_val += roman_val[str[i]]
        return int_val


print('# 2421', roman_to_integer('MMCDXXI'), roman_to_integer_s('MMCDXXI'))
print('# 1093', roman_to_integer('MXCIII'), roman_to_integer_s('MXCIII'))
print('# 3287', roman_to_integer('MMMCCLXXXVII'), roman_to_integer_s('MMMCCLXXXVII'))

print('', roman_to_integer('IV'), roman_to_integer_s('IV'))