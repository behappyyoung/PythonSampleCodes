"""
Given an array A of integers,
find the index of values that satisfy A + B = C + D,
where A,B,C & D are integers values in the array

) Return the indices `A1 B1 C1 D1`, so that
  A[A1] + A[B1] = A[C1] + A[D1]
  A1 < B1, C1 < D1
  A1 < C1, B1 != D1, B1 != C1

2) If there are more than one solutions,
   then return the tuple of values which are lexicographical smallest.

Assume we have two solutions
S1 : A1 B1 C1 D1 ( these are values of indices int the array )
S2 : A2 B2 C2 D2

S1 is lexicographically smaller than S2 iff
  A1 < A2 OR
  A1 = A2 AND B1 < B2 OR
  A1 = A2 AND B1 = B2 AND C1 < C2 OR
  A1 = A2 AND B1 = B2 AND C1 = C2 AND D1 < D2

Input: [3, 4, 7, 1, 2, 9, 8]
Output: [0, 2, 3, 5] (O index)

"""


def equals(arr):
    l = len(arr)
    solutions = []
    for i in range(0, l-1):
        a = arr[i]
        for j in range(i+1, l):
            b = arr[j]
            for k in range(i+1, l-1):
                c = arr[k]
                for m in range(k+1, l):
                    d = arr[m]
                    if (a + b) == (c + d) and j != k and b !=m:
                        solutions.append([i, j, k, m])

    return solutions


def equals_hash(arr):
    l = len(arr)
    solutions = []
    sum_dict = {}
    for i in range(0, l-1):
        a = arr[i]
        for j in range(i+1, l):
            b = arr[j]
            c_sum = a + b
            if sum_dict.get(str(c_sum)) is not None:
                c_sum_dict = sum_dict.get(str(c_sum))
                for cd in c_sum_dict:
                    if len(cd) < 3:
                        new_list = cd + [i,j]
                        # new_list.sort()
                        solutions.append(new_list)
                c_sum_dict.append([i, j])

            if sum_dict.get(str(c_sum)) is None:
                sum_dict[str(c_sum)] = [[i, j]]
    print(sum_dict)

    return solutions

input_arr = [3, 4, 7, 1, 2, 9, 8]
print(equals(input_arr))
print(equals_hash(input_arr))