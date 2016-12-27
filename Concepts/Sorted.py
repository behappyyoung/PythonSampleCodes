def comparef(a, b):
	return a - b


def comparer(a, b):
	return b - a


test = [4, 5, 7, 8, 1, 2, 12]

print test.sort(), test, test.sort(reverse=True), test
print sorted(test, cmp=comparef)
print sorted(test, cmp=comparer)


def compareSf(a, b):
	if a >= b:
		return 1
	else:
		return -1


def compareSr(a, b):
	if b >= a:
		return 1
	else:
		return -1


testStr = ['a', 'k', 'b', 'c', 'd']
print testStr.sort(), testStr
print sorted(testStr, cmp=compareSr)
print sorted(testStr, cmp=compareSf)


class MyObj:
	def __init__(self, name, count):
		self.name = name
		self.count = count

	def __repr__(self):
		return self.name + ' ' + str(self.count)


testObjs = []
for i in xrange(5):
	testObjs.append(MyObj('test obj' + str(i), i))

print testObjs, testObjs.sort(reverse=True),testObjs

print sorted(testObjs, key=lambda x: x.count, reverse=True)


def compareo(a, b):
	return a.count - b.count


print sorted(testObjs, cmp=compareo)