#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/12 16:52
# @Author  : zhangqi
# @Site    : 
# @File    : Question_Create_Traverse_Binary_Tree.py
# @Software: PyCharm Community Edition

from Class_BinaryTree2 import binaryTree
from Class_SStack import SStack


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
def createTreeByListWithRecursion(myTree, treeElements):
	myTree = myTree.createTreeByListWithRecursion(list(treeElements))
	printBTree(myTree, 0)
	return myTree


def createTreeByListWithStack(myTree, treeElements):
	myTree = myTree.createTreeByListWithStack(list(treeElements))
	printBTree(myTree, 0)
	return myTree


# 3.create a tree by input
def createTreeByInput(myTree):
	myTree = myTree.createTreeByInput(myTree)
	printBTree(myTree, 0)
	return myTree


# 	to do something with data
def todo(root):
	if root.key is not None:
		print root.key


# pre-order traversal with recursion
def preorderTraversalWithRecursion(root):
	if root is not None:
		todo(root)
		preorderTraversalWithRecursion(root.leftChild)
		preorderTraversalWithRecursion(root.rightChild)


# in-order traversal with recursion
def inorderTraversalWithRecursion(root):
	if root is not None:
		inorderTraversalWithRecursion(root.leftChild)
		todo(root)
		inorderTraversalWithRecursion(root.rightChild)


# post-order traversal with recursion
def postorderTraversalWithRecursion(root):
	if root is not None:
		postorderTraversalWithRecursion(root.leftChild)
		postorderTraversalWithRecursion(root.rightChild)
		todo(root)


# pre-order traversal with stack
def preorderTraversalWithStack(root):
	if root is None:
		return

	myStack = []
	while root or myStack:
		# check left child
		while root:
			todo(root)
			myStack.append(root)
			root = root.leftChild
		# finish check left child. left child is None, loop over

		# get parent
		root = myStack.pop()
		# check right child
		root = root.rightChild


# another methode
def preorderTraversalWithStack2(root):
	myStack = SStack()
	while root or myStack:
		while root:  # go down ro the left
			todo(root)  # deal with data
			myStack.push(root.rightChild)  # push right child
			root = root.leftChild
		root = myStack.pop()  # end of left branch , go back deal with right branch


# in-order traversal with stack
def inorderTraversalWithStack(root):
	if root is None:
		return

	myStack = []
	while root or myStack:
		# check left sub-tree get the last child
		while root:
			myStack.append(root)
			root = root.leftChild
		# finish check left child. left child is None, loop over


		# the last child is None , get parent
		root = myStack.pop()
		todo(root)
		# check right child
		root = root.rightChild


# post-order traversal with stack
def postorderTraversalWithStack(root):
	"""利用堆栈实现树的后序遍历"""
	if root is None:
		return
	myStack1 = []
	myStack2 = []
	node = root
	myStack1.append(node)
	while myStack1:  # 这个while循环的功能是找出后序遍历的逆序，存在myStack2里面
		node = myStack1.pop()
		if node.leftChild:
			myStack1.append(node.leftChild)
		if node.rightChild:
			myStack1.append(node.rightChild)
		myStack2.append(node)
	while myStack2:  # 将myStack2中的元素出栈，即为后序遍历次序
		todo(myStack2.pop())


# level-order traversal with queue
def levelorderTraversalWithQueue(root):
	if root is None:
		return
	myQueue = []
	node = root
	myQueue.append(node)
	while myQueue:
		node = myQueue.pop(0)
		todo(node)
		if node.leftChild is not None:
			myQueue.append(node.leftChild)
		if node.rightChild is not None:
			myQueue.append(node.rightChild)


if __name__ == '__main__':
	myTree = binaryTree()
	treeElements = '124#8##5##369###7##'
	# myTree = createTreeByListWithStack(myTree, treeElements )

	myTree = createTreeByListWithRecursion(myTree, treeElements)

	# myTree = createTreeByInput(myTree)
	print ('*' * 80)
	print ('pre-order Traversal')
	preorderTraversalWithRecursion(myTree)
	print ('-' * 80)
	preorderTraversalWithStack(myTree)

	print ('*' * 80)
	print ('in-order Traversal')
	print ('*' * 80)
	inorderTraversalWithRecursion(myTree)
	print ('-' * 80)
	inorderTraversalWithStack(myTree)

	print ('*' * 80)
	print ('pos-order Traversal')
	print ('*' * 80)
	postorderTraversalWithRecursion(myTree)
	print ('-' * 80)
	postorderTraversalWithStack(myTree)

	print ('*' * 80)
	print ('level-order Traversal')
	print ('*' * 80)
	levelorderTraversalWithQueue(myTree)
	print ('-' * 80)
