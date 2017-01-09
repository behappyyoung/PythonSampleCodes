'''
Sample Input

9
3 7 8 5 12 14 21 13 18
Sample Output

6
12
16

'''


def getMean(arr):
	arr_lenth = len(arr)
	if arr_lenth % 2 == 0:
		mean = (arr[arr_lenth / 2 - 1] + arr[arr_lenth / 2]) / 2
	else:
		mean = arr[arr_lenth / 2]
	return mean

n = int(raw_input().strip())
main_arr = map(int, raw_input().strip().split(' '))
main_arr.sort()
arr_lenth = len(main_arr)
if arr_lenth % 2 == 0:
	q1_arr = main_arr[:arr_lenth / 2]
	q3_arr = main_arr[arr_lenth / 2:]
else:
	q1_arr = main_arr[:(arr_lenth / 2)]
	q3_arr = main_arr[(arr_lenth / 2 + 1):]

print q1_arr, getMean(q1_arr), getMean(main_arr), getMean(q3_arr)

