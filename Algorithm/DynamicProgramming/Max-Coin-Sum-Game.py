"""
Problem statement: Consider a row of n coins of values v1 . . . vn, where n is even. We play a game against an opponent by alternating turns.
 In each turn, a player selects either the first or last coin from the row, removes it from the row permanently, and receives the value of the coin. Determine the maximum possible amount of money we can definitely win if we move first.

Note: The opponent is as clever as the user.

1. 5, 3, 7, 10 : The user collects maximum value as 15(10 + 5)

2. 8, 15, 3, 7 : The user collects maximum value as 22(7 + 15)

Does choosing the best at each move give an optimal solution?

No. In the second example, this is how the game can finish:

1.
…….User chooses 8.
…….Opponent chooses 15.
…….User chooses 7.
…….Opponent chooses 3.
Total value collected by user is 15(8 + 7)
2.
…….User chooses 7.
…….Opponent chooses 8.
…….User chooses 15.
…….Opponent chooses 3.
Total value collected by user is 22(7 + 15)
So if the user follows the second game state, maximum value can be collected although the first move is not the best.


coinGame() => time limit exceeded

"""

def coinGame(A):
    if not A:
        return 0
    def getTotal(arr, s, e):
        l = e - s
        if l == 1:
            return max(arr[s], arr[e])
        else:
            mine = max(arr[s] + min(getTotal(arr, s+2, e), getTotal(arr, s+1, e-1)),
                       arr[e] + min(getTotal(arr,s+1, e-1), getTotal(arr, s, e-2)))
            return mine

    return getTotal(A, 0, len(A)-1)


"""
 Solution by dynamic programming.
	       dp[i][j] = maximum score possible for current player for subgame A[i:j]
	    Base cases, only one option:
	       dp[i][i+1] = A[i]
	    Otherwise, we pick at either end, eventually getting
	    all the coins but the ones picked by next player:
	       dp[i][j] = sum(A[i:j]) - min(dp[i+1][j], dp[i][j-1])
	    
	    Now, we only have to maintain one column (j-1) to obtain new one (j)
"""

def coinGame_dp(A):
    if not A:
        return 0
    l = len(A)
    lookup = [[0]*l for i in range(l)]

    def getTotal(arr, s, e):
        l = e - s
        if l == 1:
            mine = max(arr[s], arr[e])
            lookup[s][e] = mine
            # print(s, e, lookup, mine)
            return mine
        else:
            lookup[s+2][e] = lookup[s+2][e] if lookup[s+2][e] != 0 else getTotal(arr, s+2, e)
            lookup[s+1][e-1] = lookup[s+1][e-1] if lookup[s+1][e-1] !=0 else getTotal(arr, s+1, e-1)
            lookup[s][e-2] = lookup[s][e-2] if lookup[s][e-2] != 0 else getTotal(arr, s, e-2)
            mine = max(arr[s] + min(lookup[s+2][e], lookup[s+1][e-1]),
                       arr[e] + min(lookup[s+1][e-1], lookup[s][e-2]))
            lookup[s][e] = mine
            # print(s, e, lookup, mine)
            return mine

    getTotal(A, 0, len(A)-1)
    print(lookup[0])
    return lookup[0][l-1]

# print(coinGame([1,2,3,500, 40, 2]))
# print(coinGame_dp([ 46, 12, 42, 67]))
print(coinGame_dp([ 26, 88, 57, 26, 65, 60, 55, 40 ]))