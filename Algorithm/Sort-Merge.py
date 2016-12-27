def merge(arr, l, m, r):
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


def merge_sort(arr, l, r):
	if l < r:
		m = (l+r)/2
		merge_sort(arr, l, m)
		merge_sort(arr, m+1, r)
		merge(arr, l, m, r)


arr = [5, 12, 13, 10, 7, 6, 2]
n = len(arr)

merge_sort(arr, 0, n - 1)

print arr