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

t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"