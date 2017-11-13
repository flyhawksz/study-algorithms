#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/5 17:38
# @Author  : flyhawk
# @Site    :
# @File    : Class_GraphMatrix.py
# @Software: PyCharm Community Edition


try:
    import Queue as Q #python version < 3.0
except ImportError:
    import queue as Q #python3.*


def PriorityQueue_int():
    que = Q.PriorityQueue()
    que.put(10)
    que.put(1)
    que.put(5)
    while not que.empty():
        print que.get(),
    print


def PriorityQueue_tuple():
    que = Q.PriorityQueue()
    que.put((10,'ten'))
    que.put((1,'one'))
    que.put((10/2,'five'))
    while not que.empty():
        print que.get(),
    print


if __name__ == '__main__':
    PriorityQueue_int()

    PriorityQueue_tuple()

