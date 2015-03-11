#!/bin/python


def  maxXor( l,  r):
    max = 0
    for lnum in range(l, r+1):
        for rnum in range(l, r+1):
            max = lnum ^ rnum if lnum ^ rnum > max else max
##            print '%d ^ %d  =>  %d , %d\n ' % (lnum, rnum,  lnum ^ rnum, max)

    return max

    

_l = int(raw_input())
_r = int(raw_input())

if(_l > _r):
    print('wrong input ..  L should less than or equal to R ')
    exit()

res = maxXor(_l, _r)
print(res)

