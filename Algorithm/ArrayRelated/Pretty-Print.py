"""
Input: A = 4.
Output:

4 4 4 4 4 4 4
4 3 3 3 3 3 4
4 3 2 2 2 3 4
4 3 2 1 2 3 4
4 3 2 2 2 3 4
4 3 3 3 3 3 4
4 4 4 4 4 4 4

Input: A = 3.
Output:

3 3 3 3 3
3 2 2 2 3
3 2 1 2 3
3 2 2 2 3
3 3 3 3 3

"""

def make_array(n):
    if n == 1:
        return [[1]]
    new_array = make_array(n-1)
    for i in range(int(len(new_array)/2)+1):    #
        new_array[i].insert(0, n)
        new_array[i].append(n)

    adding_list = [n]*(2*n-1)
    new_array.insert(0, adding_list)
    new_array.append(adding_list)
    return new_array

def pretty_print(n):
    my_array = make_array(n)
    for ma in my_array:
        print(ma)

pretty_print(3)
pretty_print(4)