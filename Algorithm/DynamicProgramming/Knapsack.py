# A Dynamic Programming based Python Program for 0-1 Knapsack problem
# Returns the maximum value that can be put in a knapsack of capacity W
def knapSack_simple(W, wt, val, n):
    # Base Case
    if n == 0 or W == 0:
        return 0
    print(W, wt, val, n)
    # If weight of the nth item is more than Knapsack of capacity
    # W, then this item cannot be included in the optimal solution
    if (wt[n - 1] > W):
        return knapSack_simple(W, wt, val, n - 1)

        # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(val[n - 1] + knapSack_simple(W - wt[n - 1], wt, val, n - 1),
                   knapSack_simple(W, wt, val, n - 1))


def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    print(K)
    return K[n][W]

def knapSack_yp(total_w, wt_arr, val_arr):
    # Base Case
    n = len(wt_arr)
    if n == 0 or W == 0:
        return 0

    def khelper(subt, s):  # t : current total, s : start index
        if s >= n:
            return 0
        t_max = 0
        for i in range(s, n - 1):
            t = 1
            while (subt - wt_arr[i] * t) >= 0:
                prev_max = khelper(subt, i + 1)
                add_more = val_arr[i] * t + khelper(subt - wt_arr[i] * t, i + 1)
                c_max = max(prev_max, add_more)

                #print(subt, wt_arr[i] * t, t_max, c_max, i, t, prev_max, add_more)
                t_max = max(t_max, c_max)
                t += 1
        return t_max

    return khelper(total_w, 0)


def knapSack_yp_dp(total_w, wt_arr, val_arr):
    # Base Case
    n = len(wt_arr)
    if n == 0 or W == 0:
        return 0

    def khelper(subt, s):  # t : current total, s : start index
        if s >= n:
            return 0
        t_max = 0
        for i in range(s, n - 1):
            t = 1
            while (subt - wt_arr[i] * t) >= 0:
                prev_max = khelper(subt, i + 1)
                add_more = val_arr[i] * t + khelper(subt - wt_arr[i] * t, i + 1)
                c_max = max(prev_max, add_more)

                #print(subt, wt_arr[i] * t, t_max, c_max, i, t, prev_max, add_more)
                t_max = max(t_max, c_max)
                t += 1
        return t_max

    return khelper(total_w, 0)

# Driver program to test above function
val = [60, 100, 220]
wt = [10, 20, 30]
W = 70

n = len(val)
print(knapSack_yp(W, wt, val))
# print(knapSack(W, wt, val, n))

