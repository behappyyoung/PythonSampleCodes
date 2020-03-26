"""
Given two integers n and k, return all possible combinations of k numbers out of 1 2 3 ... n.
Within every entry, elements should be sorted. [1, 4] is a valid entry while [4, 1] is not.
Entries should be sorted within themselves.

input If n = 4 and k = 2, a solution is:

output
[
  [1,2],
  [1,3],
  [1,4],
  [2,3],
  [2,4],
  [3,4],
]


"""



def combination_k(n, k):
    if k == 1:
        return [[i] for i in range(1, n+1)]
    if n < k:
        return []


    def combination_sek(n, s, k):
        l = n - s + 1
        print(s,k, l)
        if k == 1:
            return [[i] for i in range(s,n+1)]
        if l < k:
            return []
        solutions = []

        sub_comb = combination_sek(n, s+1, k-1)
        print(s, k, sub_comb)
        for sc in sub_comb:
            solutions.append([s] + sc)
        solutions.extend(combination_sek(n, s+1, k))
        return solutions

    return sorted(combination_sek(n, 1, k))



print(combination_k(4, 3))
print(combination_k(2, 1))
# for check
# from itertools import combinations
# print(list(combinations(range(1,6), 3)))
