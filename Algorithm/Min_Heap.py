class MinHeap(object):
	def __init__(self):
		self.minlist = []
		self.currentSize = 0

	def peek(self):
		return self.minlist[0]

	def swap(self, a, b):
		temp = self.minlist[a]
		self.minlist[a] = self.minlist[b]
		self.minlist[b] = temp

	def bubble_up(self):
		i = self.currentSize - 1
		while (i - 1) // 2 >= 0:  # (i-1) // 2 : parent node
			if self.minlist[i] < self.minlist[(i - 1) // 2]:
				self.swap(i, (i - 1) // 2)
				i = (i - 1) // 2
			else:
				break

	def sink_down(self):
		if self.currentSize == 1:
			return
		i = 0
		while (i * 2 + 1) < self.currentSize:
			if (i * 2 + 2) < self.currentSize:
				if self.minlist[i * 2 + 1] > self.minlist[i * 2 + 2]:
					min_t = i * 2 + 2
				else:
					min_t = i * 2 + 1
			else:
				min_t = i * 2 + 1
			if self.minlist[i] > self.minlist[min_t]:
				self.swap(i, min_t)
			else:
				break
			i = min_t


	def add(self, value):
		self.minlist.append(value)
		self.currentSize += 1
		self.bubble_up()


	def pop(self):
		if self.currentSize == 0:
			return None
		temp = self.minlist[0]
		self.minlist[0] = self.minlist[self.currentSize - 1]
		self.minlist.pop()
		self.currentSize = self.currentSize - 1
		self.sink_down()
		return temp

m = MinHeap()
m.add(21)
m.add(12)
print m.pop(), m.minlist
m.add(51)
m.add(3)
print m.peek(), m.minlist
m.add(15)
print m.peek(), m.minlist
m.add(8)
print m.pop(), m.minlist
m.add(20)
m.add(2)
m.add(50)
print m.peek(), m.minlist
print m.pop(), m.minlist
print m.peek(), m.minlist