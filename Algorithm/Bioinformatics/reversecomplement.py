import sys 
lines = sys.stdin.read().splitlines() 

in_str = lines[0]

r_length = len(in_str)
out_str=''
for i in xrange(r_length-1, -1, -1):
    c_char = in_str[i]
    if c_char == 'T':
        o_char = 'A'
    elif c_char == 'A':
        o_char = 'T'
    elif c_char == 'C':
        o_char = 'G'
    elif c_char =='G':
        o_char = 'C'

    out_str = out_str+o_char
print out_str
