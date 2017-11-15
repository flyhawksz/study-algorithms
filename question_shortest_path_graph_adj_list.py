#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/16 0:26
# @Author  : flyhawk
# @Site    : 
# @File    : question_shortest_path_graph_adj_list.py
# @Software: PyCharm Community Edition


from Class_GraphMatrix import GraphMatrix
from class_graph_adjacency_list import GraphAdjacencyList
from Class_Queue import Queue
from Class_SStack import SStack


# use bfs method
def shortest_path_unweighted_graph_adjacency_list(graph, start_v, end_v):

	def to_do_vertex(vertex):
		visited_order.append(vertex.id)
		print('visited vertex: %s' % vertex.id)

	# the distance from start vertex to current vertex
	distance = {}
	# the previous vertex that come to current vertex
	previous_vertex = {}
	distance[start_v.id] = 0

	my_queue = Queue()
	to_do_vertex(start_v)
	start_v.visited = True
	my_queue.enqueue(start_v)
	while not my_queue.isempty():
		current_vertex = my_queue.dequeue()
		for v in current_vertex.neighbors:
			if not v.visited:
				distance[v.id] = distance[current_vertex.id] + 1
				previous_vertex[v.id] = current_vertex
				to_do_vertex(v)
				if v is end_v:
					print('find the path and arrive at: %s, distance is %s' % (v.id, distance[v.id]))
					return (distance, previous_vertex, visited_order)
				else:
					v.visited = True
					my_queue.enqueue(v)


if __name__ == '__main__':
	visited_order = []

	g = GraphAdjacencyList()

	g.add_edge(0, 1, 5)
	g.add_edge(0, 5, 2)
	g.add_edge(1, 2, 4)
	g.add_edge(2, 3, 9)
	g.add_edge(3, 4, 7)
	g.add_edge(3, 5, 3)
	g.add_edge(4, 0, 1)
	g.add_edge(5, 4, 8)
	g.add_edge(5, 2, 1)

	# g.draw_directed_graph()

	start_v = 4
	end_v = 2

	# shortest path for graph adjacency list
	print ('-'*100)
	print ('traverse graph')
	print ('-'*100)
	dist, pre_v, visited = shortest_path_unweighted_graph_adjacency_list(g, g.get_vertex(start_v), g.get_vertex(end_v))
	print ('the distance from %s to %s is %s: ' % (start_v, end_v, dist[end_v]))

	_v = g.get_vertex(end_v)
	print(_v.id)
	while not pre_v[_v.id] is None:
		if pre_v[_v.id]:
			v = pre_v[_v.id]
			print (v.id)
			_v = v