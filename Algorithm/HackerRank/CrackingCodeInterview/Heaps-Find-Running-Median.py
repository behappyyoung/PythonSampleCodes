'''
6
12
4
5
3
8
7

Sample Output
12.0
8.0
5.0
4.5
5.0
6.0

'''
#!/bin/python

import sys


class MinMax(object):

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
			while (i * 2 +1) < self.currentSize:
				if (i * 2 + 2) < self.currentSize:
					if self.minlist[i*2 + 1] > self.minlist[i*2 + 2]:
						min_t = i*2 + 2
					else:
						min_t = i*2 + 1
				else:
					min_t = i*2 + 1
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


			temp = self.minlist[0]
			self.minlist[0] = self.minlist[self.currentSize - 1]
			self.minlist.pop()
			self.currentSize -= 1
			self.sink_down()


			return temp

	class MaxHeap(object):
		def __init__(self):
			self.maxlist = []
			self.currentSize = 0

		def peek(self):
			return self.maxlist[0]

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
			temp = self.maxlist[0]
			self.maxlist[0] = self.maxlist[self.currentSize - 1]
			self.maxlist.pop()
			self.currentSize = self.currentSize - 1
			self.sink_down()
			return temp

	def __init__(self):
		self.minHeap = self.MinHeap()
		self.maxHeap = self.MaxHeap()

	def add(self, value):
		if self.maxHeap.currentSize == 0 :
			self.maxHeap.add(value)  # default to maxHeap
			return

		if value <= self.maxHeap.peek():
			self.maxHeap.add(value)
			if self.maxHeap.currentSize > self.minHeap.currentSize+1:
				temp = self.maxHeap.pop()
				self.minHeap.add(temp)

		else:       # value > small
			self.minHeap.add(value)
			if self.maxHeap.currentSize < self.minHeap.currentSize:
				temp = self.minHeap.pop()
				self.maxHeap.add(temp)

	def get_median(self):
		if self.minHeap.currentSize == self.maxHeap.currentSize:
			median = ( float(self.minHeap.peek()) + float(self.maxHeap.peek()) ) / 2
		else:
			median = float (self.maxHeap.peek() )
		return median

mm = MinMax()

n = int(raw_input().strip())
a = []
a_i = 0
for a_i in xrange(n):
	a_t = int(raw_input().strip())
	a.append(a_t)

for i in xrange(len(a)):
	mm.add(a[i])
	print mm.get_median()