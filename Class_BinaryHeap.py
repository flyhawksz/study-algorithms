# -*- coding: utf-8 -*-
# @Time    : 2017-10-31 11:47
# @Author  : zhangqi
# @File    : Class_BinaryHeap.py
# @Software: PyCharm Community Edition

# this heap takes key value pairs, we will assume that the keys are integers
import random
from Class_BinaryTree import binaryTree
from cStringIO import StringIO
import math


class BinHeap:
	def __init__(self):
		self.heapList = [0]
		self.currentSize = 0

	def insert(self, newItem):
		self.heapList.append(newItem)
		self.currentSize = self.currentSize + 1
		# 拿最后一个数进行比较
		self.percUp(self.currentSize)

	# 向上比较并交换
	def percUp(self, index):
		# 存在2个数字以上
		while index // 2 > 0:
			# 与父节点比较
			if self.heapList[index] < self.heapList[index // 2]:
				# 交换父子节点
				self.heapList[index], self.heapList[index // 2] = self.heapList[index // 2], self.heapList[index]
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
			if self.heapList[index * 2] < self.heapList[index * 2 + 1]:
				# return left child index
				return index * 2
			else:
				# otherwise return right child index
				return index * 2 + 1

	def percDown(self, index):
		while (index * 2) <= self.currentSize:  # the node still has child
			minChildIndex = self.minChild(index)

			# current node value is greater than all the child, change position
			if self.heapList[index] > self.heapList[minChildIndex]:
				self.heapList[index], self.heapList[minChildIndex] = \
					self.heapList[minChildIndex], self.heapList[index]

			# change index
			index = minChildIndex
		# if this heap has been ordered, may use short cut, quit compare
		# else:
		#     return

	#
	def buildHeapWithList(self, alist):
		# get the middle level to start
		i = len(alist) // 2
		self.currentSize = len(alist)
		self.heapList = [0] + alist[:]
		while i > 0:
			self.percDown(i)
			i -= 1

	def delMin(self):
		retval = self.heapList[1]
		self.heapList[1] = self.heapList[self.currentSize]
		self.currentSize = self.currentSize - 1
		self.heapList.pop()
		self.percDown(1)
		return retval


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


def show_tree(tree, total_width=36, fill=' '):
	output = StringIO()
	last_row = -1
	for i, n in enumerate(tree):
		if i:
			row = int(math.floor(math.log(i + 1, 2)))
		else:
			row = 0
		if row != last_row:
			output.write('\n')
		columns = 2 ** row
		col_width = int(math.floor((total_width * 1.0) / columns))
		output.write(str(n).center(col_width, fill))
		last_row = row
	print output.getvalue()
	print '-' * total_width
	print
	return


# data = random.sample(range(1,8), 7)
# print 'data: ', data
# show_tree(data)

def createHeapByInsert():
	bh = BinHeap()
	print 'Insert'
	for i in range(0, 20):
		value = (random.randint(1, 20))
		bh.insert(value)
		print value
	print 'Print Heap'
	# tree = binaryTree()
	# tree = tree.createLevelOrderTreeWithQueue(bh.heapList)
	show_tree(bh.heapList)


def createHeapByList():
	bh = BinHeap()
	print 'List'
	alist = [random.randint(1, 100) for i in range(9)]
	bh.buildHeapWithList(alist)
	# tree = binaryTree()
	# tree = tree.createLevelOrderTreeWithQueue(bh.heapList)
	show_tree(bh.heapList)


# printBTree(tree, 0)


if __name__ == '__main__':
	createHeapByList()
	createHeapByInsert()

	# data = random.sample(range(1,8), 7)
	# print 'data: ', data
	# show_tree(data)