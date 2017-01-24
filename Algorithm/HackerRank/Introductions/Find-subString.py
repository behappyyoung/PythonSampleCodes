'''
Sample Input

ABCDCDC
CDC

Sample Output

2

'''


def count_substring(string, sub_string):
	count = 0
	for i in xrange(len(string)-len(sub_string)+1):
		print i, string[i], sub_string[0]
		if string[i] == sub_string[0]:
			match = True
			in_i = i+1
			for j in xrange(1, len(sub_string)):
				print i, string[in_i], sub_string[j]
				if string[in_i] != sub_string[j]:
					match = False
					break
				in_i += 1
			if match:
				count += 1

	return count

S = raw_input().strip()
subS = raw_input().strip()

print count_substring(S, subS)

