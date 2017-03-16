def capitalize(string):
    sa = string.split(' ')
    for i in xrange(len(sa)):
        if len(sa[i]) == 0:
            sa[i] = sa[i].upper()
        else:
            sa[i] = sa[i][0].upper() + sa[i][1:]
    return ' '.join(sa)

a = raw_input().strip()
print capitalize(a)