#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/12 20:14
# @Author  : flyhawk
# @Site    : 
# @File    : class_graph_adjacency_list.py
# @Software: PyCharm Community Edition

import matplotlib.pyplot as plt
import networkx as nx


class Vertex:
	def __init__(self, key):
		self.id = key
		self.neighbors = {}
		self.visited = False

		# use for shortest path
		self.distance = float('inf')
		self.predecessor = None

	def add_neighbor(self, nbr, weight=0):
		self.neighbors[nbr] = weight

	# def __str__(self):
	# 	return self.id + 'connect to ' + str([v.id for v in self.neighbors])

	def get_neighbors(self):
		# return the keys of a dictionary
		return self.neighbors.keys()

	def get_Id(self):
		return self.id

	def get_weight(self, nbr):
		return self.neighbors[nbr]

	# use for shortest path
	def set_distance(self, dist):
		self.distance = dist

	def get_distance(self):
		return self.distance

	def set_predecessor(self, pred):
		self.predecessor = pred

	def get_predecessor(self):
		return self.predecessor


	# def __repr__(self):
	# 	return str(self.neighbors)


class GraphAdjacencyList:
	def __init__(self):
		self.vertices_list = {}  # dict vertex object
		self.vertices = []  # <type 'list'>: ['A', 'B', 'E', 'D', 'F', 'C']
		self.edges_list = {}  # dict of tuple {(0, 1): 5, (1, 2): 4,}
		self.edges_array = []  # <type 'list'>: [[0, 1, 5], [0, 5, 2]] (tail, head, weight) for networkX to draw graph
		self.edges_array_for_sort = []  # (weight, tail, head) for sort to get shortest edge
		self.num_vertices = 0
		self.num_edges = 0

	def add_vertex(self, key):
		new_vertex = Vertex(key)
		self.vertices.append(key)
		self.vertices_list[key] = new_vertex
		self.num_vertices += 1
		return new_vertex

	def get_vertex(self, n):
		if n in self.vertices_list:
			return self.vertices_list[n]
		else:
			return None

	def __contains__(self, n):
		return n in self.vertices_list

	def add_edge(self, tail, head, cost=0):
		if tail not in self.vertices_list:
			nv = self.add_vertex(tail)
		if head not in self.vertices_list:
			nv = self.add_vertex(head)

		if (tail, head) not in self.edges_list:
			self.edges_list[(tail, head)] = cost
			self.edges_array.append([tail, head, cost])
			self.edges_array_for_sort.append([cost, tail, head])

		self.vertices_list[tail].add_neighbor(self.vertices_list[head], cost)
		
		# build edges array for networkX draw graph
		# self.edges_array.append((tail, head, cost))
		self.num_edges = len(self.edges_list)

	def get_vertices(self):
		vertices = [v for v in self.vertices_list.keys()]
		return vertices
		
	def get_vertices_list(self):
		return self.vertices_list

	def __iter__(self):
		return iter(self.vertices_list.values())

	def vertices_number(self):
		return self.num_vertices

	def edges_number(self):
		pass

	def is_empty(self):
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
		for _edge, _weight in self.edges_list.items():
			G.add_edge(str(_edge[0]), str(_edge[1]), weight=_weight)

		# G.add_weighted_edges_from(self.edges_array)

		print("nodes:", G.nodes())  # 输出全部的节点： [1, 2, 3]
		print("edges:", G.edges())  # 输出全部的边：[(2, 3)]
		print("number of edges:", G.number_of_edges())  # 输出边的数量：1
		nx.draw(G, with_labels=True)
		plt.savefig("directed_graph.png")
		plt.show()

	def reset_all_vertices_unvisited(self):
		for vertex in self.vertices_list:
			self.vertices_list[vertex].visited = False
	
	
if __name__ == '__main__':
	g = GraphAdjacencyList()
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
	
	# _v=g.get_vertex(2)
	# print (_v)
	
	for v in g:
		for w in v.get_neighbors():
			print("( %s , %s )" % (v.get_Id(), w.get_Id()))  # v.connectTo.keys()[0].id to check id


class GraphAdjacencyList2:
	def __init__(self):
		self.vertices = {}

	def add_vertex(self, vertex):
		if isinstance(vertex, Vertex):
			self.vertices[vertex.name] = vertex.neighbors

	def add_vertices(self, vertices):
		for vertex in vertices:
			if isinstance(vertex, Vertex):
				self.vertices[vertex.name] = vertex.neighbors

	def add_edge(self, vertex_from, vertex_to):
		if isinstance(vertex_from, Vertex) and isinstance(vertex_to, Vertex):
			vertex_from.add_neighbor(vertex_to)
			if isinstance(vertex_from, Vertex) and isinstance(vertex_to, Vertex):
				self.vertices[vertex_from.name] = vertex_from.neighbors
				self.vertices[vertex_to.name] = vertex_to.neighbors

	def add_edges(self, edges):
		for edge in edges:
			self.add_edge(edge[0], edge[1])

	def adjacency_list(self):
		if len(self.vertices) >= 1:
			return [str(key) + ":" + str(self.vertices[key]) for key in self.vertices.keys()]
		else:
			return dict()

	def adjacency_matrix(self):
		if len(self.vertices) >= 1:
			self.vertex_names = sorted(g.vertices.keys())
			self.vertex_indices = dict(zip(self.vertex_names, range(len(self.vertex_names))))
			import numpy as np
			self.adjacency_matrix = np.zeros(shape=(len(self.vertices), len(self.vertices)))
			for i in range(len(self.vertex_names)):
				for j in range(i, len(self.vertices)):
					for el in g.vertices[self.vertex_names[i]]:
						j = g.vertex_indices[el]
						self.adjacency_matrix[i, j] = 1
			return self.adjacency_matrix
		else:
			return dict()
