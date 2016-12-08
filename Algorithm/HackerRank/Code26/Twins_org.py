#!/bin/python
'''
3 13
3
'''
import datetime, math
n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
pairs=0


before_time  = datetime.datetime.now()


def are_primes(x):
	if x < 3:
		return False
	for i in range(3, int(math.sqrt(x))+1, 2):
		if x % i == 0:
			return False
	return True

if (n % 2) == 0:
	startn = n + 1
else:
	startn = n
next_true = False
prev_true = False
iterable = iter(xrange(startn, m-1, 2))
for i in iterable:
	if next_true:
		if are_primes(i+2):
			pairs += 1
			# print i, i+2
			next_true = True
		else:
			next_true = False
			next(iterable)
	else:
		if are_primes(i):
			if are_primes(i+2):
				pairs += 1
				# print i, i+2
				next_true = True
			else:
				next_true = False
				next(iterable)


print pairs

print datetime.datetime.now() - before_time
