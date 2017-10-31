# -*- coding: utf-8 -*-
# @Time    : 2017-10-31 11:47
# @Author  : zhangqi
# @File    : Class_BinaryHeap.py
# @Software: PyCharm Community Edition

# this heap takes key value pairs, we will assume that the keys are integers
import random
from Class_BinaryTree2 import binaryTree, treeNode


class BinHeap:
	def __init__(self):
		self.heapList = [0]
		self.currentSize = 0

	def insert(self, newItem):
		self.heapList.append(newItem)
		self.currentSize = self.currentSize + 1
		self.percUp(self.currentSize)

	def percUp(self, index):
		while index // 2 > 0:
			if self.heapList[index] < self.heapList[index//2]:
				tmp = self.heapList[index // 2]
				self.heapList[index // 2] = self.heapList[index]
				self.heapList[index] = tmp
	
				index = index // 2
				
			# if more than parent ,quit
			else:
				return


def printBTree(bt, depth):
	
	if bt:
		ch = bt.key
	else:
		return
		# ch = '#'
		
	if depth > 0:
		print '%s%s%s' % ((depth - 1) * '  ', '--', ch)
	else:
		print ch
	if not bt:
		return
	printBTree(bt.leftChild, depth + 1)
	printBTree(bt.rightChild, depth + 1)


if __name__ == '__main__':
	bh = BinHeap()
	print 'Insert'
	for i in range(0, 100):
		value = (random.random() * 100)
		bh.insert(value)
		print value
	print 'Print Heap'
	tree = binaryTree()
	tree = tree.createLevelOrderTreeWithQueue(bh.heapList)
	printBTree(tree, 0)
