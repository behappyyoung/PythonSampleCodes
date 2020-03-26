"""
word character limit = 32
dictionary is in dict..
"atiger"

"thisisaword"
d['a']

d = { 'a': 'a', 'tiger': 'animal', 'this': 'this', 'is':'is'}
d['aa']
 = > errror

"""


def new_words(d, s):
    if not s:
        ''
    r_arr = list()
    c_word = ''
    j = 0
    i = 0
    while i < len(s):
        c_word += s[i]
        if c_word in d:
                r_arr.append(c_word)
                c_word = ''
                j = i
        else:
            if i > 32 or i == len(s)-1:
                if r_arr:
                    c_word = r_arr.pop()
                    i = j
                else:
                    return 'no word'
        i += 1

        print(i,j, c_word, r_arr)

    r_str = ''
    for a in r_arr:
        r_str += a + ' '

    return r_str[:-1]


dictionary = { 'a': 'a','an':'an', 'tiger': 'animal', 'this': 'this', 'is':'is'}

print(new_words(dictionary, 'atiger'))

print(new_words(dictionary, 'antiger'))

print(new_words(dictionary, 'attt'))