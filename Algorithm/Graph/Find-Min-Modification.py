"""
Given a matrix of direction with L, R, U, D, at any point you can move to the direction which is written over the cell [i, j]. We have to tell minimum number of modifications to reach from [0, 0] to [N - 1, M - 1] .

Example :-
R R D
L L L
U U R
Answer is 1, we can modify cell [1, 2] from L To D.


"""

def minModification(grid):
    m, n = len(grid), len(grid[0])
    di = {"L": 0, "R": 0, "U": -1, "D": 1}
    dj = {"L": -1, "R": 1, "U": 0, "D": 0}

    def walk(i, j):
        while 0 <= i < m and 0 <= j < n and grid[i][j] in di:
            yield i, j
            grid[i][j], i, j = "X", i + di[grid[i][j]], j + dj[grid[i][j]]

    q = list(walk(0, 0))
    print(q, grid)

    dd = list(zip([-1, 0, 1, 0], [0, -1, 0, 1]))
    result = 0

    while q:
        print(q)
        if (m - 1, n - 1) in q:
            return result
        result += 1
        cq = list()
        for (i, j) in q:
            for (a, b) in dd:
                cq.extend(list(walk(i+a, j+b)))
        q = cq

    return -1

def minModification_solution(grid):
    m, n = len(grid), len(grid[0])
    di = {"L": 0, "R": 0, "U": -1, "D": 1}
    dj = {"L": -1, "R": 1, "U": 0, "D": 0}

    def walk(i, j):
        while 0 <= i < m and 0 <= j < n and grid[i][j] in di:
            yield i, j
            grid[i][j], i, j = "X", i + di[grid[i][j]], j + dj[grid[i][j]]

    q = list(walk(0, 0))
    result = 0
    while q:
        print(q)
        if (m - 1, n - 1) in q:
            return result
        q = [
            (x, y)
            for i, j in q
            for a, b in zip([-1, 0, 1, 0], [0, -1, 0, 1])
            for x, y in walk(i + a, j + b)
        ]
        result += 1
    return -1


# grids = ["RRRR", "LLLL","RRRR", "RRRR"]
grids = ["RRRRR", "LLDLL","RRRRR", "RRRRR", "RRRRR"]
grid = [list(row) for row in grids]
print(minModification(grid))
grid = [list(row) for row in grids]
print(minModification_solution(grid))