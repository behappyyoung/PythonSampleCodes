'''
Sample Input

2
5
1 1 1 2 2
5
2 1 3 1 2

Sample Output

0
4

'''


def merge(arr, l, m, r):
	total_swap = 0
	n1 = m-l+1
	n2 = r-m
	L = [0]*n1
	R = [0]*n2
	for i in xrange(0, n1):
		L[i] = arr[l+i]
	for j in xrange(0, n2):
		R[j] = arr[m+j+1]

	i = 0
	j = 0
	k = l
	while i < n1 and j < n2:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1

		else:
			arr[k] = R[j]
			total_swap += (n1-i)
			j += 1

		k += 1
	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1
	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1

	return total_swap


def merge_sort(arr, l, r):
	total_swap = 0
	if l < r:
		m = (l+r)/2
		total_swap += merge_sort(arr, l, m)
		total_swap += merge_sort(arr, m+1, r)
		total_swap += merge(arr, l, m, r)
	return total_swap


def count_inversions(a):
	return merge_sort(a, 0, len(a)-1)

t = int(raw_input().strip())
for a0 in xrange(t):
	n = int(raw_input().strip())
	arr = map(int, raw_input().strip().split(' '))
	print count_inversions(arr)


