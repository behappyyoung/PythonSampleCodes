'''
Sample Input

10
64630 11735 14216 99233 14470 4978 73429 38120 51135 67060
Sample Output

43900.6
44627.5
4978
'''
from __future__ import division

n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))
arr.sort()
sum = 0
length = len(arr)
mo = 0
max_mo = 1
mo_dict ={}
for i in xrange(0, length):
	sum += arr[i]
	if arr[i] in mo_dict:
		mo_dict[arr[i]] += 1
		if mo_dict[arr[i]] > max_mo:
			max_mo = mo_dict[arr[i]]
			mo = i
	else:
		mo_dict[arr[i]] = 1

if length % 2 == 0: # even
	m = length // 2
	median = (arr[m-1] + arr[m]) / 2
else:
	m = length // 2
	median = arr[m]

mean = sum / length
mode = arr[mo]
print arr, mean, median, mode