#!/bin/python
'''
4

2 (1, 2)(1, 3)
'''

import datetime

n = int(raw_input().strip())

pairs=0

before_time  = datetime.datetime.now()
pair_check = {}
for a in range(1, int(n/2) +1) :
	for b in range(a+1, n):
		for x in range(1, n-b+1):
			for y in range(1, n-a+1):
				if (x*a + b*y) == n:

					if pair_check.get((a,b)) is None:
							pairs += 1
							pair_check[(a,b)] = True
							print a, b, '--', x, y, '==', x * a, y * b
					else:
						print a, b, '--', x, y, '==', x * a, y * b , 'same'



print pairs

print datetime.datetime.now() - before_time
'''
n = int(raw_input().strip())

pairs = 0

pair_check = {}
for a in range(1, int(n / 2) + 1):
	for b in range(a + 1, n):
		for x in range(1, n - b + 1):
			for y in range(1, n - a + 1):
				if (x * a + b * y) == n:
					if pair_check.get((a, b)) is None:
						pairs += 1
						pair_check[(a, b)] = True

print pairs
'''