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
Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]


"""

def rotate_matrix(arr_list):
    arr_length = len(arr_list)
    in_arr_length = len(arr_list[0])
    copy_list =  list()

    for i in range(arr_length):
        c_arr = list()
        for j in range(in_arr_length):
            c_arr.append(arr_list[i][j])
        copy_list.append(c_arr)

    print(copy_list)

    for i in range(arr_length):
        for j in range(arr_length):
            arr_list[j][in_arr_length-i-1] = copy_list[i][j]

    print(arr_list)

# test
test_list = [[1,2],[3,4]]
rotate_matrix(test_list)
print(test_list)
test_list = [[5,7,6],[1,5,6],[1,5,8]]
rotate_matrix(test_list)
print(test_list)

"""

 Rotate a 2D array "without using extra space"
 
If the array is 

1 2 3 4 5 6 7 8 9

Then the rotated array becomes: 

7 4 1 8 5 2 9 6 3

"""

"""
Rotate a 2D array without using extra space

If the array is 

1 2 3 4 5 6 7 8 9

Then the rotated array becomes: 

7 4 1 8 5 2 9 6 3


1 2 3 4 5 6 7 8 9
56 96 91 54

Output:

7 4 1 8 5 2 9 6 3
91 56 54 96


1 2 3 
4 5 6 
7 8 9


1=>3=>9=>7=>1

3 2 1
4 5 6
7 8 9

9 2 1
4 5 6
7 8 3

7 2 1
4 5 6
9 8 3


"""


def rotate_2d(arr, size):
    c = 0
    l = len(arr)
    while c != (size - 1):
        arr[c], arr[c + size - 1] = arr[c + size - 1], arr[c]
        arr[c], arr[l - 1 - c] = arr[l - 1 - c], arr[c]
        arr[c], arr[l - size - c] = arr[l - size - c], arr[c]
        c += 1
        print(arr)


input_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rotate_2d(input_arr, 3)
print(input_arr)


