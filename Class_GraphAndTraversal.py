# -*- coding: utf-8 -*-
# @Time    : 2017-11-3 16:51
# @Author  : zhangqi
# @File    : Class_GraphAndTraversal.py
# @Software: PyCharm Community Edition

from graphviz import Digraph
import networkx as nx
from networkx.classes.graph import Graph


class GraphTable:
	def __init__(self, nodes, edges, is_dir=False):
		self.nodes = nodes
		self.edges = edges
		self.is_dir = is_dir
		self.graph = []
		for node in nodes:
			self.graph.append([node])
		for edge in edges:
			for n in self.graph:
				if n[0] == edge[0]:
					n.append(edge[1])
				if not is_dir:
					if n[0] == edge[1]:
						n.append(edge[0])
		self.G = None
	
	def __str__(self):
		return 'n'.join([str(n) for n in self.graph])
	
	def draw(self):
		settings = dict(name='Graph', engine='circo', node_attr=dict(shape='circle'), format='png')
		self.G = nx.Digraph(**settings) if self.is_dir else Graph(**settings)
		for node in self.nodes:
			self.G.node(str(node), str(node))
		for edge in self.edges:
			self.G.edge(str(edge[0]), str(edge[1]))
		return self.G
	

			# settings = dict(name='Graph', engine='circo', node_attr=dict(shape='circle'), format='png')
			# self.G = Digraph(**settings) if self.is_dir else Graph(**settings)
			# for node in self.nodes:
			#     self.G.node(str(node), str(node))
			# for edge in self.edges:
			#     self.G.edge(str(edge[0]), str(edge[1]))
			# return self.G




if __name__ == '__main__':
	gt = GraphTable([1, 2, 3, 4, 5], [(1, 2), (1, 5), (2, 5), (2, 4), (5, 4), (2, 3), (3, 4)])
	print(gt)
	gt.draw()
 
	"""
	[1, 2, 5]
	[2, 1, 5, 4, 3]
	[3, 2, 4]
	[4, 2, 5, 3]
	[5, 1, 2, 4]
	"""
