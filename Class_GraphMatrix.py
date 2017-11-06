#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/5 17:38
# @Author  : zhangqi
# @Site    : 
# @File    : Class_GraphMatrix.py
# @Software: PyCharm Community Edition

import random
import matplotlib.pyplot as plt
import networkx as nx
from networkx.classes.graph import Graph


class Graph_Matrix:

	def __init__(self, vertices=[], matrix=[]):
		"""
		
		:param vertices:a dict with vertex id and index of matrix , such as {vertex:index}
		:param matrix: a matrix
		"""
		self.matrix = matrix
		self.edges = {}
		if len(matrix) > 0:
			if len(vertices) != len(matrix):
				raise IndexError
			self.edges = self.getAllEdges()
			
		self.numEdges = len(matrix)
		self.vertices = vertices

	def isOutRange(self, x):
		try:
			if x >= self.numVertices or x <= 0:
				raise IndexError
		except IndexError:
			print("节点下标出界")

	def isEmpty(self):
		if self.numVertices == 0:
			self.numVertices = len(self.matrix)
		return self.numVertices == 0

	def addVertex(self, key):
		if key not in self.vertexList:
			self.vertexList[key] = len(self.vertexList) + 1
			
		# add a vertex mean add a row and a column
		# add a column for every row
		for i in range(self.getVerticesNumbers()):
			self.matrix[i].append(0)

		self.numVertices += 1

		nRow = [0] * self.numVertices
		self.matrix.append(nRow)

	def getVertex(self, key):
		pass

	def addEdge(self, tailV, headV, cost=0):
		if self.vertexList.index(tailV) >= 0:
			self.addVertex(tailV)
		# if fromV not in self.vertexList:
		# 	self.addVertex(fromV)
		if self.vertexList.index(headV) >= 0:
			self.addVertex(headV)
		# if toV not in self.vertexList:
		# 	self.addVertex(toV)
		
		# for directory matrix
		self.matrix[self.vertexList.index(tailV)][self.vertexList.index(headV)] = cost
		# for non-directory matrix
		# self.matrix[self.vertexList.index(fromV)][self.vertexList.index(toV)] = \
		# 	self.matrix[self.vertexList.index(toV)][self.vertexList.index(fromV)] = cost
	
		self.edgesList[(tailV, headV)] = cost

	def getEdges(self, V):
		pass

	def getVerticesNumbers(self):
		if self.numVertices == 0:
			self.numVertices = len(self.map)
		return self.numVertices

	def getAllVertices(self):
		return self.vertexList

	def getAllEdges(self):
		for i in range(len(self.matrix)):
			for j in range(len(self.matrix)):
				if 0 < self.matrix[i][j] < float('inf'):
					self.edgesList[self.vertexList[i], self.vertexList[j]] = self.matrix[i][j]
					
		return self.edgesList




def createList():
	# 生成100个随机0,1之间的浮点数序列l
	x = [random.random() for i in range(100)]
	return x


def createList2():
	x = []
	for i in range(100):
		x.append(random.randint(0, 1))
	return x


def createList3():
	n = input('please input n of the matrix')
	x = []
	for i in range(n):
		x.append(1 if random.randint(0, 1) == 1 else 'inf')
	return x


def createMatrix():

	a, b, c, d, e, f, g, h = range(8)
	
	N = [[0, 1, 1, 1, 1, 1, 0, 0],  # a
		 [0, 0, 1, 0, 1, 0, 0, 0],  # b
		 [0, 0, 0, 1, 0, 0, 0, 0],  # c
		 [0, 0, 0, 0, 1, 0, 0, 0],  # d
		 [0, 0, 0, 0, 0, 1, 0, 0],  # e
		 [0, 0, 1, 0, 0, 0, 1, 1],  # f
		 [0, 0, 0, 0, 0, 1, 0, 1],  # g
		 [0, 0, 0, 0, 0, 1, 1, 0]]  # h

	# N[a][b]
	# 1
	# sum(N[f]))
	

def createMatrix2():
	a, b, c, d, e, f, g, h = range(8)
	inf = float('inf')
	w = N = [[0, 2, 1, 3, 9, 4, inf, inf],  # a
			 [inf, 0, 4, inf, 3, inf, inf, inf],  # b
			 [inf, inf, 0, 8, inf, inf, inf, inf],  # c
			 [inf, inf, inf, 0, 7, inf, inf, inf],  # d
			 [inf, inf, inf, inf, 0, 5, inf, inf],  # e
			 [inf, inf, 2, inf, inf, 0, 2, 2],  # f
			 [inf, inf, inf, inf, inf, 1, 0, 6],  # g
			 [inf, inf, inf, inf, inf, 9, 8, 0]]  # h

		# w[a][b]
		# 2
		# w[c][e]<inf
		# False
		# sum(1 for w in w[a] if w<inf)-1
	
	
def createMatrix3():
	vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
	edge_list = [('A', 'F', 9), ('A', 'B', 10), ('A', 'G', 15), ('B', 'F', 2),
	             ('G', 'F', 3), ('G', 'E', 12), ('G', 'C', 10), ('C', 'E', 1),
	             ('E', 'D', 7)]
	
	


if __name__ == '__main__':
	print (createList())
	print ('-' * 80)
	print (createList3())



	
	
