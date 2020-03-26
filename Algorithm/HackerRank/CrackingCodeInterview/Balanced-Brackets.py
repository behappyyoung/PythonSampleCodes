'''
3
{[()]}
{[(])}
{{[[(())]]}}

YES
NO
YES
'''


def is_matched(expression):
	bracket = {'}': '{', ']': '[', ')': '('}
	cb = []
	for i in expression:
		c = bracket.get(i)
		if c:  # close bracket
			if len(cb) == 0:

				return False
			elif cb[-1] == c:
				cb.pop()
			else:
				return False

		else:  # open bracket
			cb.append(i)

	if len(cb) == 0:
		return True
	else:
		return False

print(is_matched('{{{}}}'))