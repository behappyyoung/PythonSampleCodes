def substring_count(mains, subs):
    # import re
    # p = re.compile(subs)
    # fa = p.findall(mains)
    # return len(fa)
    length = len(mains)
    sublength = len(subs)
    count = 0
    for i in xrange(length):
        if mains[i:i+sublength] == subs:
            count += 1

    return count


def minion_game(string):
    vowels = ('A', 'E', 'I','O', 'U')
    s = {}
    k = {}
    length = len(string)
    for i in xrange(length):
        # print(substring_count(string, string[i]))
        for j in xrange(i+1, length+1):
            if string[i] in vowels:
               s[string[i:j]] = substring_count(string, string[i:j])
            else:
                k[string[i:j]] = substring_count(string, string[i:j])

    sc = 0
    kc = 0
    for i in s:
        sc += s[i]
    for i in k:
        kc += k[i]

    print(sc, kc, s, k)
    if sc > kc:
        print('Stuart %s'%sc)
    elif sc == kc:
        print('Draw')
    else:
        print('Kevin %s'%kc)

a = raw_input().strip()
minion_game(a.upper())

