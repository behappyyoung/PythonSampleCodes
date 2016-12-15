'''
Sample Input

5
amy 100
david 100
heraldo 50
aakansha 75
aleksa 150

Sample Output

aleksa 150
amy 100
david 100
aakansha 75
heraldo 50

'''


class Player:
	def __init__(self, name, score):
		self.score = score
		self.name = name

	def __repr__(self):
		return self.name + ' ' + str(self.score)

	def comparator(a, b):
		if b.score > a.score: return 1
		elif a.score == b.score:
			if a.name >= b.name:return 1
			else:return -1
		else:return -1

n = int(raw_input())
data = []
for i in range(n):
	name, score = raw_input().split()
	score = int(score)
	player = Player(name, score)
	data.append(player)
#
# data = sorted(data, cmp=Player.comparator)
# for i in data:
# 	print i.name, i.score
print data, type(data), data[0].name


def comparef(a, b):
	return a-b

test = [4, 5, 7, 8, 1, 2]
test = sorted(test, cmp=comparef)
print test
data = sorted(data, cmp=Player.comparator)
print data