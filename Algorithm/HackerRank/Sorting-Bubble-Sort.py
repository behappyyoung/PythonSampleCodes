'''
3
1 2 3

Array is sorted in 0 swaps.
First Element: 1
Last Element: 3

3
3 2 1

Array is sorted in 3 swaps.
First Element: 1
Last Element: 3

'''

n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))

numberOfSwaps=0
for i in xrange(n-1, 0, -1):
    for j in xrange(i):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1]= temp
            numberOfSwaps += 1
print 'Array is sorted in %s swaps.'%numberOfSwaps
print 'First Element: %s'%a[0]
print 'Last Element: %s'%a[n-1]