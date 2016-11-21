#!/bin/python


def displayPathtoPrincess(n,grid):
    mloc=()
    ploc=()
    for ri, r in enumerate(grid):
        for ci, c in enumerate(r):
            if c == 'm':
                mloc = (ri, ci)
            if c == 'p':
                ploc = (ri, ci)

    if mloc[0] < ploc[0]:
        for i in xrange(mloc[0], ploc[0]):
            print 'DOWN'
    else:
        for i in xrange(ploc[0], mloc[0]):
            print 'UP'

    if mloc[1] < ploc[1]:
        for i in xrange(mloc[1], ploc[1]):
            print 'RIGHT'
    else:
        for i in xrange(ploc[1], mloc[1]):
            print 'LEFT'

m = input()

grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())

displayPathtoPrincess(m,grid)


