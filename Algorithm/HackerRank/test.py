import sys
import re

n = int(raw_input().strip())
arr = []
for i in range(0, n):
	arr.append(raw_input().strip())

print n, arr

for i in range(0,n):
   print arr[i]
   print  bool(re.search(r'^[+-]?\d+\.\d+', arr[i]))

