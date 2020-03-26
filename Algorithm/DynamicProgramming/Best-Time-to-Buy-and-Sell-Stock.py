"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction
(i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.



"""
def buySellStock(prices):
    l = len(prices)
    if l <= 1:
        return 0
    max_profit = 0
    find_min = 0
    find_max = 0
    for i in range(1, l):
        if prices[i] < prices[find_min]:
            find_min = i
            find_max = i
        if prices[i] > prices[find_max] and find_min < i:
            find_max = i
        if find_min < find_max:
            max_profit = max(max_profit, prices[find_max]-prices[find_min])
    return max_profit

# test
print(buySellStock([7,3,9,2,6,4]))
print(buySellStock([7,6,4,3,1]))
