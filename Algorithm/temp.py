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

if (n % 2) == 0:
	startn = n + 1
else:
	startn = n
next_true = False
iterable = iter(xrange(startn, m-1, 2))
for i in iterable:
	# print next_true, i
	if next_true:
		if isPrime(i+2):
			pairs += 1
			next_true = True
		else:
			next_true = False
			next(iterable)
	else:
		if isPrime(i):
			if isPrime(i+2):
				pairs += 1
				next_true = True
			else:
				next_true = False
				next(iterable)



print pairs