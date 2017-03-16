import string


def insert_dash(str, cut_last = False):
    newstr=''
    for s in str:
        newstr += s + '-'
    if cut_last:
        return newstr[:-1]
    else:
        return newstr


def print_rangoli(size):
    # your code goes here
    for i in xrange(1, size+1):
        dash = (size-i)*2
        alphabet = insert_dash(string.lowercase[size - 1:size - i:-1])+insert_dash(string.lowercase[size - i:size], True)
        print("{dash}{middle}{dash}".format(dash='-'*dash, middle=alphabet))

    for i in xrange(size-1, 0, -1):
        dash = (size - i) * 2
        alphabet = insert_dash(string.lowercase[size - 1:size - i:-1])+insert_dash(string.lowercase[size - i:size], True)
        print("{dash}{middle}{dash}".format(dash='-'*dash, middle=alphabet))

a = int(raw_input().strip())
print_rangoli(a)