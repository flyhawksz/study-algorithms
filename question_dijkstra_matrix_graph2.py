# -*- coding: utf-8 -*-
# @Time    : 2017-11-20 15:04
# @Author  : flyhawk
# @File    : question_dijkstra_matrix_graph2.py
# @Software: PyCharm Community Edition

import heapq


def make_mat(m, n, fill=None):
    mat = []
    for i in range(m):
        mat.append([fill] * n)
    return mat


INF = 1e6


def get_edges(graph):
    n = len(graph)
    edges = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                edges.append((i, j, graph[i][j]))
    return edges


def show(path, start, stop):
    i = stop
    tmp = [stop]
    while i != start:
        i = path[i]
        tmp.append(i)
    return list(reversed(tmp))


def dijkstra(graph, v0):
    n = len(graph)
    dis = [INF] * n
    dis[v0] = 0
    path = [0] * n

    unvisited = get_edges(graph)
    heapq.heapify(unvisited)

    while len(unvisited):
        u = heapq.heappop(unvisited)[0]
        for v in range(len(graph[u])):
            w = graph[u][v]
            if dis[u] + w < dis[v]:
                dis[v] = dis[u] + w
                path[v] = u

    return dis, path


if __name__ == '__main__':
    graph = make_mat(5, 5, fill=INF)
    graph[0][1] = 1
    graph[0][2] = 3
    graph[1][2] = 3
    graph[1][3] = 2
    graph[1][4] = 2
    graph[3][1] = 1
    graph[3][2] = 5
    graph[4][3] = 3

    dis, path = dijkstra(graph, 0)

    v0 = 0
    for i in range(len(graph)):
        if i == v0:
            continue
        print("%d->%d: " % (v0, i))
        print(show(path, v0, i))
        print(dis[i])
