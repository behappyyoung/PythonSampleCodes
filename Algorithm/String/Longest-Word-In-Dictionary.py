"""
For example, given the input of S = "abppplee" and
D = {"able", "ale", "apple", "bale", "kangaroo"}
the correct output would be "apple"

"""
def lengthOfLongestinDictionary(s, d):
    """
    :type s: str
          d: list of str
    :rtype: int
    """
    if not s:
        return 0

    d = sorted(d, key=lambda w: len(w),  reverse=True)
    in_str = False
    for ds in d:
        for i in range(len(ds)):
            if ds[i] in s:
                in_str = True
            else:
                in_str = False
                break
        print(ds, in_str)
        if in_str:
            return len(ds)

    return 0

dictionary={"able", "ale", "apple", "bale", "kangaroo"}

print(lengthOfLongestinDictionary('abppplee', dictionary))