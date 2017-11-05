# -*- coding: utf-8 -*-
# @Time    : 2017-11-2 9:13
# @Author  : zhangqi
# @File    : Class_Graph.py
# @Software: PyCharm Community Edition

import sys
import os


class Vertex:
	def __init__(self, num):
		self.id = num
		self.connectedTo = {}
		self.color = 'white'
		self.dist = sys.maxsize
		self.pred = None
		self.disc = 0
		self.fin = 0

	# def __lt__(self,o):
	#     return self.id < o.id

	def addNeighbor(self, nbr, weight=0):
		self.connectedTo[nbr] = weight

	def setColor(self, color):
		self.color = color

	def setDistance(self, d):
		self.dist = d

	def setPred(self, p):
		self.pred = p

	def setDiscovery(self, dtime):
		self.disc = dtime

	def setFinish(self, ftime):
		self.fin = ftime

	def getFinish(self):
		return self.fin

	def getDiscovery(self):
		return self.disc

	def getPred(self):
		return self.pred

	def getDistance(self):
		return self.dist

	def getColor(self):
		return self.color

	def getConnections(self):
		return self.connectedTo.keys()

	def getWeight(self, nbr):
		return self.connectedTo[nbr]

	def __str__(self):
		return str(self.id) + ":color " + self.color + ":disc " + str(self.disc) + ":fin " + str(
			self.fin) + ":dist " + str(self.dist) + ":pred \n\t[" + str(self.pred) + "]\n"

	def getId(self):
		return self.id


class Vertex1:
	def __init__(self, key):
		self.id = key
		self.connectTo = {}
		
	def addNeighbor(self, nbr, weight=0):
		self.connectTo[nbr] = weight
		
	def __str__(self):
		return self.key + 'connect to ' + str([v.id for v in self.connectTo])
	
	def getConnections(self):
		# return the keys of a dictionary
		return self.connectTo.keys()
	
	def getId(self):
		return self.id
	
	def getWeight(self,nbr):
		return self.connectTo[nbr]

	
class Graph:
	def __init__(self):
+
		
	def addVertex(self, key):
		newVertex = Vertex(key)
		self.vertexList[key] = newVertex
		self.numVertices += 1
		return newVertex

	def getVertex(self, n):
		if n in self.vertexList:
			return self.vertexList[n]
		else:
			return None

	def __contains__(self, n):
		return n in self.vertexList
	
	def addEdge(self, fromV , toV, cost=0):
		if fromV not in self.vertexList:
			nv = self.addVertex(fromV)
		if toV not in self.vertexList:
			nv = self.addVertex(toV)

		if (fromV, toV) not in self.edgesList:
			self.edgesList[(fromV, toV)] = cost

		self.vertexList[fromV].addNeighbor(self.vertexList[toV], cost)
		
	def getVertices(self):
		return self.vertexList
	
	def __iter__(self):
		return iter(self.vertexList.values())
	
	def verticesNumber(self):
		return self.numVertices
	
	def edgesNumber(self):
		pass
	
	def isEmpty(self):
		return self.numVertices == 0


if __name__ == '__main__':
	g = Graph()
	for i in range(6):
		g.addVertex(i)
	
	g.addEdge(0, 1, 5)
	g.addEdge(0, 5, 2)
	g.addEdge(1, 2, 4)
	g.addEdge(2, 3, 9)
	g.addEdge(3, 4, 7)
	g.addEdge(3, 5, 3)
	g.addEdge(4, 0, 1)
	g.addEdge(5, 4, 8)
	g.addEdge(5, 2, 1)

	for v in g:
		for w in v.getConnections():
			print("( %s , %s )" % (v.getId(), w.getId()))  # v.connectTo.keys()[0].id to check id