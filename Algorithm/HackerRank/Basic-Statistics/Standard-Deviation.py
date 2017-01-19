'''
Sample Input

5
10 40 30 50 20
Sample Output

14.1

'''
from __future__ import division
import math

n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))

main_arr = []
sd = 0
total = 0
for i in xrange(n):
	total += arr[i]

mean = total / n
s_total = 0
for i in xrange(n):
	s_total += (mean - arr[i]) * (mean - arr[i])

s_mean = s_total / n

sd = math.sqrt(s_mean)
print ("%.1f"%( sd ))