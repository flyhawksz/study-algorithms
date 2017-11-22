#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/16 0:26
# @Author  : flyhawk
# @Site    : 
# @File    : question_shortest_path_graph_adj_list.py
# @Software: PyCharm Community Edition


from class_graph_adjacency_list import GraphAdjacencyList
from Class_Queue import Queue
import networkx as nx
import matplotlib.pyplot as plt
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
		# 字典也能排序
		# In[21]: a = {'a': 1, 'b': 2, 'c': 4, 'd': 3}
		# 按字典值排序
		# In[22]: sorted(a.items(), key=lambda s: s[1])
		# Out[22]: [('a', 1), ('b', 2), ('d', 3), ('c', 4)]
		# 按字典键排序
		# In[23]: sorted(a.items(), key=lambda s: s[0])
		# Out[23]: [('a', 1), ('b', 2), ('c', 4), ('d', 3)]
		# candidates = [node for node in unvisited.items() if node[1]]  # 找出目前还有拿些点未松弛过
		
		# candidates = []
		# for node in unprocessed.items():
		# 	if node[1] < inf:
		# 		candidates.append(node)
		# # 如果 candidates 为空，说明所有节点都已经松弛过，或者图不连通，则退出循环
		# if len(candidates) == 0:
		# 	break
		# (1) 提取估算距离最小的顶点方法1,使用列表排序,效率相对低，但容易理解
		# # 将目前未收录，可以用来松弛的点, 按 距离 进行排序, 取最小值作为当前的节点和距离
		# # current_vertex_id, current_distance = sorted(candidates, key=lambda x: x[1])[0]
		
		# (2) 提取估算距离最小的顶点方法2，使用优先队列（元组）,效率相对高一些
		# t = hq.nsmallest(1, candidates, key=lambda x:x[1])
		
		t = sorted(unprocessed.iteritems(), key=lambda x: x[1])
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


def bellman_ford_graph_adjacency_matrix(graph, start_v):
	"""
	与 dijkstra 算法的区别是这里采用对边进行遍历比较
	Ford算法的每次迭代遍历所有边, 并对边进行松弛(relax)操作. 对边e进行松弛是指: 若从源点通过e.start到达e.stop的路径长小于已知最短路径, 则更新已知最短路径.
	若路径中不存在负环, 则进行n-1次迭代后不存在可以进行松弛的边. 因此再遍历一次边, 若存在可松弛的边说明图中存在负环.
	:param graph:
	:param start_v:
	:param end_v: 如果不提供 end_v， 则遍历，取得源点到所有节点的最短路径长度
	:return:processed　收录的节点的长度

	"""
	
	# 1.初始化
	num_vertex = graph.num_vertices
	edges = graph.edges_array
	
	# 与源点的距离
	distance = [inf] * num_vertex
	# 前驱节点 the predecessor vertex that come to current vertex
	predecessor = [0] * num_vertex
	
	current_vertex_index = graph.vertices.index(start_v)
	distance[current_vertex_index] = 0  # 这样第一次从未收录节点中取最小值,即可取到起点
	# predecessor[current_vertex_index] = None  # 起点无前驱
	
	# 所有点遍历
	for i in range(num_vertex):
		for edge in edges:
			tail_index = graph.vertices.index(edge[0])
			head_index = graph.vertices.index(edge[1])
			# print ('head index: %d' % head_index)
			edge_cost = edge[2]
			new_distance = distance[tail_index] + edge_cost
			
			# 在某边中，如果 tail 的距离 加上 该边的距离，小于 head 的距离
			if new_distance < distance[head_index]:
				# 将当前边的　head 的距离更新为新的距离　
				distance[head_index] = new_distance
				# 记录 head 的前躯为当前边的 tail
				predecessor[head_index] = edge[0]
	
	# 再次遍历检查是否存在负环　check negative loop
	flag = False
	for edge in edges:
		tail_index = graph.vertices.index(edge[0])
		head_index = graph.vertices.index(edge[1])
		edge_cost = edge[2]
		new_distance = distance[tail_index] + edge_cost
		
		# 在某边中，如果 tail 的距离 加上 该边的距离，小于 head 的距离
		if new_distance < distance[head_index]:
			# 存在负环,退出
			flag = True
			break
	if flag:  # 如果存在负环，返回错误，各距离值无效
		return False
	return distance, predecessor


# 最小生成树 kruskal
def minimum_span_tree_kruskal(graph):
	"""
	1).记Graph中有v个顶点，e个边
	2).新建图Graphnew，Graphnew中拥有原图中相同的e个顶点，但没有边
	3).将原图Graph中所有e个边按权值从小到大排序
	4).循环：从权值最小的边开始遍历每条边 直至图Graph中所有的节点都在同一个连通分量中
	    if 这条边连接的两个节点于图Graphnew中不在同一个连通分量中添加这条边到图Graphnew中
	:param graph:
	:return:
	"""
	number_vertex = graph.num_vertices
	# 用来记录当前分量的根节点, 用这个根节点来代表整个分量。如果代表元相关，则表示在同一分量中
	# 可以用武林门派来代表分量，用掌门来表示代表元，如果某个人所属门派的掌门相同，他们就是同门派的
	# 初始化代表元为节点本身
	represent_element = {v: v for v in graph.vertices}
	mst = []
	edges = graph.edges_array_for_sort
	edges.sort()
	for w, vi, vj in edges:
		# 边的两个端点属于不同的分量，即代表元
		if represent_element[vi] != represent_element[vj]:
			mst.append(((vi, vj), w))
			
			# 合并连通分量, 将代表元集合合并
			_represent_element, _another_represent_element = represent_element[vi], represent_element[vj]
			for v in graph.vertices:
				if represent_element[v] == _another_represent_element:
					represent_element[v] = _represent_element
			
			# 如果已经收集齐了所需要数量的边，结束循环
			if len(mst) == number_vertex - 1:
				break
	if len(mst) == number_vertex - 1:
		return mst
	else:
		# 图不连通，不能生成最小树
		return False


def minimum_span_tree_prim(graph):
	"""
	对于一个给定的图，
	设置两个空的集合A、B:
		A用于存储原始图的最小生成树的顶点，最开始的时候A中只包含一个顶点，
		B中存放的是这个最小生成树相邻接的边权值，最开始的B是空集的
	1、从与起点相邻接的 集合中找出权最小的节点
	2、如果未被收录，收录
	   收录的边的数量 + 1
	
	3、遍历 与当前节点相邻的节点，如果未收录，将其加入集合B
	:param graph:
	:return:
	"""
	number_vertex = graph.num_vertices
	# 最小树集合
	mst = [None] * number_vertex
	# 与最小树邻接的点的集合，采用优先堆，按权值排序
	adjacent_vertex = hq((0, 0, 0))
	# 收录边的数量
	collected_edges_count = 0
	
	while collected_edges_count < number_vertex and not adjacent_vertex.is_empty():
		_weight, _tail, _head = adjacent_vertex.dequeue()
		# 已收录则跳过
		if mst[_head]:
			continue
		collected_edges_count += 1
		
		for _v, _w in graph.get_vertex(v).neighbors:
			if not mst[_v]:
				adjacent_vertex.enqueue(_w, _head, _v)
				
	return mst

	

def draw_minimum_span_tree(graph, mst):
	G = nx.DiGraph()  # 建立一个空的无向图G
	for node in graph.vertices:
		G.add_node(str(node))
	for (_edge, _weight) in mst:
		G.add_edge(_edge[0], _edge[1], weight=_weight)
	
	# G.add_weighted_edges_from(self.edges_array)
	
	print("nodes:", G.nodes())  # 输出全部的节点： [1, 2, 3]
	print("edges:", G.edges())  # 输出全部的边：[(2, 3)]
	print("number of edges:", G.number_of_edges())  # 输出边的数量：1
	nx.draw(G, with_labels=True)
	plt.savefig("directed_graph.png")
	plt.show()


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


def create_graph_by_edges_with_negative_edge():
	g = GraphAdjacencyList()
	edges = {
		'B': {'A': 5, 'D': 1, 'G': 2},
		'A': {'B': 5, 'D': 3, 'E': 12, 'F': 5},
		'D': {'B': 1, 'G': -1, 'E': 1, 'A': 3},
		'G': {'B': 2, 'D': 1, 'C': 2},
		'C': {'G': 2, 'E': 1, 'F': 16},
		'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
		'F': {'A': 5, 'E': -2, 'C': 16}}
	
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


def test_dijkstra_graph_adjacency_list():
	# shortest path for graph adjacency list
	print ('-' * 100)
	print ('dijkstra traverse graph')
	print ('-' * 100)
	print (dijkstra2())
	print ('-' * 100)
	g = create_graph_by_edges()
	# g.draw_directed_graph()
	print (dijkstra_graph_adjacency_list(g, g.get_vertex(start_v)))
	
	print ('the shortest distance to %s is: %s' %
	       (end_v, dijkstra_graph_adjacency_list(g, g.get_vertex(start_v), g.get_vertex(end_v))))
	
	current_vertex = g.get_vertex(end_v)
	while current_vertex.predecessor:
		print ('%s - %s' % (current_vertex.id, current_vertex.distance))
		current_vertex = current_vertex.predecessor


def test_bellman_ford_graph_adjacency_matrix():
	g = create_graph_by_edges_with_negative_edge()
	
	start_v = 'B'
	
	print ('-' * 100)
	print ('bellman_ford_graph_adjacency_matrix')
	print ('-' * 100)
	
	t = bellman_ford_graph_adjacency_matrix(g, start_v)
	# 如果没有负环
	if t:
		distance, predecessor = t
		print (distance)
		
		_v = g.vertices.index(end_v)
		print('%s index: %s  distance: %s' % (g.vertices[_v], _v, distance[_v]))
	
	else:
		print ('there is a negative cycle')


def test_minimum_span_tree_kruskal():
	print ('-' * 100)
	print ('bellman_ford_graph_adjacency_matrix')
	print ('-' * 100)
	
	g = create_graph_by_edges()
	
	mst = minimum_span_tree_kruskal(g)
	print (mst)
	
	draw_minimum_span_tree(g, mst)


if __name__ == '__main__':
	visited_order = []
	
	start_v = 'B'
	end_v = 'C'
	
	# test_shortest_path()
	
	# test_dijkstra_graph_adjacency_list()
	
	# test_bellman_ford_graph_adjacency_matrix()
	
	test_minimum_span_tree_kruskal()
