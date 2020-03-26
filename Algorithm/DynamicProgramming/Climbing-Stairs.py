"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps


Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


climb_stairs => time limit exceeded

"""

def climb_stairs(n):
    if n <= 2:
        return n

    ways = climb_stairs(n - 1) + climb_stairs(n - 2)
    return ways


def climb_stairs_hash_list(n):  #recursive
    hash_list = [0] * n
    if n <= 2:
        hash_list[n-1] = n
        return n

    if hash_list[n-1] != 0:
        return hash_list[n-1]
    else:
        ways = climb_stairs_hash_list(n-1) + climb_stairs_hash_list(n-2)
        hash_list[n-1] = ways

    return hash_list[n-1]


def climb_stairs_dp(n):
    if n <= 2: return n
    hash_list = [0] * (n+1)

    hash_list[1] = 1
    hash_list[2] = 2

    for i in range(3, n+1):
        hash_list[i] = hash_list[i-1] + hash_list[i-2]
    return hash_list[n]

print(climb_stairs(30))
print(climb_stairs_hash_list(30))
print(climb_stairs_dp(30))

# from datetime import datetime

# start_time = datetime.now()
# print(climb_stairs(30))
# end_time = datetime.now()
# print(end_time - start_time)
#
#
# start_time = datetime.now()
# print(climb_stairs_hash(30))
# end_time = datetime.now()
# print(end_time - start_time)
#
#
# start_time = datetime.now()
# print(climb_stairs_hash_list(30))
# end_time = datetime.now()
# print(end_time - start_time)
#
# start_time = datetime.now()
# print(climb_stairs_dp(40))
# end_time = datetime.now()
# print(end_time - start_time)

