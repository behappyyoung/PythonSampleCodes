#!/bin/python

import sys

n = int(raw_input().strip())
divisor=[1, n]
for i in xrange(2, int(n/2)):
	if i in divisor:
		break
	if n % i == 0:
		divisor.append(i)
		divisor.append(n/i)

#print divisor
max = 0
temp = 0
current_max = divisor[0]
for i in divisor:
	s = str(i)
	for j in range(0, len(s)):
		temp += int(s[j])
	#	print j, temp
	if max < temp:
		current_max = i
		max = temp
	elif max == temp:
		if current_max > i:
			current_max = i
	print i, current_max, max, temp
	temp = 0					
print current_max
