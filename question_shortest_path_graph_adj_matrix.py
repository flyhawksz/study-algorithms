#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/16 0:25
# @Author  : flyhawk
# @Site    : 
# @File    : question_shortest_path_graph_adj_matrix.py
# @Software: PyCharm Community Edition

from Class_GraphMatrix import GraphMatrix
from Class_Queue import Queue
import heapq as hq
import random


def create_random_matrix(vex_num=10):
	'''
	随机图顶点矩阵生成器
	输入：顶点个数，即矩阵维数
	'''
	nodes = []
	matrix = []
	for i in range(vex_num):
		one_list = []
		for j in range(vex_num):
			one_list.append(random.randint(1, 100))
		matrix.append(one_list)
		nodes.append('v' + str(i))
		
	my_graph = GraphMatrix(nodes, matrix)
	# print(my_graph)
	return my_graph

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


# bfs_queue method
def shortest_path_unweighted_graph_adjacency_matrix(graph, start_v, end_v):
	"""
	
	:param graph:
	:param start_v: string 'a'
	:param end_v:  string 'h'
	:return: distance, previous_vertex, visited_order
	"""
	def to_do_vertex(graph, vertex_index):
		visited_order.append(graph.vertices[vertex_index])
		print('visited vertex: %s' % graph.vertices[vertex_index])

	visited = [False] * g.num_vertices
	visited_order = []
	
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
			if (0 < graph.matrix[current_vertex_index][i] < inf) and not visited[i]:
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


def dijkstra_graph_adjacency_matrix(graph, start_v, end_v=None):
	"""
	 1 Dijkstra(G, W, s)　　　　　　//G表示图，W表示权值函数，s表示源顶点
	 2 　　d[s] ←0　　　　　　　　　　//源点到源点最短路为0
	 3 　　for each v ∈ V - {s}　　//3-8行均为初始化操作
	 4 　　　　　do d[v]←∞
	 5 　 　　　　  parent[v]←NIL
	 6 　　S←∅　　　　　　　　
	 7 　　Q←V　　　　　　　　//此处Q为优先队列，存储未进入S的各顶点以及从源点到这些顶点的估算距离，采用二叉堆（最小堆）实现，越小越优先
	 8 　　while Q≠∅
	 9 　　 do u←Extract-Min(Q)　　//提取估算距离最小的顶点，在优先队列中位于顶部，出队列，放入集合S中
	10 　　　  S←S∪{u}
	11 　　　　for each v ∈ Adj(u)　　//松弛操作，对与u相邻的每个顶点v，进行维持三角不等式成立的松弛操作。
	12 　　　　　　do if d[v] > d[u] + w(u, v)
	13 　　　　　　　　then d[v] = d[u] + w(u, v)　　//这一步隐含了更新优先队列中的值，DECREASE。
	14 　　　　　　　　　　  parent[v]←u　　　　　　//置v的前驱结点为u
	:param graph:
	:param start_v:
	:param end_v: 如果不提供 end_v， 则遍历，取得源点到所有节点的最短路径长度
	:return:processed　收录的节点的长度

	"""
	
	# 1.初始化
	# 未收录的节点
	unprocessed = {}
	# 已收录的节点
	processed = {}
	# 前驱节点 the predecessor vertex that come to current vertex
	predecessor = {}

	# 未收录节点全部初始化为无穷
	for i in range(graph.num_vertices):
		unprocessed[i] = inf
	# 起点
	current_vertex_index = graph.vertices.index(start_v)
	unprocessed[current_vertex_index] = 0  # 这样第一次从未收录节点中取最小值,即可取到起点
	predecessor[current_vertex_index] = None  # 起点无前驱
	current_distance = 0
	
	# 所有点遍历
	while unprocessed:
		# 2.选择未被收录的节点中的最短路径节点 收录，并作为当前节点
		candidates = []
		for v in unprocessed.items():
			if v[1] < inf:
				candidates.append(v)
		# 如果 candidates 为空，说明所有节点都已经松弛过，或者图不连通，则退出循环
		if len(candidates) == 0:
			break
		# (1) 提取估算距离最小的顶点方法1,使用列表排序,效率相对低，但容易理解
		# 将目前未收录，可以用来松弛的点, 按 距离 进行排序, 取最小值作为当前的节点和距离
		# current_vertex_index, current_distance = sorted(candidates, key=lambda x: x[1])[0]
		
		# (2) 提取估算距离最小的顶点方法2，使用优先队列（元组）,效率相对高一些
		t = hq.nsmallest(1, candidates, key=lambda x: x[1])
		current_vertex_index, current_distance = t[0]
		
		processed[current_vertex_index] = current_distance
		unprocessed.pop(current_vertex_index)  # 字典(dict)删除元素, 可以选择两种方式, dict.pop(key)和del dict[key].
		
		# 3.前的节点，更新所有邻居的距离
		# 遍历所有邻居
		for v_index in range(graph.num_vertices):
			# 未被收录的邻居
			if v_index in unprocessed:
				new_distance = processed[current_vertex_index] + graph.matrix[current_vertex_index][v_index]
				# 如果新路径更短
				if new_distance < unprocessed[v_index]:
					# 更新距离
					unprocessed[v_index] = new_distance
					# 更新前驱
					predecessor[v_index] = current_vertex_index
					
	return processed, predecessor


def test_shortest_path_unweighted_graph_adjacency_matrix(g, start_v, end_v):
	# shortest path for graph adjacency matrix
	print ('-'*100)
	print ('traverse graph')
	print ('-'*100)
	dist, pre_v, visited = shortest_path_unweighted_graph_adjacency_matrix(g, start_v, end_v)
	print ('the distance from %s to %s is %s: ' % (start_v, end_v, dist[g.vertices.index(end_v)]))

	_v = g.vertices.index(end_v)
	print(g.vertices[_v])
	while not pre_v[_v] is None:
		# if pre_v[_v]:
		v = pre_v[_v]
		print (g.vertices[v])
		_v = v


def test_dijkstra_graph_adjacency_matrix(g, start_v, end_v):
	print ('-' * 100)
	print ('dijkstra_graph_adjacency_matrix')
	print ('-' * 100)
	
	distance, predecessor = dijkstra_graph_adjacency_matrix(g, start_v)
	print (distance)
	
	_v = g.vertices.index(end_v)
	print('%s index: %s  distance: %s' % (g.vertices[_v], _v, distance[_v]))
	
	while not predecessor[_v] is None:
		# if pre_v[_v]:
		v = predecessor[_v]
		print ('%s index: %s  distance: %s' % (g.vertices[v], v, distance[v]))
		_v = v


if __name__ == '__main__':
	_graph = GraphMatrix()
	# g = create_undirected_matrix(_graph)
	# g = create_directed_matrix(_graph)
	# g = create_directed_graph_from_edges(_graph)
	g = create_random_matrix(50)
	
	# g.draw_directed_graph()

	start_v = 'a'
	end_v = 'h'

	inf = float('inf')

	# 1.测试无权重最短路径
	# test_shortest_path_unweighted_graph_adjacency_matrix(g, start_v, end_v)
	
	# 2.测试有权重最短路径 Dijkstra
	start_v = 'v0'
	end_v = 'v45'
	test_dijkstra_graph_adjacency_matrix(g, start_v, end_v)
	

