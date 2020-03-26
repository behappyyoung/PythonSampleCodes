"""
input
alphabet = ['b', 'c', 'a']
sentences = ['abc', 'acb', 'baa', 'bc', '']

output
["", "bc", "baa" ]

"""

def customSort(arr, order):

    def sort_function(word):
        # for w in word:
        # print([order.index(c) for c in word])
        return [order.index(c) for c in word]

    # r_arr = sorted(arr, key=sort_function)
    r_arr = sorted(arr, key=lambda word: [order.index(c) for c in word])
    return r_arr


alphabet = ['b', 'c', 'a']
sentences = ['abc', 'acb', 'baa', 'bc', '', 'ca']
print(customSort(sentences, alphabet))