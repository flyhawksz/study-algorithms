#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/12 23:58
# @Author  : flyhawk
# @Site    : 
# @File    : question_create_traverse_graph_adjacency_list.py
# @Software: PyCharm Community Edition


from class_graph_adjacency_list import GraphAdjacencyList
from Class_Queue import Queue


def traversal_dfs_recursion(graph):
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


	def dfs_recursion(graph):





	def to_do_vertex(graph, i):
		print('vertex: %s' % (graph.vertices[i]))

	def to_do_edge(graph, w, k):
		print('edge tail: %s, edge head: %s, weight: %s' % (graph.vertices[w], graph.vertices[k], str(graph.matrix[w][k])))



	if start_v not in graph.vertices:
		print('%s is not in this graph' % start_v)
		return False

	if end_v not in graph.vertices:
		print('%s is not in this graph' % end_v)
		return False

	inf = float('inf')
	visited = [False] * graph.num_vertices

	# try dfs by recursion method
	dfs_recursion(graph, start_v, end_v)

	print ('-'*100)

	# try dfs by stack method
	visited = [False] * graph.num_vertices
	my_stack = SStack()
	dfs_stack(graph, start_v, end_v, my_stack)




if __name__ == '__main__':
	g = GraphAdjacencyList()

	g = buildGraph('e:\\fourletterwords2.txt')
	# bfs(g, g.getVertex('BOSS'))
	# dfs(g, g.getVertex('BOSS'))
	# traverse(g.getVertex('SAGE'))

	# g.addEdge(0, 1, 5)
	# g.addEdge(0, 5, 2)
	# g.addEdge(1, 2, 4)
	# g.addEdge(2, 3, 9)
	# g.addEdge(3, 4, 7)
	# g.addEdge(3, 5, 3)
	# g.addEdge(4, 0, 1)
	# g.addEdge(5, 4, 8)
	# g.addEdge(5, 2, 1)

	draw2(g)
	# bfs(g, g.getVertex(2))

	# traverse(g.getVertex(1))
	# print('-'*80)
	# dfs(g, g.getVertex(2))
	# traverse(g.getVertex(1))
