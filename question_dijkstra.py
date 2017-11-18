#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/18 23:18
# @Author  : flyhawk
# @Site    : 
# @File    : question_dijkstra.py
# @Software: PyCharm Community Edition


import sys


class Vertex(object):
	def __init__(self, key):
		self.id = key
		self.adj = {}

	def addNeighbor(self, nbr, weight=0):
		self.adj[nbr] = weight

	def getNeighbors(self):
		return self.adj.keys()

	def getId(self):
		return self.id

	def getWeight(self, key):
		return self.adj[key]


class Graph(object):
	def __init__(self):
		self.vertexlist = {}
		self.size = 0

	def addVertex(self, key):
		vertex = Vertex(key)
		self.vertexlist[key] = vertex
		self.size += 1
		return vertex

	def getVertex(self, key):
		return self.vertexlist.get(key)

	def __contains__(self, key):
		if key in self.vertexlist:
			return True
		else:
			return False

	def addEdge(self, f, t, weight=0):
		if f not in self.vertexlist:
			self.addVertex(f)
		if t not in self.vertexlist:
			self.addVertex(t)
		self.vertexlist[f].addNeighbor(self.vertexlist[t], weight)

	def getVertices(self):
		return self.vertexlist.keys()

	def __iter__(self):
		return iter(self.vertexlist.values())


def Dijkstra(G, s):
	path = {}
	vertexlist = []
	for v in G:
		vertexlist.append(v)
		path[v] = sys.maxsize
	path[s] = 0
	queue = PriorityQueue(path)
	queue.buildHeap(vertexlist)
	while queue.size > 0:
		vertex = queue.delMin()
		for v in vertex.getNeighbors():
			newpath = path[vertex] + vertex.getWeight(v)
			if newpath < path[v]:
				path[v] = newpath
				queue.perUp(v)
	return path


class PriorityQueue(object):
	def __init__(self, path):
		self.path = path
		self.queue = []
		self.size = 0

	def buildHeap(self, alist):
		self.queue = alist
		self.size = len(alist)
		for i in xrange(self.size / 2 - 1, 0, -1):
			self._perDown(i)

	def delMin(self):
		self.queue[0], self.queue[-1] = self.queue[-1], self.queue[0]
		minvertex = self.queue.pop()
		self.size -= 1
		self._perDown(0)
		return minvertex

	def perUp(self, v):
		i = self.queue.index(v)
		self._perUp(i)

	def _perUp(self, i):
		if i > 0:
			if self.path[self.queue[i]] <= self.path[self.queue[(i - 1) / 2]]:
				self.queue[i], self.queue[(i - 1) / 2] = self.queue[(i - 1) / 2], self.queue[i]
				self._perUp((i - 1) / 2)

	def _perDown(self, i):
		left = 2 * i + 1
		right = 2 * i + 2
		little = i
		if left <= self.size - 1 and self.path[self.queue[left]] <= self.path[self.queue[i]]:
			little = left
		if right <= self.size - 1 and self.path[self.queue[right]] <= self.path[self.queue[little]]:
			little = right
		if little != i:
			self.queue[i], self.queue[little] = self.queue[little], self.queue[i]
			self._perDown(little)


if __name__ == '__main__':
	g = Graph()
	g.addEdge('u', 'x', 1)
	g.addEdge('u', 'v', 2)
	g.addEdge('u', 'w', 5)
	g.addEdge('x', 'v', 2)
	g.addEdge('x', 'y', 1)
	g.addEdge('x', 'w', 3)
	g.addEdge('v', 'w', 3)
	g.addEdge('y', 'w', 1)
	g.addEdge('y', 'z', 1)
	g.addEdge('w', 'z', 5)
	u = g.getVertex('u')
	path = Dijkstra(g, u)
	for v in path:
		print v.id, path[v]