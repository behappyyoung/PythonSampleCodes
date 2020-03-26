"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.


"""
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return 0

    max_str = s[0]
    max_len = 1
    i = 1
    while i < len(s):
        if s[i] not in max_str:
            max_str += s[i]
            max_len = max(max_len, len(max_str))

        else:
            ni = s[:i].rfind(s[i]) + 1
            max_str = s[ni:i+1]
        print(max_str)
        i += 1
    return max_len


print(lengthOfLongestSubstring('bbtablud'))