import sys
sys.path.insert(1,'./base')

from aliases import *
import value
import board


def initializeHash():

	for i in range(1,9):
		for j in range(1,9):
			if board.Board.BOARD[i][j]!=None :
				p = board.Board.BOARD[i][j]
				if(p.player==BLACK):
					value.HASH_VALUE -= value.VLE[value.MODE][board.Board.instanceOf(p)][j][i]
				else:
					value.HASH_VALUE += value.VLE[value.MODE][board.Board.instanceOf(p)][j][i]


	print(value.HASH_VALUE)


def updateHash(p,pos,another_pos):
	
	if(p.player==BLACK):
		i,j = pos[0],pos[1]
		value.HASH_VALUE += value.VLE[value.PREV_MODE][board.Board.instanceOf(p)][j][i]

		i,j = another_pos[0],another_pos[1]
		value.HASH_VALUE -= value.VLE[value.MODE][board.Board.instanceOf(p)][j][i]

	else:
		i,j = pos[0],pos[1]
		value.HASH_VALUE -= value.VLE[value.PREV_MODE][board.Board.instanceOf(p)][j][i]

		i,j = another_pos[0],another_pos[1]
		value.HASH_VALUE += value.VLE[value.MODE][board.Board.instanceOf(p)][j][i]


def updateMode():
	pass