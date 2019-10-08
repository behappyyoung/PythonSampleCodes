"""
    https://www.interviewbit.com/problems/spiral-order-matrix-i/
    Given the following matrix:

[
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]
You should return

[1, 2, 3, 6, 9, 8, 7, 4, 5]

"""


def spiral_order(arr):
    if len(arr) < 1:
        return []
    spiral_arr = arr.pop(0)
    for i in range(len(arr)-1):
        spiral_arr.append(arr[i].pop(-1))
    for i in range(len(arr[-1])):
        spiral_arr.append(arr[-1].pop(-1))
    del arr[-1]
    for i in range(len(arr)-1, 0, -1):
        spiral_arr.append(arr[i].pop(0))

    # spiral_arr.append(spiral_order(arr))
    print(spiral_arr, arr)


# testing data
test_tuple = [[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ], [10, 11, 12]]
spiral_order(test_tuple)
test_tuple2 = [[1,2],[4, 5], [6,8]]
spiral_order(test_tuple2)