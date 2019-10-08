"""
   Redo 09292019 with python3
   input : string
   output : First character Capitalized String
"""

def capitalizeString(string):
    sa = string.split(' ')
    for i in range(len(sa)):
        sa[i] = sa[i][0].upper() + sa[i][1:].lower()
    return ' '.join(sa)

a = input().strip()

# simple
print(' '.join(map(lambda x :x[0].upper() + x[1:].lower(), a.split(' '))))
# use function
print(capitalizeString(a))