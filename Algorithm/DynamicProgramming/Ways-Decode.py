"""
'A' -> 1
'B' -> 2
...
'Z' -> 26
Input 1:
    A = "8"

Output 1:
    1

Explanation 1:
    Given encoded message "8", it could be decoded as only "H" (8).

    The number of ways decoding "8" is 1.

Input 2:
    A = "12"

Output 2:
    2

Explanation 2:
    Given encoded message "12", it could be decoded as "AB" (1, 2) or "L" (12).

    The number of ways decoding "12" is 2.
"""

def numDecodings(s):
    l = len(s)
    if s[0] == '0':
        return 0
    dp = [0] * (l + 1)
    dp[0] = dp[1] = 1
    for i in range(1, l):
        v1 = int(s[i:i + 1])
        v2 = int(s[i - 1:i + 1])
        if 0 < v1 <= 9:
            # If we get a valid single number decoding, the number of decodings will
            # same as previous. Because a single valid decoding won't add to your count.
            dp[i + 1] = dp[i]

        if 10 <= v2 <= 26:
            # Check if a double number decoding is valid.
            # If it is valid, we need to add everything before this two digit number to the current number.
            dp[i + 1] = dp[i + 1] + dp[i - 1]
        # At any state, if we are not able to modify something, it is invalid.
        if dp[i + 1] == 0:
            print(dp)
            return 0
    print(dp)
    return dp[l]


print(numDecodings('10'))
print(numDecodings('4612'))
print(numDecodings('2611055971756562'))  # 4
print(numDecodings(
    '5163490394499093221199401898020270545859326357520618953580237168826696965537789565062429676962877038781708385575876312877941367557410101383684194057405018861234394660905712238428675120866930196204792703765204322329401298924190'))