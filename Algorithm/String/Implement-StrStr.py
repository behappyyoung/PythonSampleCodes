"""
string.find()

"""

def string_find(main_s, sub_s):
    find_it = -1
    for i in range(len(main_s)):
        if main_s[i] == sub_s[0]:
            if len(main_s) - i >= len(sub_s):
                find_it = i
                for j in range(1, len(sub_s)):
                    if main_s[i+j] != sub_s[j]:
                        find_it = -1
                        break
                if find_it != -1:
                    break
    return find_it

main_string = 'test sting has sub string'
sub_string = 'sub'
print(string_find(main_string, sub_string))
sub_string = 'ttt'
print(string_find(main_string, sub_string))