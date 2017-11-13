#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/12 23:58
# @Author  : flyhawk
# @Site    : 
# @File    : question_create_traverse_graph_adjacency_list.py
# @Software: PyCharm Community Edition


from class_graph_adjacency_list import GraphAdjacencyList
from Class_Queue import Queue


def deep_first_search(graph, start_v=None, end_v=None):

	def to_do_vertex(graph, i):
		print('vertex: %s' % (graph.vertices[i]))

	def to_do_edge(graph, w, k):
		print('edge tail: %s, edge head: %s, weight: %s' % (graph.vertices[w], graph.vertices[k], str(graph.matrix[w][k])))

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
		print('current vertex: %s' % start_v)
		visited[start_v] = True
		visited_order.append(start_v)
		for v in graph.get_vertex(start_v).neighbors:
			if end_v and (v is end_v):
				print('find the path from %s to %s' % (start_v, end_v))
				return visited_order
			else:
				dfs_recursion(graph, v, end_v)

	visited = [False] * graph.num_vertices
	visited_order = []

	if start_v and end_v:
		if start_v not in graph.vertices:
			print('%s is not in this graph' % start_v)
			return False

		if end_v not in graph.vertices:
			print('%s is not in this graph' % end_v)
			return False

	elif start_v:
		if start_v not in graph.vertices:
			print('%s is not in this graph' % start_v)
			return False
		dfs_recursion(graph, start_v)
	else:
		for vertex in graph.vertices_list:
			if visited[vertex] is False:
				dfs_recursion(graph, vertex)

	print visited_order
	return visited_order


	# print ('-'*100)
	#
	# # try dfs by stack method
	# visited = [False] * graph.num_vertices
	# my_stack = SStack()
	# dfs_stack(graph, start_v, end_v, my_stack)


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
	deep_first_search(g, 2)

	# traverse(g.getVertex(1))
	# print('-'*80)
	# dfs(g, g.getVertex(2))
	# traverse(g.getVertex(1))
