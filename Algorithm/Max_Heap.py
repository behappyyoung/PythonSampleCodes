class MaxHeap(object):
	def __init__(self):
		self.maxlist = []
		self.currentSize = 0

	def peek(self):
		if self.currentSize == 0:
			return None
		else:
			self.maxlist[0]

	def swap(self, a, b):
		temp = self.maxlist[a]
		self.maxlist[a] = self.maxlist[b]
		self.maxlist[b] = temp

	def bubble_up(self):
		i = self.currentSize - 1
		while (i - 1) // 2 >= 0:  # (i-1) // 2 : parent node
			if self.maxlist[i] > self.maxlist[(i - 1) // 2]:
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
				if self.maxlist[i * 2 + 1] < self.maxlist[i * 2 + 2]:
					max_t = i * 2 + 2
				else:
					max_t = i * 2 + 1
			else:
				max_t = i * 2 + 1
			if self.maxlist[i] < self.maxlist[max_t]:
				self.swap(i, max_t)
			else:
				break
			i = max_t


	def add(self, value):
		self.maxlist.append(value)
		self.currentSize += 1
		self.bubble_up()


	def pop(self):
		if self.currentSize == 0:
			return None
		temp = self.maxlist[0]
		self.maxlist[0] = self.maxlist[self.currentSize - 1]
		self.maxlist.pop()
		self.currentSize = self.currentSize - 1
		self.sink_down()
		return temp

m = MaxHeap()
print m.pop(), m.maxlist
m.add(12)
print m.pop(), m.maxlist
m.add(4)
print m.pop(), m.maxlist
m.add(8)
m.add(20)
m.add(2)
m.add(50)
print m.peek(), m.maxlist
print m.pop(), m.maxlist
print m.peek(), m.maxlist