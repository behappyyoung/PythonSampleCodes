"""
# https://www.interviewbit.com/problems/grid-unique-paths/



# unique_paths : recursive => too slow  Time Limit Exceeded.
# unique_paths_d : dynamic programming

"""

def unique_paths(r, c):
    if r == 1 or c == 1:
        return 1
    return unique_paths(r-1, c) + unique_paths(r, c-1)


def unique_paths_d(r, c):
    unique_paths = {}

    for row in range(1, r+1):
        for col in range(1, c+1):
            if row == 1 or col == 1:
                unique_paths[str(row)+':'+str(col)] = 1
            else:
                unique_paths[str(row)+':'+str(col)] = unique_paths.get(str(row-1)+':'+str(col)) + unique_paths.get(str(row)+':'+str(col-1))
    return unique_paths.get(str(r)+':'+str(c))

print(unique_paths(2, 2))
print(unique_paths(3, 6))
print(unique_paths(12, 13))
print(unique_paths_d(2, 2))
print(unique_paths_d(100, 1))
# print(unique_paths_d(12, 13))