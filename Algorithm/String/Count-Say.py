"""
1.     1
 2.     11
 3.     21
 4.     1211
 5.     111221
 6.     312211
 7.     13112221
 8.     1113213211
 9.     31131211131221
10.     13211311123113112211

Input: 4
Output: "1211"

"""


def countAndSay(n):
    if n == 1:
        return '1'
    if n == 2:
        return '11'
    prev_s = '11'
    for i in range(3, n+1):
        cnt = 1
        c_str = ''
        for s in range(0, len(prev_s)-1):
            if prev_s[s] == prev_s[s+1]:
                cnt += 1
            else:
                c_str += str(cnt) + prev_s[s]
                cnt = 1
        c_str += str(cnt) + prev_s[-1]
        print(i, prev_s, c_str)
        prev_s = c_str

    return c_str

# print(countAndSay(5))
print(countAndSay(7))