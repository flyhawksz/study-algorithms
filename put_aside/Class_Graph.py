# -*- coding: utf-8 -*-
# @Time    : 2017-11-2 9:13
# @Author  : zhangqi
# @File    : Class_Graph.py
# @Software: PyCharm Community Edition

import sys
import os
import matplotlib.pyplot as plt
import networkx as nx

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
		self.vertices_list = {}
		self.edges_list = {}
		self.num_vertices = 0
		
	def add_vertex(self, key):
		newVertex = Vertex(key)
		self.vertices_list[key] = newVertex
		self.num_vertices += 1
		return newVertex

	def get_vertex(self, n):
		if n in self.vertices_list:
			return self.vertices_list[n]
		else:
			return None

	def __contains__(self, n):
		return n in self.vertices_list
	
	def add_edge(self, fromV , toV, cost=0):
		if fromV not in self.vertices_list:
			nv = self.add_vertex(fromV)
		if toV not in self.vertices_list:
			nv = self.add_vertex(toV)

		if (fromV, toV) not in self.edges_list:
			self.edges_list[(fromV, toV)] = cost

		self.vertices_list[fromV].addNeighbor(self.vertices_list[toV], cost)
		
	def get_vertices(self):
		return self.vertices_list
	
	def __iter__(self):
		return iter(self.vertices_list.values())
	
	def vertices_number(self):
		return self.num_vertices
	
	def edgesNumber(self):
		pass
	
	def is_nmpty(self):
		return self.num_vertices == 0

	def draw_undirected_graph(self):
		G = nx.Graph()  # 建立一个空的无向图G
		for node in self.vertices:
			G.add_node(str(node))
		for edge in self.edges:
			G.add_edge(str(edge[0]), str(edge[1]))

		print("nodes:", G.nodes())  # 输出全部的节点： [1, 2, 3]
		print("edges:", G.edges())  # 输出全部的边：[(2, 3)]
		print("number of edges:", G.number_of_edges())  # 输出边的数量：1
		nx.draw(G, with_labels=True)
		plt.savefig("undirected_graph.png")
		plt.show()

	def draw_directed_graph(self):
		G = nx.DiGraph()  # 建立一个空的无向图G
		for node in self.vertices_list:
			G.add_node(str(node))
		# for edge in my_graph.edges:
		# G.add_edge(str(edge[0]), str(edge[1]))
		G.add_weighted_edges_from(self.edges_array)

		print("nodes:", G.nodes())  # 输出全部的节点： [1, 2, 3]
		print("edges:", G.edges())  # 输出全部的边：[(2, 3)]
		print("number of edges:", G.number_of_edges())  # 输出边的数量：1
		nx.draw(G, with_labels=True)
		plt.savefig("directed_graph.png")
		plt.show()


if __name__ == '__main__':
	g = Graph()
	for i in range(6):
		g.add_vertex(i)
	
	g.add_edge(0, 1, 5)
	g.add_edge(0, 5, 2)
	g.add_edge(1, 2, 4)
	g.add_edge(2, 3, 9)
	g.add_edge(3, 4, 7)
	g.add_edge(3, 5, 3)
	g.add_edge(4, 0, 1)
	g.add_edge(5, 4, 8)
	g.add_edge(5, 2, 1)

	g.draw_directed_graph()
	
	for v in g:
		for w in v.getConnections():
			print("( %s , %s )" % (v.getId(), w.getId()))  # v.connectTo.keys()[0].id to check id