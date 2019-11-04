"""
Given an array of integers, every element appears thrice except for one. Find that single one.


Input : [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
Output : 4


single_number = > n ==> extra space
Could you implement it without using extra memory?

"""

def single_number(arr):
    check_dict = {}
    for i in arr:
        str_i = str(i)
        if str_i in check_dict:
            check_dict[str_i] = False
        else:
            check_dict[str_i] = True

    for check in check_dict:
        if check_dict[check]:
            return check


def single_number_s(arr):
    first = 0
    second = 0
    for i in arr:
        first = (first ^ i) & ~second
        second = (second ^ i) & ~first
    return first

input_arr = [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]

print(single_number(input_arr))
print(single_number_s(input_arr))

input_arr = [ 890, 992, 172, 479, 973, 901, 417, 215, 901, 283, 788, 102, 726, 609, 379, 587, 630, 283, 10, 707, 203, 417, 382, 601, 713, 290, 489, 374, 203, 680, 108, 463, 290, 290, 382, 886, 584, 406, 809, 601, 176, 11, 554, 801, 166, 303, 308, 319, 172, 619, 400, 885, 203, 463, 303, 303, 885, 308, 460, 283, 406, 64, 584, 973, 572, 194, 383, 630, 395, 901, 992, 973, 938, 609, 938, 382, 169, 707, 680, 965, 726, 726, 890, 383, 172, 102, 10, 308, 10, 102, 587, 809, 460, 379, 713, 890, 463, 108, 108, 811, 176, 169, 313, 886, 400, 319, 22, 885, 572, 64, 120, 619, 313, 3, 460, 713, 811, 965, 479, 3, 247, 886, 120, 707, 120, 176, 374, 609, 395, 811, 406, 809, 801, 554, 3, 194, 11, 587, 169, 215, 313, 319, 554, 379, 788, 194, 630, 601, 965, 417, 788, 479, 64, 22, 22, 489, 166, 938, 66, 801, 374, 66, 619, 489, 215, 584, 383, 66, 680, 395, 400, 166, 572, 11, 992 ]

print(single_number(input_arr))
print(single_number_s(input_arr))
