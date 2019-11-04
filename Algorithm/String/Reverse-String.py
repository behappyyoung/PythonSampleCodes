"""
Input 1:
    A = "the sky is blue"
Output 1:
    "blue is sky the"

Input 2:
    A = "this is ib"
Output 2:
    "ib is this"
"""
def reverse_string_with_function(str):
    str_arr = str.split(' ')
    str_arr.reverse()
    return ' '.join(str_arr)


def reverse_string(str):
    str_arr = str.split(' ')
    return_str = ''
    for i in range(len(str_arr)-1, -1, -1):
        return_str = return_str + ' ' + str_arr[i]

    return return_str[1:]

input_str = "the sky is blue"
print(input_str, reverse_string(input_str), reverse_string_with_function(input_str))
input_str = "this is ib"
print(input_str, reverse_string(input_str), reverse_string_with_function(input_str))