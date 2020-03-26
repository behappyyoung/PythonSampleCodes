"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Input: ["flower","flow","flight"]
Output: "fl"

"""


def common_prefix(strs):
    l = len(strs)
    if l < 1:
        return ''
    if l==1:
        return strs[0]
    f = strs[0]
    if len(f) < 1:
        for s in strs:
            if f != s:
                return ''
        return f
    cs = ''
    i = 0
    diff = False

    while not diff and i < len(f):
        for s in range(1, l):
            if len(strs[s]) <= i:
                diff = True
                break
            if f[i] != strs[s][i]:
                diff = True
                break
        if not diff:
            cs += f[i]
        i += 1
    return cs

# print(common_prefix(["flower","flow","flight"]))
# print(common_prefix(["flower","flow","test"]))
print(common_prefix(["","",""]))
print(common_prefix(["a","a","a"]))
print(common_prefix(["a","ac"]))