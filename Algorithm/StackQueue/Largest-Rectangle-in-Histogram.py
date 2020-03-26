"""
https://www.interviewbit.com/problems/largest-rectangle-in-histogram/

Given an array of integers A of size N. A represents a histogram
 Width of each bar is 1.
Input 1:
    A = [2, 1, 5, 6, 2, 3]
Output 1:
    10

largest_rectangle => time limit exceeded

"""

def largest_rectangle(arr):
    max_rectangle = 0
    for i in range(len(arr)):
        width = 1
        l = i - 1
        r = i + 1
        ldone = False
        rdone = False
        while not ldone or not rdone:
            if l >= 0:
                if arr[l] >= arr[i]:
                    width += 1
                    l -= 1
                else:
                    ldone = True
            else:
                ldone = True
            if r < len(arr):
                if arr[r] >= arr[i]:
                    width += 1
                    r += 1
                else:
                    rdone = True
            else:
                rdone = True

        c_rectangle = arr[i] * width
        # print(i, c_rectangle, width)
        if c_rectangle > max_rectangle:
            max_rectangle = c_rectangle
    return max_rectangle

def largest_rectangle_s(arr):
    stack = [-1]
    max_rectangle = 0

    for i in range(len(arr)):
        while stack[-1] != -1 and arr[stack[-1]] >= arr[i]:
            last_element_index = stack.pop()
            max_rectangle = max(max_rectangle, arr[last_element_index] * (i-stack[-1]-1) )
        stack.append(i)

    while stack[-1] != -1:
        last_element_index = stack.pop()
        max_rectangle = max(max_rectangle, arr[last_element_index] * (len(arr) - stack[-1]-1))

    return max_rectangle

# print(largest_rectangle([2, 1, 5, 6, 2, 3]))
print(largest_rectangle([ 90, 58, 69, 70, 82, 100, 13, 57, 47, 18 ]))
print(largest_rectangle_s([ 90, 58, 69, 70, 82, 100, 13, 57, 47, 18 ]))
