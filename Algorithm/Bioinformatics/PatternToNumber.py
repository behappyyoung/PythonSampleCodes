import sys
lines = sys.stdin.read().splitlines()

in_str = lines[0]
total_num = 0
sq = -1
for i in range(len(in_str)-1, -1, -1):
    c_char = in_str[i:i+1]
    sq = sq + 1
    c_num = 0
    if c_char == 'C':
        c_num = 1
    elif c_char == 'G':
        c_num = 2
    elif c_char == 'T':
        c_num = 3
    print (c_num, sq, c_num * (4**sq))
    total_num = total_num + c_num * (4**sq)

print (total_num)