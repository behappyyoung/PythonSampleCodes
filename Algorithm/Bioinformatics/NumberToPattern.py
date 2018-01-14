import sys
lines = sys.stdin.read().splitlines()

in_num = int(lines[0])
in_k = int(lines[1])

out_str = ''
next_num = in_num
for i in range(in_k-1, -1, -1):
    sq = 4**i
    c_num = int(next_num / sq)
    next_num = next_num % sq
    if c_num == 0:
        c_char = 'A'
    elif c_num == 1:
        c_char = 'C'
    elif c_num == 2:
        c_char = 'G'
    elif c_num == 3:
        c_char = 'T'

    out_str = out_str + c_char

print(out_str)