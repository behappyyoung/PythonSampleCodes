#!/bin/python


def  maxXor( l,  r):
    cmax = 0
    for lnum in range(l, r+1):
        for rnum in range(l, r+1):
            cmax = lnum ^ rnum if lnum ^ rnum > cmax else cmax

    return cmax

_l = int(raw_input())
_r = int(raw_input())

if(_l > _r):
    print('wrong input ..  L should less than or equal to R ')
    exit()

res = maxXor(_l, _r)
print(res)

