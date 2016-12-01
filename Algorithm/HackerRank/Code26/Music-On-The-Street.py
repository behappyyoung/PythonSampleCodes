#!/bin/python
'''
2
1 3
7 2 3

-2

5
1 4 7 8 10
7 2 3
'''
n = int(raw_input().strip())        # number of border points

borders = map(int, raw_input().strip().split(' ')) # border points
m, m_min, m_max = map(int, raw_input().strip().split(' '))

total_lenth=0
for i in xrange(1, n):
	distance = (borders[i]-borders[i-1])
	if total_lenth + distance >= m:
		break;
	else:
		total_lenth += distance

s = borders[0] - m_max
print n, borders, m, m_min, m_max, total_lenth, s






