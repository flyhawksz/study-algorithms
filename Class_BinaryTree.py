# -*- coding: utf-8 -*-
# @Time    : 2017-9-27 14:24
# @Author  : zhangqi
# @File    : Class_BinaryTree.py
# @Software: PyCharm Community Edition

class BTNode:
	"""节点类"""
	def __init__(self, item=None, leftChild=None, rightChild=None):
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
	
	def __init__(self, item=None):
		self.tree = BTNode(item)
		
	def setRoot(self, item):
		self.tree.item = item
	
	
	def insertLeft(self, item):
		if self.tree.leftChild is None:
			self.tree.leftChild = BinaryTree(item)
		else:
			t = BinaryTree(item)
			t.leftChild = self.tree.leftChild
			self.tree.leftChild = t
	
	def insertRight(self, item):
		if self.tree.rightChild is None:
			self.tree.rightChild = BinaryTree(item)
		else:
			t = BinaryTree(item)
			t.rightChild = self.tree.rightChild
			self.tree.rightChild = t
		
		
	def isEmpty(self):
		return self.tree is None
	
	
	def num_nodes(self):
		pass
	
	
	def getData(self):
		return self.tree.item
	
	
	def getLeftChild(self):
		return self.tree.leftChild
	
	
	def getRightChild(self):
		return self.tree.rightChild
	
	
	def traversal(self):   # 遍历二叉树节点迭代器
		pass
	
	def createBinaryTreeInPreorder(self):  # 创建二叉树，遵循前序遍历方式输入
	
	
if __name__ == '__main__':
	tree = BinaryTree('a')
	tree.insertLeft('b')
	tree.insertRight('c')
	tree.getLeftChild().insertRight('d')
	tree.getRightChild().insertLeft	('e')
	tree.getRightChild().insertRight('f')
	
	
