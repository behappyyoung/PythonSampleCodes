"""
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
[2, 11, 6, 3]
11 + 3 = 14
[6, 2, 3, 4]

"""
def houseRobber(arr):
    l = len(arr)
    if l == 0:
        return 0
    elif l == 1:
        return arr[0]
    ms = [0] * (l+1)
    ms[1] = arr[0]
    for i in range(1, l):
        ms[i+1] = max(ms[i], ms[i-1]+ arr[i])
    return ms[l]

# test
print(houseRobber([2, 11, 6, 3]))
