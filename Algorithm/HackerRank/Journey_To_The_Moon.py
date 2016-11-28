# Enter your code here. Read input from STDIN. Print output to STDOUT

N, l = map(int,raw_input().split())

groups={}
group_count = 0;
isin = False
current =''
for i in xrange(l):
    a, b = map(int, raw_input().split())
    # Store a and b in an appropriate data structure
    if group_count == 0:
        groups[0] = [a, b]
        group_count = 1
        isin = True
    else:
        for g in xrange(group_count):
            if a in groups[g] or b in groups[g]:
                if isin :   # already in other group current => combine groups[c] <- groups[g]
                    for ing in groups[g]:
                        # print 'error' , g, ing, current
                        if ing not in groups[current]:
                            groups[current].append(ing)
                    # groups.pop(g)
                    groups[g] = []
                    if a not in groups[current]:
                            groups[current].append(a)
                    if b not in groups[current]:
                        groups[current].append(b)
                else:        
                    if a not in groups[g]:
                        groups[g].append(a)
                    if b not in groups[g]:
                        groups[g].append(b)
                    isin = True
                    current = g
            
        
    if isin:
        isin = False
        current = ''
    else:
        groups[group_count] = [a, b]
        group_count += 1

# print group_count, groups


result = 0
# Compute the final result using the inputs from above
remaining = N
for c in groups:
    remaining = remaining - len(groups[c])
    result += ( len(groups[c]) * remaining )

result += ( remaining * (remaining-1) )/2
print result