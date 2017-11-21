# -*- coding: utf-8 -*-
# @File    : question_shortest_path_floyd.py

# python实现Floyd算法
# 作者：si1ver zhou_weilin@qq.com
# 时间：2015.08.25
N = 4
_ = float('inf')  # 无穷大
graph = [[0, 2, 6, 4], [_, 0, 3, _], [7, _, 0, 1], [5, _, 12, 0]]
path = [[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]]  # 记录路径，最后一次经过的点


def back_path(path, i, j):  # 递归回溯
	while -1 != path[i][j]:
		back_path(path, i, path[i][j])
		back_path(path, path[i][j], j)
		print (path[i][j],)
		return ;
	return ;


print ("Graph:\n", graph)
for k in range(N):
	for i in range(N):
		for j in range(N):
			if graph[i][j] > graph[i][k] + graph[k][j]:
				graph[i][j] = graph[i][k] + graph[k][j]
				path[i][j] = k
print ("Shortest distance:\n", graph)
print ("Path:\n", path)
print ("Points pass-by:")
for i in range(N):
	for j in range(N):
		print ("%d -> %d:" % (i, j),)
		back_path(path, i, j)
		print ("\n",)
