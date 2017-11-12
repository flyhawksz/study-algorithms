#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/12 14:49
# @Author  : zhangqi
# @Site    : 
# @File    : Class_Queue.py
# @Software: PyCharm Community Edition

# Bradley N. Miller, David L. Ranum
# Introduction to Data Structures and Algorithms in Python
# Copyright 2005


class Queue:
    def __init__(self):
        self.items = []

    def isempty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        e = self.items.pop()
        return e

    def size(self):
        return len(self.items)


# if __name__ == '__main__':
# 	pass