"""
    list has sort() method with number and string
    sorted() function for list with number, string, and object

"""
test = [4, 5, 7, 8, 1, 2, 12]
print(test)
print('sorted : %s' % sorted(test))
print('sorted reverse : %s' % sorted(test, reverse=True))
print('list is unchanged : %s' % test) # same
test.sort()
print('list is changed after sort() : %s' % test) # sorted
test.sort(reverse=True)
print('list is changed after sort(reverse=True) [reverse] : %s' % test) # sorted reverse

testStr = ['a', 'k', 'b', 'c', 'd']
print(testStr)
print('sorted : %s' % sorted(testStr))
print('sorted reverse : %s' % sorted(testStr, reverse=True))
print('list is unchanged : %s' % testStr) # same
testStr.sort()
print('list is changed after sort() : %s' % testStr) # sorted
testStr.sort(reverse=True)
print('list is changed after sort(reverse=True) [reverse] : %s' % testStr) # sorted reverse


class MyObj:
	def __init__(self, name, count):
		self.name = name
		self.count = count

	def __repr__(self):
		return self.name + ' ' + str(self.count)

testObjs = [MyObj('test obj 3', 3)]
testObjs.append(MyObj('test obj 4', 4))
testObjs.append(MyObj('test obj 2', 2))
testObjs.append(MyObj('test obj 6', 6))

print(testObjs)
print(sorted(testObjs, key=lambda x: x.count))
print(sorted(testObjs, key=lambda x: x.count, reverse=True))
print('list is unchanged : %s' % testObjs) # same


def compare_count(item):
	return item.count

print(sorted(testObjs, key=compare_count))