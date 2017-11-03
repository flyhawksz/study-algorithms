#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/2 22:35
# @Author  : zhangqi
# @Site    : 
# @File    : Question_Graph_BFS.py
# @Software: PyCharm Community Edition


from Class_Graph import Graph, Vertex
from queue import Queue

def dfs(g, start):
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

	:param g:
	:param start:
	:return:
	"""



def bfs(g, start):
	"""
	广度优先搜索算法使用我们先前开发的邻接表表示。此外，它使用一个 Queue，一个关键的地方，决定下一个探索的顶点
	BFS 从起始顶点开始，颜色从灰色开始，表明它正在被探索。另外两个值，即距离和前导，
	对于起始顶点分别初始化为 0 和 None 。最后，放到一个队列中
	:param g: a instance of graph
	:param start: a instance vertex, such as g.getVertex('FOOL')
	:return:
	"""
	start.setDistance(0)
	start.setPred(None)
	vertQueue = Queue()
	vertQueue.enqueue(start)
	while vertQueue.size() > 0:
		currentVert = vertQueue.dequeue()
		for nbr in currentVert.getConnections():
			if nbr.getColor() == 'white':
				nbr.setColor('gray')
				nbr.setDistance(currentVert.getDistance() + 1)
				nbr.setPred(currentVert)
				vertQueue.enqueue(nbr)

			currentVert.setColor('black')


def buildGraph(wordFile):
	d = {}
	g = Graph()
	wfile = file(wordFile, 'r')
	# create buckets of words that differ by one letter
	for line in wfile:
		word = line[:-1]
		for i in range(len(word)):
			bucket = word[:i] + '_' + word[i+1:]
			if bucket in d:
				d[bucket].append(word)
			else:
				d[bucket] = [word]
	# add vertices and edges for words in the same bucket
	for bucket in d.keys():
		for word1 in d[bucket]:
			for word2 in d[bucket]:
				if word1 != word2:
					g.addEdge(word1, word2)

	return g


def traverse(y):
	"""
	展示了如何按前导链接打印出字梯
	:param y: a instance of vertex , such as g.getVertex('FOOL')
	:return:
	"""
	x = y
	while x.getPred():
		print(x.getId())
		x = x.getPred()
	print(x.getId())




if __name__ == '__main__':
	g = buildGraph('e:\\fourletterwords.txt')
	bfs(g, g.getVertex('FOOL'))
	# traverse(g.getVertex('FOOL'))