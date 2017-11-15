#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/12 23:58
# @Author  : flyhawk
# @Site    : 
# @File    : question_create_traverse_graph_adjacency_list.py
# @Software: PyCharm Community Edition


from __future__ import print_function
from class_graph_adjacency_list import GraphAdjacencyList
from Class_Queue import Queue
from Class_SStack import SStack


def deep_first_search(graph, start_v=None, end_v=None):

	def to_do_vertex(vertex):
		visited_order.append(vertex.id)
		print('visited vertex: %s' % vertex.id)

	def dfs_recursion(graph, start_v, end_v=None):
		"""
		姥姥的伪代码
		void  DFS( Graph G,  int V )
		{ /* 从第V个顶点出发递归地深度优先遍历图G */
		VertexType W;
			Visited[V] = TRUE;
			VisitFunc(V);      /* 访问第V个顶点 */
			for( W = FirstAdjV(G, V);  W;  W = NextAdjV (G, V, W) )
				if( !Visited[W] )
					DFS(G, W); /* 对V的尚未访问的邻接顶点W递归调用DFS */
		}
		:param g: a instance of graph
		:param start: a instance vertex, such as g.getVertex('FOOL')
		:return:
		"""
		# deal with the visited vertex
		to_do_vertex(start_v)
		# print('visited vertex: %s' % start_v.id)
		start_v.visited = True
		for v in start_v.neighbors:
			if not v.visited:
				dfs_recursion(graph, v, end_v)
		
	def dfs_search_recursion(graph, start_v, end_v):
		# deal with the visited vertex
		to_do_vertex(start_v)
		# print('visited vertex: %s' % start_v.id)
		start_v.visited = True
		for v in start_v.neighbors:
			if (v is end_v) and not v.visited:
				to_do_vertex(v)
				print ('find the path and arrive at: %s' % v.id)
				return
			elif not v.visited:
				dfs_search_recursion(graph, v, end_v)

	def dfs_search_stack(graph, start_v, end_v):
		def get_first_adjacent_vertex(_vertex):
			"""
			get current vertex first adjacent vertex
			:param graph:
			:param current_vertex_index:
			:return: if has return the index. otherwise return None
			"""
			for v in _vertex.neighbors:
				if not v.visited:
					return v
			return None

		my_stack = SStack()
		# deal with the visited vertex
		to_do_vertex(start_v)
		# print('visited vertex: %s' % start_v.id)
		start_v.visited = True
		my_stack.push(start_v)
		while not my_stack.is_empty():
			v = get_first_adjacent_vertex(my_stack.top())
			if v:
				v.visited = True
				to_do_vertex(v)
				if v is end_v:
					print('find the path and arrive at: %s' % v.id)
					return

				my_stack.push(v)

			else:
				my_stack.pop()

	visited_order = []

	if start_v and end_v:
		if start_v not in graph.vertices_list:
			print('%s is not in this graph' % start_v)
			return False

		if end_v not in graph.vertices_list:
			print('%s is not in this graph' % end_v)
			return False

		print ('*'*100)
		print ('dfs_search_recurse')
		print ('*'*100)
		dfs_search_recursion(graph, graph.get_vertex(start_v), graph.get_vertex(end_v))

		print ('*'*100)
		print ('dfs_search_stack')
		print ('*'*100)
		graph.reset_all_vertices_unvisited()
		visited_order = []
		dfs_search_stack(graph, graph.get_vertex(start_v), graph.get_vertex(end_v))
		
	elif start_v:
		if start_v not in graph.vertices_list:
			print('%s is not in this graph' % start_v)
			return False
		dfs_recursion(graph, graph.get_vertex(start_v))
	else:
		for vertex in graph.vertices_list:
			if not graph.get_vertex(vertex).visited:
				dfs_recursion(graph, graph.get_vertex(vertex))
	
	# print(visited_order)
	return visited_order


def breadth_first_search(graph, start_v=None, end_v=None):
	def to_do_vertex(vertex):
		visited_order.append(vertex.id)
		print('visited vertex: %s' % vertex.id)
	
	def bfs_queue(graph, start_v, end_v=None):
		my_queue = Queue()
		to_do_vertex(start_v)
		start_v.visited = True
		my_queue.enqueue(start_v)
		while not my_queue.isempty():
			current_vertex = my_queue.dequeue()
			for v in current_vertex.neighbors:
				if not v.visited:
					if v is end_v:
						to_do_vertex(v)
						print('find the path and arrive at: %s' % v.id)
						return
					else:
						to_do_vertex(v)
						v.visited = True
						my_queue.enqueue(v)
	
	visited_order = []
	
	if start_v and end_v:
		if start_v not in graph.vertices_list:
			print('%s is not in this graph' % start_v)
			return False

		if end_v not in graph.vertices_list:
			print('%s is not in this graph' % end_v)
			return False

		print ('*'*100)
		print ('dfs_search_queue')
		print ('*'*100)
		bfs_queue(graph, graph.get_vertex(start_v), graph.get_vertex(end_v))
		
	return visited_order


if __name__ == '__main__':
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

	g.draw_directed_graph()

	# traverse graph
	print ('-'*100)
	print ('traverse graph')
	print ('-'*100)
	print(deep_first_search(g))

	# traverse grapth with a start
	print ('-'*100)
	print ('traverse grapth with a start')
	print ('-'*100)
	g.reset_all_vertices_unvisited()
	print(deep_first_search(g, 4))

	# traverse grapth with a start
	print ('-'*100)
	print ('search grapth with start and end')
	print ('-'*100)
	g.reset_all_vertices_unvisited()
	print(deep_first_search(g, 4, 2))

	print ('+'*100)
	print ('search grapth with start and end')
	print ('+'*100)
	g.reset_all_vertices_unvisited()
	print(broad_first_search(g, 4, 2))
	
	# traverse(g.getVertex(1))
	# print('-'*80)
	# dfs(g, g.getVertex(2))
	# traverse(g.getVertex(1))
