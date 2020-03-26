"""
Given a set of candidate numbers (C) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.

Given candidate set 2,3,6,7 and target 7,
A solution set is:
[2, 2, 3]
[7]

[2, 3, 6, 7]
6
==>
[2,2,2]
[3,3]
[6]

[2, 3]
6
==>
[2,2,2]
[3,3]

[2, 4]
8
==>
[2,2,2,2]
[2,2,4]
[4,4]

"""

g_count = 0
def sum_combination_new(arr, target):
    solutions = []

    def backtracking(c_target, c_arr, sub_arr):

        print('start', c_target, c_arr, sub_arr)
        c_solution = []
        if c_arr > c_target:
            if len(sub_arr) > 0:
                c_solution = backtracking(c_target, sub_arr[0], sub_arr[1:])
            else:
                c_solution = []
        elif c_arr == c_target:
            c_solution = [c_arr]

        else:       # c_arr < c_target:

            # check if c_arr can make target
            if c_target % c_arr == 0:
                c_solution = [[c_arr] * (c_target//c_arr)]

            print('in', c_target, c_arr, sub_arr, c_solution)
            sub_target = c_target - c_arr

            while sub_target > 0:
                global g_count
                g_count += 1
                sub_solution = backtracking(sub_target, c_arr, sub_arr[:])
                print('sub', c_target, c_arr, c_solution,  sub_target, 'sub', sub_solution, g_count)

                if sub_solution:
                    if len(sub_solution) >= 1:
                        if isinstance(sub_solution[0], list):
                            for ss in sub_solution:
                                ss.append(c_arr)
                        else:
                            sub_solution.append(c_arr)
                    else:
                        sub_solution = sub_solution.append(c_arr)

                if sub_solution not in c_solution:
                    c_solution.append(sub_solution)
                sub_target -= c_arr

            print(c_arr, c_target, 'c', c_solution, sub_solution, g_count)
        return c_solution

    # arr.reverse()
    print(arr)
    for i in range(len(arr)):
        c_sol = backtracking(target, arr[i], arr[i+1:])
        if c_sol:
            solutions.append(c_sol)
        print(i, solutions)
    solutions.sort()
    return solutions


def sum_combination(A, t):

    if not A:
        return []
    arr = list(set(A))      # remove duplicates

    solutions = []
    arr.sort()
    if arr[0] == t:
        return [[arr[0]]]
    elif arr[0] > t:
        return []
    c = [arr[0]]
    subt = t - arr[0]
    while subt > 0:
        sub_comb = sum_combination(arr[1:], subt)
        for sc in sub_comb:
            print(sc)
            solutions.append(c + sc)
        c.append(arr[0])
        print(c)
        subt = t - sum(c)
    if subt == 0:
        solutions.append(c)
    solutions.extend(sum_combination(arr[1:], t))
    print(solutions)
    return sorted(solutions)


input_array = [ 2, 3, 6, 8]
target = 8
# print(sum_combination(input_array, target))
input_array = [ 8, 10, 6, 11, 1, 16, 8 ]
target = 28
print(sum_combination(input_array, target))
## [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 ] [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 6 ] [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 8 ] [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 10 ] [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 11 ] [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 6 6 ] [1 1 1 1 1 1 1 1 1 1 1 1 1 1 6 8 ] [1 1 1 1 1 1 1 1 1 1 1 1 6 10 ] [1 1 1 1 1 1 1 1 1 1 1 1 8 8 ] [1 1 1 1 1 1 1 1 1 1 1 1 16 ] [1 1 1 1 1 1 1 1 1 1 1 6 11 ] [1 1 1 1 1 1 1 1 1 1 6 6 6 ] [1 1 1 1 1 1 1 1 1 1 8 10 ] [1 1 1 1 1 1 1 1 1 8 11 ] [1 1 1 1 1 1 1 1 6 6 8 ] [1 1 1 1 1 1 1 1 10 10 ] [1 1 1 1 1 1 1 10 11 ] [1 1 1 1 1 1 6 6 10 ] [1 1 1 1 1 1 6 8 8 ] [1 1 1 1 1 1 6 16 ] [1 1 1 1 1 1 11 11 ] [1 1 1 1 1 6 6 11 ] [1 1 1 1 6 6 6 6 ] [1 1 1 1 6 8 10 ] [1 1 1 1 8 8 8 ] [1 1 1 1 8 16 ] [1 1 1 6 8 11 ] [1 1 6 6 6 8 ] [1 1 6 10 10 ] [1 1 8 8 10 ] [1 1 10 16 ] [1 6 10 11 ] [1 8 8 11 ] [1 11 16 ] [6 6 6 10 ] [6 6 8 8 ] [6 6 16 ] [6 11 11 ] [8 10 10 ]

# print(sum_combination_new(input_array, target))