"""
You are given with an array of 1s and 0s. And you are given with an integer M, which signifies number of flips allowed.
Find the position of zeros which when flipped will produce maximum continuous series of 1s.

For this problem, return the indices of maximum continuous series of 1s in order.

Input :
Array = {1 1 0 1 1 0 0 1 1 1 }
M = 1

Output :
[0, 1, 2, 3, 4]


"""

def max_continuous_1s(arr, m):
    c_start = 0
    c_end = 0
    c_count = 0
    max_count = 0
    max_start = 0
    max_end = 0
    flipped = 0

    while c_end < len(arr):
        if arr[c_end] == 0:
            if flipped < m:
               flipped += 1
               c_count += 1
               c_end += 1
            else:
                if arr[c_start] == 0:
                    flipped -= 1
                c_count -= 1
                c_start += 1
        else:
            c_count += 1
            c_end += 1


        print(c_start, c_end, c_count, flipped)
        if c_count > max_count:
            max_count = c_count
            max_start = c_start
            max_end = c_end

    print(max_start, max_end, max_count)
    print_out = []
    for i in range(max_start, max_end):
        print_out.append(i)
    return print_out

# test
input_arr = [1, 1, 0, 1, 1, 0, 0, 1, 1, 1]

print(max_continuous_1s(input_arr, 1))



