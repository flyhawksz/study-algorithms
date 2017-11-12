#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/12 20:14
# @Author  : flyhawk
# @Site    : 
# @File    : class_graph_adjacency_list.py
# @Software: PyCharm Community Edition


class Vertex:
	def __init__(self, key):
		self.id = key
		self.neighbors = {}

	def add_neighbor(self, nbr, weight=0):
		self.neighbors[nbr] = weight

	def __str__(self):
		return self.id + 'connect to ' + str([v.id for v in self.neighbors])

	def get_connections(self):
		# return the keys of a dictionary
		return self.neighbors.keys()

	def get_Id(self):
		return self.id

	def get_weight(self, nbr):
		return self.neighbors[nbr]

	def __repr__(self):
		return str(self.neighbors)


class GraphAdjacencyList:
	def __init__(self):
		self.vertices_list = {}
		self.edges_list = {}
		self.num_vertices = 0

	def add_vertex(self, key):
		new_vertex = Vertex(key)
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

	def add_edge(self, from_vertex, to_vertex, cost=0):
		if from_vertex not in self.vertices_list:
			nv = self.add_vertex(from_vertex)
		if to_vertex not in self.vertices_list:
			nv = self.add_vertex(to_vertex)

		if (from_vertex, to_vertex) not in self.edges_list:
			self.edges_list[(from_vertex, to_vertex)] = cost

		self.vertices_list[from_vertex].add_neighbor(self.vertices_list[to_vertex], cost)

	def get_vertices(self):
		return self.vertices_list

	def __iter__(self):
		return iter(self.vertices_list.values())

	def vertices_number(self):
		return self.num_vertices

	def edges_number(self):
		pass

	def is_empty(self):
		return self.num_vertices == 0


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

	for v in g:
		for w in v.get_connections():
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
