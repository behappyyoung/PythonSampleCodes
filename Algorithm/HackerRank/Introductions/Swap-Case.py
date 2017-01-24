'''
Sample Input

HackerRank.com presents "Pythonist 2".
Sample Output

hACKERrANK.COM PRESENTS "pYTHONIST 2".

'''

S = raw_input().strip()
newS = ''
for s in S:
	if s.islower():
		newS += s.upper()
	elif s.isupper():
		newS += s.lower()
	else:
		newS += s

print newS

