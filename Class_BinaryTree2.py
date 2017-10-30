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

	def createTreeByListWithRecursion(self, preOrderList):
		"""
		根据前序列表重建二叉树
		:param preOrder: 输入前序列表
		:return: 二叉树
		"""
		preOrder = preOrderList
		if preOrder is None or len(preOrder) <= 0:
			return None
		currentItem = preOrder.pop(0)  # 模拟C语言指针移动
		if currentItem is '#':
			root = None
		else:
			root = treeNode(currentItem)
			root.leftChild = self.createTreeByListWithRecursion(preOrder)
			root.rightChild = self.createTreeByListWithRecursion(preOrder)
		return root

	def createTreeByListWithStack(self, preOrderList):
		"""
		根据前序列表和中序列表,重建二叉树
		:param preOrder: 输入前序列表
		:return: 二叉树
		"""
		preOrder = preOrderList
		pStack = SStack()

		# check
		if preOrder is None or len(preOrder) <= 0 or preOrder[0] is '#':
			return None

		# get the root
		tmpItem = preOrder.pop(0)
		root = treeNode(tmpItem)

		# push root
		pStack.push(root)
		currentRoot = root

		while preOrder:
			# get another item
			tmpItem = preOrder.pop(0)
			# has child
			if tmpItem is not '#':
				# does not has left child, insert one
				if currentRoot.leftChild is None:
					currentRoot = self.insertLeft(currentRoot, tmpItem)
					pStack.push(currentRoot.leftChild)
					currentRoot = currentRoot.leftChild

				# otherwise insert right child
				elif currentRoot.rightChild is None:
					currentRoot = self.insertRight(currentRoot, tmpItem)
					pStack.push(currentRoot.rightChild)
					currentRoot = currentRoot.rightChild
			# one child is null
			else:
				# if has no left child
				if currentRoot.leftChild is None:
					currentRoot.leftChild = None

					# get another item fill right child
					tmpItem = preOrder.pop(0)
					# has right child
					if tmpItem is not '#':
						currentRoot = self.insertRight(currentRoot, tmpItem)
						pStack.push(currentRoot.rightChild)
						currentRoot = currentRoot.rightChild
					# right child is null
					else:
						currentRoot.rightChild = None
						# pop itself
						parent = pStack.pop()
						# pos parent
						if not pStack.is_empty():
							parent = pStack.pop()
						# parent become current root
						currentRoot = parent

						# return from right child, so the parent has right child, go to parent's parent
						if currentRoot.rightChild is not None:
							if not pStack.is_empty():
								parent = pStack.pop()
								currentRoot = parent

				# there is a leftchild ,fill right child with null and return to parent
				else:
					currentRoot.rightChild = None
					# pop itself
					parent = pStack.pop()
					if not pStack.is_empty():
						parent = pStack.pop()
					currentRoot = parent

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

def printBTree(bt, depth):
	'''''
	递归打印这棵二叉树，#号表示该节点为NULL
	'''
	ch = bt.key if bt else '#'
	if depth > 0:
		print '%s%s%s' % ((depth - 1) * '  ', '--', ch)
	else:
		print ch
	if not bt:
		return
	printBTree(bt.leftChild, depth + 1)
	printBTree(bt.rightChild, depth + 1)


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
def createTreeByListWithRecursion():
	global myTree
	global treeElementList

	myTree = myTree.createTreeByListWithRecursion(list(treeElementList))
	printBTree(myTree, 0)

def createTreeByListWithStack():
	global myTree
	global treeElementList

	myTree = myTree.createTreeByListWithStack(list(treeElementList))
	printBTree(myTree, 0)

	# 3.create a tree by input
def createTreeByInput():
	global myTree
	myTree = myTree.createTreeByInput(myTree)
	printBTree(myTree, 0)

if __name__ == '__main__':
	myTree = binaryTree()
	treeElementList = '124#8##5##369###7##'
	createTreeByListWithStack()
	# createTreeByListWithRecursion()
	# createTreeByInput()