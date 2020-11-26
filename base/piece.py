import sys
sys.path.insert(1,'./AI')

import board
import score


class Piece():

	def __init__(self,position,player,movement=[False,False,False]):

		self.position = position
		self.player = player
		self.moves = []
		self.isPinned = False
		self.keepPiece = None

		# Defining possible movements of piece type to check 
		# for pin

		self.movement = movement

	def movePlayer(self,pos,another_pos):
		self.position=another_pos
		board.Board.BOARD[pos[0]][pos[1]]=None

		score.updateHash(self,pos,another_pos)

		if(board.Board.BOARD[another_pos[0]][another_pos[1]]!=None):
			board.Board.BOARD[another_pos[0]][another_pos[1]]=self
			return True
		else:
			board.Board.BOARD[another_pos[0]][another_pos[1]]=self
			return False





	

	

