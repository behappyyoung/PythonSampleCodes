"""

Examples:
Input: N = 1, K = 1
Output: 0

Input: N = 2, K = 1
Output: 0

Input: N = 2, K = 2
Output: 1

Input: N = 4, K = 5
Output: 1

Explanation:
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001

On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

Given row N and index K, return the K-th indexed symbol in row N. (The values of K are 1-indexed.) (1 indexed).

get_str = > time limit exceed


"""
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        def get_str(n):
            if n == 1:
                return '0'
            if n == 2:
                return '01'
            pre_str = get_str(n - 1)
            pre_length = len(pre_str)
            s = pre_str + get_str(n - 1)[pre_length//2:] + get_str(n - 1)[:pre_length//2]
            return s

        c_str = get_str(N)
        print(c_str)
        return c_str[K-1]

    def kthGrammar_calculation(self, N: int, K: int) -> int:

        if N == 1:
            return 0
        elif N == 2:
            return 0 if K == 1 else 1
        else:
            pre_pre_length = 2**(N-3)
            if K <= pre_pre_length * 2 :
                return self.kthGrammar_calculation(N-1, K)
            elif pre_pre_length < K <= (pre_pre_length *3):
                return self.kthGrammar_calculation(N-1, K-pre_pre_length)
            else:
                return 1 if self.kthGrammar_calculation(N-1, K-(pre_pre_length*2)) == 0 else 0







s = Solution()
print(s.kthGrammar(3, 4))
print(s.kthGrammar(3, 3))
print(s.kthGrammar_calculation(3, 3))
print(s.kthGrammar_calculation(30,434991989))