#!/bin/python
'''
3 13
3 (3, 5)(5, 7)(11, 13)
'''
import datetime, math
n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
pairs=0


before_time  = datetime.datetime.now()


def are_primes(x, prev=False):
	if x < 3:
		return False, False
	if x == 5:
		return True, True
	prev_skip = prev
	prev = True
	for i in range(3, int(math.sqrt(x))+1, 2):
		if x % i == 0:
			return prev, False
		if not prev_skip:
			if (x-2) % i == 0:
				prev = False
				prev_skip = True
	return prev, True

if (n % 2) == 0:
	startn = n + 3
else:
	startn = n + 2

next_true = False
prev_prime = False
this_prime = False
iterable = iter(xrange(startn, m+1, 2))
for i in iterable:

	if not this_prime:
		prev_prime, this_prime  = are_primes(i)
	else:
		prev_prime, this_prime = are_primes(i, True)

	# print i, prev_prime, this_prime
	if this_prime and prev_prime:
		pairs += 1
		# print i - 2, i
	elif not this_prime:
		next(iterable)

print pairs

print datetime.datetime.now() - before_time
