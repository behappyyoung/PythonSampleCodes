"""

Given an array with n objects colored red, white or blue,
sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Input : [0 1 2 0 1 2]
Modify array so that it becomes : [0 0 1 1 2 2]

"""

def sort_by_color(arr):
    red = []
    white = []
    blue = []
    for i in arr:
        if i == 0:
            red.append(i)
        elif i == 1:
            white.append(i)
        elif i==2:
            blue.append(i)
    arr = red
    arr.extend(white)
    arr.extend(blue)
    print(arr)



# test
input_arr = [0, 1, 2, 0, 1, 2]
print(sort_by_color(input_arr))
# for check
input_arr.sort()
print(input_arr)

input_arr = [0]
print(sort_by_color(input_arr))
# for check
input_arr.sort()
print(input_arr)

