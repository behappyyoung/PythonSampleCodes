'''
Sample Input

6
6 12 8 10 20 16
5 4 3 2 1 5
Sample Output

9.0

'''
from __future__ import division


def getMean(arr):
	arr_lenth = len(arr)
	if arr_lenth % 2 == 0:
		mean = (arr[arr_lenth // 2 - 1] + arr[arr_lenth // 2]) / 2
	else:
		mean = arr[arr_lenth // 2]
	return mean

n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))
arr_weight = map(int, raw_input().strip().split(' '))
main_arr = []
count = 0
for i in xrange(n):
	for j in xrange(arr_weight[i]):
		main_arr.append(arr[i])
print main_arr, len(main_arr)
main_arr.sort()
arr_lenth = len(main_arr)
if arr_lenth % 2 == 0:
	q1_arr = main_arr[:arr_lenth // 2]
	q3_arr = main_arr[arr_lenth // 2:]
else:
	q1_arr = main_arr[:(arr_lenth // 2)]
	q3_arr = main_arr[(arr_lenth // 2 + 1):]

print q1_arr, getMean(q1_arr), getMean(main_arr), getMean(q3_arr)

print ("%.1f"%( getMean(q3_arr) - getMean(q1_arr) ))