def seats(A):
    n = A.count('x')
    totalmove = 0
    lx = 0
    space = 0
    for i in A:
        if i == 'x':
            if space != 0:
                totalmove += min(lx, n - lx) * space
                space = 0
            lx += 1
        else:
            space += 1
    return totalmove % 10000003


print(seats('...x...x..x..x'))
print(seats('xx...'))
