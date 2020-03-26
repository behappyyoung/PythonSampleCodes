"""
Given two arrays A & B of size N each.
Find the maximum N elements from the sum combinations (Ai + Bj) formed from elements in array A and B.

For example if A = [1,2], B = [3,4], then possible pair sums can be 1+3 = 4 , 1+4=5 , 2+3=5 , 2+4=6
and maximum 2 elements are 6, 5

N = 4
a[]={1,4,2,3}
b[]={2,5,1,6}

Maximum 4 elements of combinations sum are
10   (4+6),
9    (3+6),
9    (4+5),
8    (2+6)

n = 1
a = [1, 2, 3, 4]

b = [30, 40, 50, 60]

64,65,62,61

"""
import heapq
def max_pair_combination(A, B):
    if not A and not B:
        return []
    if not A:
        B.sort(reverse=True)
        return B
    if not B:
        A.sort(reverse=True)
        return A
    l = len(A)
    r_arr = list()
    A.sort(reverse = True)
    B.sort(reverse = True)
    print(A, B)
    for i in range(l):
        r_arr.append(A[0] + B[i])

    heapq.heapify(r_arr)
    for i in range(1, l):
        for j in range(l):
            c_sum = a[i] + B[j]
            h_small = heapq.nsmallest(1, r_arr)[0]
            if c_sum > h_small:
                heapq.heappop(r_arr)
                heapq.heappush(r_arr, c_sum)
            else:
                break

    r_arr.sort(reverse=True)
    print(r_arr)


def max_pair_combination_p(A, B):
    if not A and not B:
        return []
    if not A:
        B.sort(reverse=True)
        return B
    if not B:
        A.sort(reverse=True)
        return A
    l = len(A)
    A.sort(reverse=True)
    B.sort(reverse=True)
    print(A, B)
    c_max = A[0] + B[0]
    count = 1
    r_arr = [c_max]
    i = 1
    j = 1
    pre_i = 0
    pre_j = 0
    while count < l:
        pre_i_sum = A[pre_i] + B[j]
        pre_j_sum = A[i] + B[pre_j]
        # if A[i] + B[pre_j] > A[pre_i] + B[j]:
        #
        # elif A[i + 1] + B[j] > A[i] + B[j + 1]:
        #     c_max = A[i + 1] + B[j]
        #     i += 1
        # else:
        #     c_max = A[i] + B[j + 1]
        #     j += 1
        # if pre_i == i and pre_j == j :
        #     i += 1
        #     j += 1
        print(pre_i, i, pre_j, j, c_max, r_arr)
        r_arr.append(c_max)
        count += 1

    print(r_arr)
# a = [1, 2, 3, 4]
# b = [30, 40, 50, 60]
# max_pair_combination(a, b)
# a=[1,4,2,3,9, 30]
# b=[2,5,1,6,4, 30]
# max_pair_combination(a, b)
# a=[3,4]
# b=[3,4]
# max_pair_combination(a, b)
a = [ 3, 2, 4, 2 ]
b = [ 4, 3, 1, 2 ]
max_pair_combination(a, b)

a = [ 50, 49, 48, 47 ]
b = [ 9, 8, 7, 6 ]
max_pair_combination(a, b)