from __future__ import division
n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))
weigh_arr = map(int, raw_input().strip().split(' '))
sum = 0
wsum = 0
for i in xrange(n):
    sum += arr[i]*weigh_arr[i]
    wsum += weigh_arr[i]
wmean = sum / wsum
print ("%.1f"%wmean)

