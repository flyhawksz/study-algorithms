# -*- coding: utf-8 -*-
# @Time    : 2017-11-16 14:23
# @Author  : flyhawk
# @File    : class_priority_queue.py
# @Software: PyCharm Community Edition

import random


class PriorityQueueForTuple:
	def __init__(self):
		self.heap_array = [(0, 0)]
		self.currentSize = 0
	
	def insert(self, newItem):
		"""
		add new item,
		:param newItem: (priority, key) ,such as (1, 'a')
		:return:
		"""
		self.heap_array.append(newItem)
		self.currentSize = self.currentSize + 1
		# 拿最后一个数进行比较
		self.percUp(self.currentSize)
	
	# 向上比较并交换
	def percUp(self, index):
		# 存在2个数字以上
		while index // 2 > 0:
			# 与父节点比较
			if self.heap_array[index][0] < self.heap_array[index // 2][0]:
				# 交换父子节点
				self.heap_array[index], self.heap_array[index // 2] = self.heap_array[index // 2], self.heap_array[index]
				# 序号切换到交换后的父节点
				index = index // 2
			# if more than parent ,quit
			else:
				return
	
	def minChild(self, index):
		# if there is only left child, no right child
		if index * 2 + 1 > self.currentSize:
			# return left child index
			return index * 2
		
		else:  # there are left child and right child
			# left child is smaller
			if self.heap_array[index * 2] < self.heap_array[index * 2 + 1]:
				# return left child index
				return index * 2
			else:
				# otherwise return right child index
				return index * 2 + 1
	
	def percDown(self, index):
		while (index * 2) <= self.currentSize:  # the node still has child
			min_child_index = self.minChild(index)
			
			# current node value is greater than all the child, change position
			if self.heap_array[index][0] > self.heap_array[min_child_index][0]:
				self.heap_array[index], self.heap_array[min_child_index] = \
					self.heap_array[min_child_index], self.heap_array[index]
			
			# change index
			index = min_child_index
		# if this heap has been ordered, may use short cut, quit compare
		# else:
		#     return
	
	#
	def buildHeapWithList(self, alist):
		"""
		build a heap with list
		:param alist: alist such as [(0, 'a'), (3, 'b')...]
		:return:
		"""

		self.currentSize = len(alist)
		for item in alist:
			self.heap_array.append(item)
			
		# get the middle level to start
		i = len(alist) // 2
		while i > 0:
			self.percDown(i)
			i -= 1
	
	def delMin(self):
		retval = self.heap_array[1]
		self.heap_array[1] = self.heap_array[self.currentSize]
		self.currentSize = self.currentSize - 1
		self.heap_array.pop()
		self.percDown(1)
		return retval

	def rearrange_vertex(self, vertex, distance):
		"""
		to find the vertex that key, and rearrage the position
		:param vertex: string
		:param distance: new distance of the vertex
		:return:
		"""
		done = False
		vertex_index = 0
		i = 0
		
		# search key by value
		while not done and i <= self.currentSize:
			if self.heap_array[i][1] == vertex:
				done = True
				vertex_index = i
			else:
				i += 1
		
		# find the index
		if vertex_index > 0:
			# update the distance of the vertex
			self.heap_array[vertex_index] = (distance, self.heap_array[vertex_index][1])
			# compare and change position
			self.percUp(vertex_index)
			
# def printBTree(bt, depth):
# 	if bt:
# 		ch = bt.key
# 	else:
# 		return
# 	# ch = '#'
#
# 	if depth > 0:
# 		print ('%s%s%s' % ((depth - 1) * '  ', '--', ch))
# 	else:
# 		print (ch)
# 	if not bt:
# 		return
# 	printBTree(bt.leftChild, depth + 1)
# 	printBTree(bt.rightChild, depth + 1)


def createHeapByInsert():
	pqt = PriorityQueueForTuple()
	print ('Insert')
	for i in range(0, 100):
		value = random.randint(1, 100)
		pqt.insert((value, 'v' + str(i)))
		print (value, 'v' + str(i))


def createHeapByList():
	pqt = PriorityQueueForTuple()
	print ('List')
	alist = [(random.randint(1, 100), 'v' + str(i)) for i in range(10)]
	pqt.buildHeapWithList(alist)
	


if __name__ == '__main__':
	createHeapByList()
	# createHeapByInsert()
