T = int(raw_input())
rmin = 10000000
colmin = 10000000
for num in range(0, T):
    ins = raw_input().split(' ')
    rmin = min(rmin, int(ins[0]))
    colmin = min(colmin, int(ins[1]))

print rmin * colmin