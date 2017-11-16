#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/16 0:25
# @Author  : flyhawk
# @Site    : 
# @File    : question_shortest_path_graph_adj_matrix.py
# @Software: PyCharm Community Edition

from Class_GraphMatrix import GraphMatrix
from Class_Queue import Queue


def create_undirected_matrix(my_graph):
	nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

	matrix = [[0, 1, 1, 1, 1, 1, 0, 0],  # a
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
	my_graph = GraphMatrix(nodes, matrix)
	print(my_graph)

	# my_graph.DepthFirstSearch()

	# draw_undircted_graph(my_graph)

	return my_graph


def create_directed_matrix(my_graph):
	nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
	inf = float('inf')
	matrix = [[0, 2, 1, 3, 9, 4, inf, inf],  # a
			  [inf, 0, 4, inf, 3, inf, inf, inf],  # b
			  [inf, inf, 0, 8, inf, inf, inf, inf],  # c
			  [inf, inf, inf, 0, 7, inf, inf, inf],  # d
			  [inf, inf, inf, inf, 0, 5, inf, inf],  # e
			  [inf, inf, 2, inf, inf, 0, 2, 2],  # f
			  [inf, inf, inf, inf, inf, 1, 0, 6],  # g
			  [inf, inf, inf, inf, inf, 9, 8, 0]]  # h

	my_graph = GraphMatrix(nodes, matrix)
	print(my_graph)
	return my_graph


def create_directed_graph_from_edges(my_graph):
	nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
	edge_list = [('A', 'F', 9), ('A', 'B', 10), ('A', 'G', 15), ('B', 'F', 2),
				 ('G', 'F', 3), ('G', 'E', 12), ('G', 'C', 10), ('C', 'E', 1),
				 ('E', 'D', 7)]

	my_graph = GraphMatrix(nodes)
	my_graph.add_edges_from_list(edge_list)
	print(my_graph)

	# my_graph.DepthFirstSearch()
	#
	# draw_directed_graph(my_graph)

	return my_graph


def bfs_queue(graph, start_v, end_v):
	def to_do_vertex(graph, vertex_index):
		visited_order.append(graph.vertices[vertex_index])
		print('visited vertex: %s' % graph.vertices[vertex_index])

	my_queue = Queue()
	# the distance from start vertex to current vertex
	distance = [0] * graph.num_vertices
	# the previous vertex that come to current vertex
	previous_vertex = [None] * graph.num_vertices

	current_vertex_index = graph.vertices.index(start_v)
	# set the start vertex distance as 0
	distance[current_vertex_index] = 0
	# marked with visited
	visited[current_vertex_index] = True
	# deal with the vertex
	to_do_vertex(graph, current_vertex_index)
	# push stack
	my_queue.enqueue(current_vertex_index)

	while not my_queue.isempty():
		# pop the first element as current vertex
		current_vertex_index = my_queue.dequeue()
		# find all the adjacent vertices
		for i in range(graph.num_vertices):
			if (0 < graph.matrix[current_vertex_index][i] < inf) and (visited[i] is False):
				# calculate the distance
				distance[i] = distance[current_vertex_index] + 1
				# mark the previous
				previous_vertex[i] = current_vertex_index
				# deal with the vertex
				to_do_vertex(graph, i)
				# mark the vertex
				visited[i] = True
				# check whether come to the end
				if graph.vertices[i] is end_v:
					print('find the path from %s to %s' % (start_v, end_v))
					return distance, previous_vertex, visited_order

				# enqueue the element
				my_queue.enqueue(i)

	print('can not find the path from %s to %s' % (start_v, end_v))
	return False


if __name__ == '__main__':
	_graph = GraphMatrix()
	# g = create_undirected_matrix(_graph)
	g = create_directed_matrix(_graph)
	# g = create_directed_graph_from_edges(_graph)
	
	# created_graph.draw_directed_graph()

	start_v = 'a'
	end_v = 'h'

	inf = float('inf')
	visited = [False] * g.num_vertices
	visited_order = []

	# shortest path for graph adjacency matrix
	print ('-'*100)
	print ('traverse graph')
	print ('-'*100)
	dist, pre_v, visited = bfs_queue(g, start_v, end_v)
	print ('the distance from %s to %s is %s: ' % (start_v, end_v, dist[g.vertices.index(end_v)]))

	_v = g.vertices.index(end_v)
	print(g.vertices[_v])
	while not pre_v[_v] is None:
		# if pre_v[_v]:
		v = pre_v[_v]
		print (g.vertices[v])
		_v = v
