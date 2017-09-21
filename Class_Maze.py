# -*- coding: utf-8 -*-
# @Time    : 2017-9-19 11:13
# @Author  : zhangqi
# @File    : Class_Maze.py
# @Software: PyCharm Community Edition

# 四个方向，一步
dirs = [(0, 1), (1,0), (0, -1), (-1, 0)]
maze = [[1, 0, 0, 1, 0, 1],
      [1, 1, 1, 0, 1, 0],
      [0, 0, 1, 0, 1, 0],
      [0, 1, 1, 1, 0, 0],
      [0, 0, 0, 1, 0, 0],
      [1, 0, 0, 0, 0, 0]]



def mark(maze, pos):
	maze[pos[0]][pos[1]] = 2


def passible(maze, pos):
	return maze[pos[0]][pos[1]] == 0


def find_path(maze, pos, end):
	mark(maze, pos)
	if pos == end:
		print (pos, )
		return True
	for i in range(4):
		nextp = pos[0] + dirs[i][0], pos[1] + dirs[i][1]
		if passible(maze, nextp):
			print (pos,)
			return True

	return False


if __name__ == '__main__':
	print(find_path(maze, (1, 3), (0, 2)))
