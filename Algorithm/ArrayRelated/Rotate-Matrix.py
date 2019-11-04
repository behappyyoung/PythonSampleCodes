"""
https://www.interviewbit.com/problems/rotate-matrix/

If the array is

[
    [1, 2],
    [3, 4]
]
Then the rotated array becomes:

[
    [3, 1],
    [4, 2]
]



"""
def rotate_matrix(arr_list):
    arr_length = len(arr_list)
    in_arr_length = len(arr_list[0])
    return_list = []
    for i in range(arr_length):
        c_arr = []
        for j in range(in_arr_length):
            c_arr.append(0)
        return_list.append(c_arr)

    for i in range(arr_length):
        for j in range(arr_length):
            return_list[j][in_arr_length-i-1] = arr_list[i][j]
    return return_list


# test
test_list = [[1,2],[3,4]]
print(rotate_matrix(test_list))
test_list = [[5,7,6],[1,5,6],[1,5,8]]
print(rotate_matrix(test_list))