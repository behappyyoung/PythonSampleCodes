t = int(raw_input().strip())
answers =[]
for a0 in xrange(t):
	m = int(raw_input().strip())
	n = int(raw_input().strip())
	a = map(int, raw_input().strip().split(' '))

	done = False
	for i in xrange(n):
		s = a[i]
		for j in xrange(i+1, n):
			if s + a[j] == m:
				print (m,n,i,j)
				answers.append([i+1, j+1])
				done = True
				break
		if done:
			break
print answers
for a in answers:
	print a[0], a[1]
