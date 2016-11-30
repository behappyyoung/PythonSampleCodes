#!/bin/python

import sys

n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]

bombn = (n / 2) + (n % 2)
bombm = (m / 2) + (m % 2)
totalbomb = bombm * bombn
print totalbomb