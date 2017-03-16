def print_formatted(number):
    # your code goes here
    blen = len(bin(number))-2
    for i in xrange(1, number+1):
        print("{0:{l}d} {0:{l}o} {0:{l}X} {0:{l}b} ".format(i, l=blen))

a = int(raw_input().strip())
print_formatted(a)