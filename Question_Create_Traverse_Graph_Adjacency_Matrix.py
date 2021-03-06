#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/12 22:31
# @Author  : flyhawk
# @Site    : 
# @File    : Question_Create_Traverse_Graph_Adjacency_Matrix.py
# @Software: PyCharm Community Edition

import random
from Class_GraphMatrix import GraphMatrix
from Class_SStack import SStack
from Class_Queue import Queue


def createList():
	# 生成100个随机0,1之间的浮点数序列l
	x = [random.random() for i in range(100)]
	return x


def createList2():
	x = []
	for i in range(100):
		x.append(random.randint(0, 1))
	return x


def createList3():
	n = input('please input n of the matrix')
	x = []
	for i in range(n):
		x.append(1 if random.randint(0, 1) == 1 else 'inf')
	return x


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




# def dfs_visit(self, numCourses, prerequisites):
# 	"""
# 	traverse all the vertices, there are may some disconnected vertices, dfs can not visit
# 	so that need visit all of them, and call dfs
# 	:param self:
# 	:param numCourses:
# 	:param prerequisites:
# 	:return:
# 	"""
# 	graph = [[] for _ in range(num_)]
# 	visit = [0 for _ in range(numCourses)]
# 	for x, y in prerequisites:
# 		graph[x].append(y)
#
# 		def dfs(i):
# 			if visit[i] == -1:
# 				return False
# 			if visit[i] == 1:
# 				return True
# 			visit[i] = -1
# 			for j in graph[i]:
# 				if not dfs(j):
# 					return False
# 			visit[i] = 1
# 			return True
#
# 	for i in range(numCourses):
# 		if not dfs(i):
# 			return False
# 	return True


def to_do_vertex(self, i):
	print('vertex: %s' % (self.vertices[i]))


def to_do_edge(self, w, k):
	print('edge tail: %s, edge head: %s, weight: %s' % (self.vertices[w], self.vertices[k], str(self.matrix[w][k])))


def depth_first_traversal(graph):
	"""
	traverse all the vertices, there are may some disconnected vertices, dfs can not visit
	so that need visit all of them, and call dfs
	"""

	def DFS(i, queue):  # with queue

		queue.append(i)
		to_do_vertex(i)
		visited[i] = 1
		if len(queue) != 0:
			w = queue.pop()
			for k in range(graph.num_vertices):
				if graph.matrix[w][k] is 1 and visited[k] is 0:
					to_do_edge(w, k)
					DFS(k, queue)

	visited = [0] * graph.num_vertices
	queue = []
	for i in range(graph.num_vertices):
		if visited[i] is 0:
			DFS(i, queue)


def dfs_search(graph, start_v, end_v):
	print('*' * 90)
	print('from %s to %s' % (start_v, end_v))

	# dfs method 1 use recurse
	def dfs_recursion(graph, start_v, end_v):
		print('current vertex: %s' % start_v)
		visited[graph.vertices.index(start_v)] = True
		for i in range(graph.num_vertices):
			if (0 < graph.matrix[graph.vertices.index(start_v)][i] < inf) and (visited[i] == False):
				if graph.vertices[i] is end_v:
					print('find the path from %s to %s' % (start_v, end_v))
					return True
				else:
					dfs_recursion(graph, graph.vertices[i], end_v)

		return False

	# dfs method 2 use stack
	def dfs_stack(graph, start_v, end_v):  # with stack
		# 深度优先搜索
		# 深度优先搜索要得到距离起始点最远的顶点，然后不能继续前进的时候返回
		# 规则1：如果可能，访问一个邻接的未访问顶点，标记它，并把它放入栈中
		# 规则2：当不能执行规则1时，如果栈不空，就从栈中弹出一个顶点
		# 规则3：如果不能执行规则1和规则2，就完成了整个搜索过程
		my_stack = SStack()
		current_vertex_index = graph.vertices.index(start_v)
		# marked with visited
		visited[current_vertex_index] = True
		# deal with the vertex
		to_do_vertex(graph, current_vertex_index)
		# push stack
		my_stack.push(current_vertex_index)

		while not my_stack.is_empty():
			# get the first adjacent vertex of the peek of stack, and set as current vertex
			vertex_index = get_first_adjacent_vertex(graph, my_stack.top())
			if vertex_index != -1:
				visited[vertex_index] = True
				to_do_vertex(graph, vertex_index)
				if graph.vertices[vertex_index] is end_v:
					print('find the path from %s to %s' % (start_v, end_v))
					return True
				my_stack.push(vertex_index)
			else:
				my_stack.pop()

		print('can not find the path from %s to %s' % (start_v, end_v))
		return False

	def get_first_adjacent_vertex(graph, current_vertex_index):
		"""
		get current vertex first adjacent vertex
		:param graph:
		:param current_vertex_index:
		:return: if has return the index. otherwise return -1
		"""
		for i in range(graph.num_vertices):
			if (0 < graph.matrix[current_vertex_index][i] < inf) and (visited[i] is False):
				return i

		return -1


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

	dfs_stack(graph, start_v, end_v)


def bfs_search(graph, start_v, end_v):

	def bfs_queue(graph, start_v, end_v):
		"""
		//广度优先搜索
		规则1：访问下一个未来访问的邻接点（如果存在），这个顶点必须是当前顶点的邻接点，标记为已访问，并把它插入到队列中
		规则2：如果因为已经没有未访问顶点而不能执行规则1，那么从队列头取一个顶点（如果存在），并使其称为当前顶点
		规则3：如果因为队列为空而不能执行规则2，则搜索结束
		:param graph:
		:param start_v:
		:param end_v:
		:return:
		"""
		my_queue = Queue()

		current_vertex_index = graph.vertices.index(start_v)
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
					# deal with the vertex
					to_do_vertex(graph, i)
					# mark the vertex
					visited[i] = True
					# check whether come to the end
					if graph.vertices[i] is end_v:
						print('find the path from %s to %s' % (start_v, end_v))
						return True

					# enqueue the element
					my_queue.enqueue(i)

		print('can not find the path from %s to %s' % (start_v, end_v))
		return False

	print('*' * 90)
	print('from %s to %s' % (start_v, end_v))

	inf = float('inf')
	visited = [False] * graph.num_vertices

	bfs_queue(graph, start_v, end_v)


if __name__ == '__main__':
	my_graph = GraphMatrix()
	# created_graph = create_undirected_matrix(my_graph)
	created_graph = create_directed_matrix(my_graph)
	# created_graph = create_directed_graph_from_edges(my_graph)

	# my_graph.DepthFirstSearch()

	# draw_undircted_graph(created_graph)
	created_graph.draw_directed_graph()



	# DepthFirstSearch(created_graph)

	# dfs_search(created_graph, 'A', 'D')
	# dfs_search(created_graph, 'a', 'g')

	# bfs_search(created_graph, 'A', 'D')


# create_directed_graph_from_edges()


# print (createList())
# print ('-' * 80)
# print (createList3())
