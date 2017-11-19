# -*- coding: utf-8 -*-
# @Time    : 2017-11-16 14:23
# @Author  : flyhawk
# @File    : class_priority_queue.py
# @Software: PyCharm Community Edition

import random


class PriorityQueueForTuple:
	def __init__(self):
		self.heap_array = []
		self.current_size = 0

	def enqueue(self, newItem):
		"""
		add new item,
		:param newItem: (priority, key) ,such as (1, 'a')
		:return:
		"""
		self.heap_array.append(newItem)
		self.current_size = self.current_size + 1
		# 拿最后一个数进行比较
		self.shift_up(self.current_size)
	
	# 向上比较并交换
	def shift_up(self, index):
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
	
	def min_child(self, index):
		# if there is only left child, no right child
		if index * 2 + 1 > self.current_size:
			# return left child index
			return index * 2
		
		else:  # there are left child and right child
			# left child is smaller
			if self.heap_array[index * 2][0] < self.heap_array[index * 2 + 1][0]:
				# return left child index
				return index * 2
			else:
				# otherwise return right child index
				return index * 2 + 1
	
	def shift_down(self, index):
		while (index * 2) <= self.current_size:  # the node still has child
			min_child_index = self.min_child(index) - 1
			
			# current node value is greater than all the child, change position
			if self.heap_array[index][0] > self.heap_array[min_child_index][0]:
				self.heap_array[index], self.heap_array[min_child_index] = \
					self.heap_array[min_child_index], self.heap_array[index]
			
			# change index
			index = min_child_index
		# if this heap has been ordered, may use short cut, quit compare
		# else:
		#     return

	# 一次性包括了 percDown 和 minChild 两个函数，似乎更容易理解
	def _shift_down(self, i):
		left = 2 * i + 1
		right = 2 * i + 2
		little = i
		if left < self.size - 1 and self.path[self.queue[left]] <= self.path[self.queue[i]]:
			little = left
		if right <= self.size - 1 and self.path[self.queue[right]] <= self.path[self.queue[little]]:
			little = right
		if little != i:
			self.queue[i], self.queue[little] = self.queue[little], self.queue[i]
			self._perDown(little)

	def build_heap_with_list(self, alist):
		"""
		build a heap with list
		:param alist: alist such as [(0, 'a'), (3, 'b')...]
		:return:
		"""

		self.current_size = len(alist)
		# self.heap_array = [(0, 0)]
		for item in alist:
			self.heap_array.append(item)
			
		# get the middle level to start
		i = len(alist) // 2
		while i > 0:
			self.shift_down(i)
			i -= 1
	
	def dequeue(self):
		_element = self.heap_array[0]
		self.heap_array[0] = self.heap_array[self.current_size]
		self.current_size = self.current_size - 1
		self.heap_array.pop()
		self.shift_down(1)
		return _element

	def is_empty(self):
		if self.current_size == 0:
			return True
		else:
			return False


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
		pqt.enqueue((value, 'v' + str(i)))
		print (value, 'v' + str(i))


def createHeapByList():
	pqt = PriorityQueueForTuple()
	print ('List')
	alist = [(random.randint(1, 100), 'v' + str(i)) for i in range(10)]
	pqt.build_heap_with_list(alist)
	


if __name__ == '__main__':
	createHeapByList()
	# createHeapByInsert()
