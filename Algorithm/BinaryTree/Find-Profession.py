"""

                E
           /         \
          E           D
        /   \        /  \
       E     D      D    E
      / \   / \    / \   / \
     E   D D   E  D   E E   D


"""
def findProfession(level, pos):
    if level == 1:
        return 'Engineer'

    flip = False
    while level >= 2:
        if (pos % 2) == 0:
            flip = not flip
        pos = (pos + 1) // 2
        # odd same profession with parent even = flip

        print(pos, flip, level)
        level -= 1

    print(pos, flip)
    if pos == 1:
        if flip:
            return 'Doctor'
        return 'Engineer'
    else:
        if flip:
            return 'Engineer'
        return 'Doctor'


print(findProfession(4, 2))