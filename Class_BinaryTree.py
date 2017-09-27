# -*- coding: utf-8 -*-
# @Time    : 2017-9-27 14:24
# @Author  : zhangqi
# @File    : Class_BinaryTree.py
# @Software: PyCharm Community Edition

class BTNode:
	"""节点类"""
	def __init__(self, item, leftChild=None, rightChild=None):
		self.item = item
		self.leftChild = leftChild
		self.rightChild = rightChild
		

class BinaryTree:
	"""
	BinaryTree(self, data, lchild, rchild)
	isEmpty(self)
	num_nodes(self)
	getData(self)
	getLeftChild()
	getRightChild()
	setLeftChild(self, btree)
	setRightChild(self, btree)
	traversal(self)   # 遍历二叉树节点迭代器
	forall()
	"""
	
	def __init__(self, item):
		self.root = BTNode(item)
	
	def insertLeft(self, item):
		if self.leftChild is None:
			self.leftChild = BinaryTree(item)
		else:
			t = BinaryTree(item)
			t.leftChild = self.leftChild
			self.leftChild = t
	
	def insertRight(self, item):
		if self.rightChild is None:
			self.rightChild = BinaryTree(item)
		else:
			t = BinaryTree(item)
			t.rightChild = self.rightChild
			self.rightChild = t
		
		
	def isEmpty(self):
		return self.root is None
	
	
	def num_nodes(self):
	
	
	def getData(self):
		return self.root.item
	
	
	def getLeftChild(self):
		return self.leftChild
	
	
	def getRightChild(self):
		return self.rightChild
	
	
	def traversal(self):   # 遍历二叉树节点迭代器
		pass
	
	
if __name__ == '__main__':
	tree = BinaryTree('a')
	tree.insertLeft('b')
	tree.insertRight('c')
	tree.getLeftChild().insertRight('d')
	tree.getRightChild().insertLeft	('e')
	tree.getRightChild().insertRight('f')
	
	
