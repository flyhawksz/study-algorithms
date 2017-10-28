# -*- coding: utf-8 -*-
# @Time    : 2017-9-27 14:24
# @Author  : zhangqi
# @File    : Class_BinaryTree.py
# @Software: PyCharm Community Edition

from Class_SStack import SStack

myTree = None

class treeNode:
	def __init__(self, rootObj = None, leftChild = None, rightChild = None):
		self.key = rootObj
		self.leftChild = None
		self.rightChild = None

class binaryTree:
	"""
	BinaryTree(self, binaryTreeObj)
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

	_buildTreeIndex = 0

	def __init__(self):
		self.root = treeNode()

	def createTreeByInput(self, root):
		tmpKey = raw_input("please input a key, input '#' for Null")
		if tmpKey == '#':
			root = None
		else:
			root = treeNode(rootObj=tmpKey)
			root.leftChild = self.createTreeByInput(root.leftChild)
			root.rightChild = self.createTreeByInput(root.rightChild)

		return root

	def createTreeByListWithRecursion(self, preOrder, index=0):
		"""
		根据前序列表和中序列表,重建二叉树
		:param preOrder: 输入前序列表
		:return: 二叉树
		"""
		if preOrder is None or len(preOrder) <= 0:
			return None

		if preOrder[0] is '#':
			root = None
		else:
			self._buildTreeIndex = self._buildTreeIndex + 1
			root = treeNode(preOrder[0])
			root.leftChild = self.createTreeByList(preOrder[1:])
			root.rightChild = self.createTreeByList(preOrder[self._buildTreeIndex+1:])
			list
		return root

	def createTreeByListWithStack(self, preOrderString):
		"""
		根据前序列表和中序列表,重建二叉树
		:param preOrder: 输入前序列表
		:return: 二叉树
		"""
		preOrder = list(preOrderString)
		pStack = SStack()
		if preOrder is None or len(preOrder) <= 0:
			return None

		tmpItem = preOrder.pop(0)
		if tmpItem is '#':
			root = None
		else:
			root = treeNode(tmpItem)

		pStack.push(root)
		currentRoot = root

		while preOrder:
			tmpItem = preOrder.pop(0)
			if tmpItem is '#':
				currentRoot.leftChild = None
				parent = pStack.pop()
				currentRoot = parent
				tmpItem = preOrder.pop(0)
				if tmpItem is '#':
					currentRoot.rightChild = None
					parent = pStack.pop()
					currentRoot = parent
				else:
					currentRoot = self.insertRight(currentRoot, tmpItem)
					pStack.push(currentRoot)

			else:
				if currentRoot.leftChild is None:
					currentRoot = self.insertLeft(currentRoot, tmpItem)
					pStack.push(currentRoot.leftChild)
					currentRoot = currentRoot.leftChild
				else:
					currentRoot = self.insertRight(currentRoot, tmpItem)
					pStack.push(currentRoot.rightChild)
					currentRoot = currentRoot.rightChild

		return root

	def insertLeft(self, root, newNode):
		if root.leftChild is None:
			root.leftChild = treeNode(newNode)
		else:
			tmpNode = treeNode(newNode)
			tmpNode.leftChild = root.leftChild
			root.leftChild = tmpNode

		return root

	def insertRight(self, root, newNode):
		if root.rightChild is None:
			root.rightChild = treeNode(newNode)
		else:
			tmpNode = treeNode(newNode)
			tmpNode.rightChild = root.rightChild
			root.rightChild = tmpNode

		return root

	def isEmpty(self):
		return self.key is None

	def setRootValue(self, obj):
		self.key = obj

	def getRootValue(self):
		return self.key

	def getLeftChild(self):
		return self.leftChild

	def getRightChild(self):
		return self.rightChild

	def traversal(self):   # 遍历二叉树节点迭代器
		pass

	def createBinaryTreeInPreorderWithArray(self, arr):  # 创建二叉树，遵循前序遍历方式输入,solve array

		if len(arr) < 1:
			return None


		pass



	# 1 creat a tree with insert method
def createTreeByMethod():

	myTree = binaryTree()
	myTree.setRootValue('a')
	print (myTree.getRootValue())
	myTree.insertLeft('b')
	myTree.insertRight('c')
	myTree.getLeftChild().insertRight('d')
	myTree.getRightChild().insertLeft('e')
	myTree.getRightChild().insertRight('f')
	myTree.getRightChild().getRightChild().getRootValue

	print(myTree.getLeftChild())
	print(myTree.getLeftChild().getRootValue())

	print(myTree.getRightChild())
	print(myTree.getRightChild().getRootValue())

	myTree.getLeftChild().setRootValue('hello')
	print (myTree.getLeftChild().getRootValue())

	# 2.create a tree with string in preoder
def createTreeByList():
	global myTree

	treeElementList = '124#8##5##369###7##'
	# myTree = myTree.createTreeByListWithRecursion(treeElementList)
	# print (myTree)

	myTree = myTree.createTreeByListWithStack(treeElementList)
	print (myTree)

	# 3.create a tree by input
def createTreeByInput():

	myTree.createTreeByInput(myTree)

if __name__ == '__main__':
	myTree = binaryTree()
	createTreeByList()