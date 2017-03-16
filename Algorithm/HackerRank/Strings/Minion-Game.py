def substring_count(mains, subs, starting):
    # import re
    # p = re.compile(subs)
    # fa = p.findall(mains)
    # return len(fa)
    length = len(mains)
    sublength = len(subs)
    count = 0
    for i in xrange(starting, length-sublength+1):
        if mains[i:i+sublength] == subs:
            count += 1

    return count


def minion_game(string):
    vowels = ('A', 'E', 'I','O', 'U')
    s = {}
    k = {}
    kc = 0
    sc = 0
    length = len(string)
    for i in range(length):
        if string[i] in vowels:
            kc += (length - i)
        else:
            sc += (length - i)

        # for j in xrange(i+1, length+1):
        #     if string[i] in vowels:
        #         cur = k.get(string[i:j])
        #         print i, cur
        #         if cur:
        #             k[string[i:j]] = cur + 1
        #         else:
        #             k[string[i:j]] = 1
        #     else:
        #         cur = s.get(string[i:j])
        #         if cur:
        #             s[string[i:j]] = cur + 1
        #         else:
        #             s[string[i:j]] = 1
    # for i in xrange(length):
    #     # print(s, k)
    #
    #     if string[i] in vowels:
    #         for j in xrange(i + 1, length + 1):
    #             print i, j
    #             if not k.get(string[i:j]):
    #                 k[string[i:j]] = substring_count(string, string[i:j], i)
    #     else:
    #         for j in xrange(i + 1, length + 1):
    #             print i, j
    #             if not s.get(string[i:j]):
    #                 s[string[i:j]] = substring_count(string, string[i:j], i)

    # sc = 0
    # kc = 0
    # for i in s:
    #     sc += s[i]
    # for i in k:
    #     kc += k[i]

    # print(sc, kc, s, k)
    if sc > kc:
        print('Stuart %s'%sc)
    elif sc == kc:
        print('Draw')
    else:
        print('Kevin %s'%kc)

a = raw_input().strip()
minion_game(a.upper())

