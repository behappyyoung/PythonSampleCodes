"""
1, 11, 21, 1211, 111221, ...
1 is read off as one 1 or 11.
11 is read off as two 1s or 21.

21 is read off as one 2, then one 1 or 1211.

Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

Example:

if n = 2,
the sequence is 11.

Your Input: 5
Expected output is 111221

Your Input: 7
Expected output is 13112221

"""

def count_and_say(n):
    how_many = 1
    new_string = ''
    s = '1'
    seq = 1
    while seq < n:
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                how_many += 1
            else:
                new_string = new_string + str(how_many) + s[i]
                how_many = 1
        if how_many == 1:
            new_string = new_string + "1" + s[-1]
        else:
            new_string = new_string + str(how_many) + s[-1]
        seq += 1
        s = new_string
        how_many = 1
        new_string = ''
    return s

print(count_and_say(5))
print(count_and_say(7))