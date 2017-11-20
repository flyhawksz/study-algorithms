#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/16 0:26
# @Author  : flyhawk
# @Site    : 
# @File    : question_shortest_path_graph_adj_list.py
# @Software: PyCharm Community Edition


from class_graph_adjacency_list import GraphAdjacencyList
from Class_Queue import Queue
import heapq as hq

inf = float('inf')


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
	# mark
	start_v.visited = True
	# enqueue
	my_queue.enqueue(start_v)
	# traverse
	while not my_queue.isempty():
		
		current_vertex = my_queue.dequeue()
		for v in current_vertex.neighbors:
			if not v.visited:
				distance[v.id] = distance[current_vertex.id] + 1
				previous_vertex[v.id] = current_vertex
				to_do_vertex(v)
				if v is end_v:
					print('find the path and arrive at: %s, distance is %s' % (v.id, distance[v.id]))
					return distance, previous_vertex, visited_order
				else:
					v.visited = True
					my_queue.enqueue(v)


def dijkstra_graph_adjacency_list(graph, start_v, end_v=None):
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
	unprocessed = {}
	processed = {}
	
	for v in graph.vertices_list.values():
		unprocessed[v.id] = inf
	
	unprocessed[start_v.id] = 0
	
	start_v.distance = 0
	start_v.predecessor = None
	
	current_vertex = start_v
	current_distance = 0
	
	# 所有点遍历
	for i in xrange(graph.num_vertices):
		# 2.选择未被收录的节点中的最短路径节点 收录，并作为当前节点
		# 字典是无序的，须转成 列表 方能排序
		# candidates = [node for node in unvisited.items() if node[1]]  # 找出目前还有拿些点未松弛过
		candidates = []
		for node in unprocessed.items():
			if node[1] < inf:
				candidates.append(node)
		# 如果 candidates 为空，说明所有节点都已经松弛过，或者图不连通，则退出循环
		if len(candidates) == 0:
			break
		# (1) 提取估算距离最小的顶点方法1,使用列表排序,效率相对低，但容易理解
		# # 将目前未收录，可以用来松弛的点, 按 距离 进行排序, 取最小值作为当前的节点和距离
		# # current_vertex_id, current_distance = sorted(candidates, key=lambda x: x[1])[0]
		
		# (2) 提取估算距离最小的顶点方法2，使用优先队列（元组）,效率相对高一些
		t = hq.nsmallest(1, candidates, key=lambda x: x[1])
		current_vertex_id, current_distance = t[0]
		current_vertex = graph.get_vertex(current_vertex_id)
		# 这个点已经松弛过，收录当前节点，并从未收录节点中删除
		processed[current_vertex.id] = current_distance
		unprocessed.pop(current_vertex.id)  # 字典(dict)删除元素, 可以选择两种方式, dict.pop(key)和del dict[key].
		
		# 3.前的节点，更新所有邻居的距离
		# 遍历所有邻居
		for neighbor_vertex in current_vertex.neighbors:
			# 未被访问的邻居
			if neighbor_vertex.id in unprocessed:
				new_distance = processed[current_vertex.id] + current_vertex.get_weight(neighbor_vertex)
				if new_distance < unprocessed[neighbor_vertex.id]:
					unprocessed[neighbor_vertex.id] = new_distance
					
					neighbor_vertex.distance = new_distance
					neighbor_vertex.predecessor = current_vertex
					
	if end_v:
		return processed[end_v.id]
	else:
		return processed


def dijkstra2():
	nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
	distances = {
		'B': {'A': 5, 'D': 1, 'G': 2},
		'A': {'B': 5, 'D': 3, 'E': 12, 'F': 5},
		'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
		'G': {'B': 2, 'D': 1, 'C': 2},
		'C': {'G': 2, 'E': 1, 'F': 16},
		'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
		'F': {'A': 5, 'E': 2, 'C': 16}}
	
	unvisited = {node: None for node in nodes}  # 把None作为无穷大使用
	visited = {}  # 用来记录已经松弛过的数组
	current = 'B'  # 要找B点到其他点的距离
	currentDistance = 0
	unvisited[current] = currentDistance  # B到B的距离记为0
	
	while True:
		for neighbour, distance in distances[current].items():
			if neighbour not in unvisited: continue  # 被访问过了，跳出本次循环
			newDistance = currentDistance + distance  # 新的距离
			if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:  # 如果两个点之间的距离之前是无穷大或者新距离小于原来的距离
				unvisited[neighbour] = newDistance  # 更新距离
		visited[current] = currentDistance  # 这个点已经松弛过，记录
		del unvisited[current]  # 从未访问过的字典中将这个点删除
		if not unvisited: break  # 如果所有点都松弛过，跳出此次循环
		candidates = [node for node in unvisited.items() if node[1]]  # 找出目前还有拿些点未松弛过
		current, currentDistance = sorted(candidates, key=lambda x: x[1])[0]  # 找出目前可以用来松弛的点,进行排序,取最小值
	
	return visited


def create_graph_by_add_edge():
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
	
	return g


def create_graph_by_edges():
	g = GraphAdjacencyList()
	edges = {
		'B': {'A': 5, 'D': 1, 'G': 2},
		'A': {'B': 5, 'D': 3, 'E': 12, 'F': 5},
		'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
		'G': {'B': 2, 'D': 1, 'C': 2},
		'C': {'G': 2, 'E': 1, 'F': 16},
		'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
		'F': {'A': 5, 'E': 2, 'C': 16}}
	
	for v in edges:
		for _key, _val in edges[v].items():
			g.add_edge(v, _key, _val)
	
	return g


def test_shortest_path():
	g1 = create_graph_by_add_edge()
	g2 = create_graph_by_edges()
	
	g = g2
	
	# g.draw_directed_graph()
	
	start_v = 'A'
	end_v = 'C'
	
	# shortest path for graph adjacency list
	print ('-' * 100)
	print ('traverse graph')
	print ('-' * 100)
	dist, pre_v, visited = shortest_path_unweighted_graph_adjacency_list(g, g.get_vertex(start_v), g.get_vertex(end_v))
	print ('the distance from %s to %s is %s: ' % (start_v, end_v, dist[end_v]))
	
	_v = g.get_vertex(end_v)
	print(_v.id)
	while not pre_v[_v.id] is None:
		v = pre_v[_v.id]
		print (v.id)
		if v.id in pre_v.keys():
			_v = v
		else:
			break


if __name__ == '__main__':
	visited_order = []
	
	start_v = 'B'
	end_v = 'C'
	
	# test_shortest_path()
	
	# shortest path for graph adjacency list
	print ('-' * 100)
	print ('dijkstra traverse graph')
	print ('-' * 100)
	print (dijkstra2())
	print ('-' * 100)
	g = create_graph_by_edges()
	# g.draw_directed_graph()
	print (dijkstra_graph_adjacency_list(g, g.get_vertex(start_v)))
	
	print ('the shortest distance to %s is: %s' % (end_v, dijkstra_graph_adjacency_list(g, g.get_vertex(start_v), g.get_vertex(end_v))))
	
	current_vertex = g.get_vertex(end_v)
	while current_vertex.predecessor:
		print ('%s - %s' % (current_vertex.id, current_vertex.distance))
		current_vertex = current_vertex.predecessor
		