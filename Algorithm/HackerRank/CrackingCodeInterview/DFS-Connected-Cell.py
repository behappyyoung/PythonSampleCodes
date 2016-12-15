'''Sample Input

4
4
1 1 0 0
0 1 1 0
0 0 1 0
1 0 0 0

Sample Output

5
'''


def count_region(grid, i, j):
	if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
		return 0
	if grid[i][j] == 0:
		return 0
	current = 1
	grid[i][j] = 0
	current += count_region(grid, i, j - 1)
	current += count_region(grid, i, j + 1)
	current += count_region(grid, i - 1, j)
	current += count_region(grid, i - 1, j - 1)

	current += count_region(grid, i - 1, j + 1)
	current += count_region(grid, i + 1, j)
	current += count_region(grid, i + 1, j - 1)

	current += count_region(grid, i + 1, j + 1)
	return current


def get_biggest_region(grid):
	max_region = 0
	for i in xrange(len(grid)):
		for j in xrange(len(grid[0])):
			max_region = max(max_region, count_region(grid, i, j))
	return max_region

n = int(raw_input().strip())
m = int(raw_input().strip())
grid = []
for grid_i in xrange(n):
	grid_temp = map(int, raw_input().strip().split(' '))
	grid.append(grid_temp)
print get_biggest_region(grid)