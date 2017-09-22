# -*- coding: utf-8 -*-
# @Time    : 2017-9-19 11:13
# @Author  : zhangqi
# @File    : Class_Maze.py
# @Software: PyCharm Community Edition

from Class_SStack import SStack

# 四个方向，一步
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
maze = [[1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 0, 1, 0, 1, 1],
        [1, 1, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1]]


def mark(maze, pos):
	maze[pos[0]][pos[1]] = 2


def passible(maze, pos):
	if maze[pos[0]][pos[1]] == 0:
		return True
	else:
		return False
	
	
def print_path(end, pos, st):
	print 'end:%s ' %(end,)
	print pos
	while not st.is_empty():
		print st.pop()


# method 1 use Recursion(递归)
def find_path(maze, pos, end):
	mark(maze, pos)
	if pos == end:
		print pos,
		return True
	for i in range(4):
		nextp = pos[0] + dirs[i][0], pos[1] + dirs[i][1]
		if passible(maze, nextp):
			if find_path(maze, nextp, end):
				print pos,
				return True

	return False


# method 2 use Stack
def maze_solve_stack(maze, start, end):
	if start == end:
		print start
		return
	
	st = SStack()
	mark(maze, start)
	st.push((start, 0))
	while not st.is_empty():
		pos, nxt = st.pop()
		for i in range(nxt, 4):
			nextp = (pos[0] + dirs[i][0],
			         pos[1] + dirs[i][1])
			if nextp == end:
				print_path(end, pos, st)
				return
			if passible(maze, nextp):
				st.push((pos, i + 1))
				mark(maze, nextp)
				st.push((nextp, 0))
				break
	print 'No path found'
	

if __name__ == '__main__':
	# test method 1
	# print(find_path(maze, (1, 2), (3, 1)))
	
	# test method 2
	maze_solve_stack(maze, (1, 2), (3, 1))
