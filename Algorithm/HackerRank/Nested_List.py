import sys

n = int(raw_input().strip())
arr = []
for i in range(0, n):
	name=raw_input().strip()
	grade=float(raw_input().strip())
	arr.append([name, grade])

first =100
second = 100
secondArr = []
firstArr = []

for std in arr:
	if first > std[1]:
		second = first
		first = std[1]
		secondArr = firstArr
		firstArr = [std[0]]

	elif first == std[1]:
		firstArr.append(std[0])

	elif second == std[1]:
		secondArr.append(std[0])

	elif second > std[1]:
		second = std[1]
		secondArr = [std[0]]

secondArr.sort()
for s in secondArr:
	print s