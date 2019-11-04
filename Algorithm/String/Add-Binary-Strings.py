"""

"""
def add_binary_strings(s1, s2):
    return_str = ''
    length_s1 = len(s1)
    length_s2 = len(s2)
    max_length = max(length_s1, length_s2)
    if length_s1 > length_s2:
        for i in range(length_s1-length_s2):
            s2 = '0' + s2
    elif length_s2 > length_s1:
        for i in range(length_s2-length_s1):
            s1 = '0' + s1
    over_number = 0
    for i in range(max_length-1, -1, -1):
        current_number = int(s1[i]) + int(s2[i]) + over_number
        if current_number >= 2:
            current_number = current_number - 2
            over_number = 1
        else:
            over_number = 0
        return_str = str(current_number) + return_str
    if over_number == 1:
        return_str = '1' + return_str
    return return_str

print(add_binary_strings('1', '1'))
print(add_binary_strings('111', '000001'))
print(add_binary_strings('11111111111111111111111111111111', '1'))