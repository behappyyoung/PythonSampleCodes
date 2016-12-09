'''
Sample Input

3
12
5
7
Sample Output

Not prime
Prime
Prime
'''
import math


def is_prime(x):
	if x == 2:
		return True
	if x < 2 or x % 2 == 0:
		return False

	for i in range(3, int(math.sqrt(x)) + 1, 2):
		if x % i == 0:
			return False
	return True


p = int(raw_input().strip())
for _ in xrange(p):
	n = int(raw_input().strip())
	if is_prime(n):
		print 'Prime'
	else:
		print 'Not prime'