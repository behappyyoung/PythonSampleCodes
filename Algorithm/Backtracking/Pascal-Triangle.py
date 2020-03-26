class Solution:
    def generate(self, numRows: int): # -> List[List[int]]:
        if numRows == 0:
            []
        elif numRows == 1:
            return [[1]]
        else:
            solutions = self.generate(numRows - 1)
            c_solution = [1]
            last_pre = solutions[-1] if solutions else []
            for i in range(len(last_pre)-1):
                c_solution += [last_pre[i] + last_pre[i + 1]]

            c_solution.append(1)

            solutions.append(c_solution)
            return solutions

# test
s = Solution()
print(s.generate(5))