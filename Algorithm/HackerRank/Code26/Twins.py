#!/bin/python
'''
3 13
3
'''

n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
pairs=0


def isPrime(x):
	if x < 3:
		return True
	for i in range(3, x, 2):
		if x % i == 0:
			return False

	return True

for i in xrange(n, m-1):
	if isPrime(i) and isPrime(i+2):
		pairs += 1
		#print i, i+2

print pairs

