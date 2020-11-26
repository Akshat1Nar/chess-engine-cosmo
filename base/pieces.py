import sys
sys.path.insert(1,'./AI')

from piece import Piece
import board
from aliases import *
import score

class Pawn(Piece):

	def __init__(self,position,player,enpassant=False,moved=False):

		super().__init__(position,player)
		self.moved=moved
		self.movesD=[]
		self.enpassant = enpassant
		

	def updateMoves(self,flag=True):

		
		self.moves = []
		self.movesD = []
		
		if(self.isPinned==True):
			return

		x,y = self.position.x,self.position.y
		moves = []
		movesD = []

		
		#----------------------------------------------------
		if(self.player==WHITE):

			
			#------------------------------------------
			#Double Pawn move
			if(self.moved==False):
				x_,y_ = x+2*board.Board.POSITION_FOR_WHITE,y
				x__ = x+1*board.Board.POSITION_FOR_WHITE
				if(isValid((x_,y_))):
					if(not board.Board.isPieceAt(POSITION._make((x_,y_))) and not board.Board.isPieceAt(POSITION._make((x__,y_)))):
						moves.append(POSITION._make((x_,y_)))



			#------------------------------------------
			# Normal pawn move
			x_,y_ = x+1*board.Board.POSITION_FOR_WHITE,y
			if(isValid((x_,y_))):
				if(not board.Board.isPieceAt(POSITION._make((x_,y_)))):
					moves.append(POSITION._make((x_,y_)))


			
			#------------------------------------------
			# pawn move diagonally
			x_,y_ = x+1*board.Board.POSITION_FOR_WHITE,y+1
			if(isValid((x_,y_))):
				board.Board.CHECK_SQUARES[self.player][x_][y_]=PAWN
				if(board.Board.isPieceAt(POSITION._make((x_,y_)))):
					if(board.Board.BOARD[x_][y_].player!=self.player and not isinstance(board.Board.BOARD[x_][y_].player,King)):
						movesD.append(POSITION._make((x_,y_)))
	
	
			# pawn move diagonally
			x_,y_ = x+1*board.Board.POSITION_FOR_WHITE,y-1
			if(isValid((x_,y_))):
				board.Board.CHECK_SQUARES[self.player][x_][y_]=PAWN
				if(board.Board.isPieceAt(POSITION._make((x_,y_)))):
					if(board.Board.BOARD[x_][y_].player!=self.player and not isinstance(board.Board.BOARD[x_][y_].player,King)):
						movesD.append(POSITION._make((x_,y_)))


		#----------------------------------------------------

		elif(self.player==BLACK):

			#------------------------------------------
			#Double Pawn move
			if(self.moved==False):
				x_,y_ = x+2*board.Board.POSITION_FOR_BLACK,y
				x__ = x+1*board.Board.POSITION_FOR_BLACK
				if(isValid((x_,y_))):
					if(not board.Board.isPieceAt(POSITION._make((x_,y_))) and not board.Board.isPieceAt(POSITION._make((x__,y_)))):
						moves.append(POSITION._make((x_,y_)))



			#------------------------------------------
			# Normal pawn move
			x_,y_ = x+1*board.Board.POSITION_FOR_BLACK,y
			if(isValid((x_,y_))):
				if(not board.Board.isPieceAt(POSITION._make((x_,y_)))):
					moves.append(POSITION._make((x_,y_)))


			
			#------------------------------------------
			# pawn move diagonally
			x_,y_ = x+1*board.Board.POSITION_FOR_BLACK,y+1
			if(isValid((x_,y_))):
				board.Board.CHECK_SQUARES[self.player][x_][y_]=PAWN
				if(board.Board.isPieceAt(POSITION._make((x_,y_)))):
					if(board.Board.BOARD[x_][y_].player!=self.player and not isinstance(board.Board.BOARD[x_][y_].player,King)):
						movesD.append(POSITION._make((x_,y_)))
	
	
			# pawn move diagonally
			x_,y_ = x+1*board.Board.POSITION_FOR_BLACK,y-1
			if(isValid((x_,y_))):
				board.Board.CHECK_SQUARES[self.player][x_][y_]=PAWN
				if(board.Board.isPieceAt(POSITION._make((x_,y_)))):
					if(board.Board.BOARD[x_][y_].player!=self.player and not isinstance(board.Board.BOARD[x_][y_].player,King)):
						movesD.append(POSITION._make((x_,y_)))


		#----------------------------------------------------

		else:
			raise NameError("Unknown Player")


		#----------------------------------------------------
		self.movesD = movesD
		moves.extend(movesD)

		if flag==False:
			self.moves = moves

		else:

			preserve = self.position
			for each in moves:
				preserve_piece = board.Board.BOARD[each.x][each.y]

				self.movePlayer(self.position,each)
				
				if(board.Board.checkCheck()==False):
					self.moves.append(each)

				self.movePlayer(self.position,preserve)
				board.Board.BOARD[each.x][each.y] = preserve_piece

		# self.moves = moves





class Queen(Piece):

	def __init__(self,position,player):

		super().__init__(position,player)
		self.movement = [True,True,True]

	def updateMoves(self,flag=True):

		

		self.moves = []
		
		if(self.isPinned==True):
			return

		moves = []
		x,y = self.position.x,self.position.y

		#----------------------------------------------------------
		#X_AXIS

		x_,y_ = x+1,y
		while isValid((x_,y_)):
			if(board.Board.isPieceAt(POSITION._make((x_,y_)))):
				if(board.Board.getPiece(POSITION._make((x_,y_))).player!=self.player and not isinstance(board.Board.getPiece(POSITION._make((x_,y_))).player,King)):
					moves.append(POSITION._make((x_,y_)))
				elif (board.Board.BOARD[x_][y_].player==self.player and not isinstance(board.Board.BOARD[x_][y_].player,King)):
					board.Board.CHECK_SQUARES[self.player][x_][y_]=QUEEN
				break
			else:
				moves.append(POSITION._make((x_,y_)))
			x_+=1


		x_,y_ = x-1,y
		while isValid((x_,y_)):
			if(board.Board.isPieceAt(POSITION._make((x_,y_)))):
				if(board.Board.getPiece(POSITION._make((x_,y_))).player!=self.player and not isinstance(board.Board.getPiece(POSITION._make((x_,y_))).player,King)):
					moves.append(POSITION._make((x_,y_)))
				elif (board.Board.BOARD[x_][y_].player==self.player and not isinstance(board.Board.BOARD[x_][y_].player,King)):
					board.Board.CHECK_SQUARES[self.player][x_][y_]=QUEEN
				break
			else:
				moves.append(POSITION._make((x_,y_)))
			x_-=1
		#----------------------------------------------------------


		#----------------------------------------------------------
		#Y_AXIS

		x_,y_ = x,y+1
		while isValid((x_,y_)):
			if(board.Board.isPieceAt(POSITION._make((x_,y_)))):
				if(board.Board.getPiece(POSITION._make((x_,y_))).player!=self.player and not isinstance(board.Board.getPiece(POSITION._make((x_,y_))).player,King)):
					moves.append(POSITION._make((x_,y_)))
				elif (board.Board.BOARD[x_][y_].player==self.player and not isinstance(board.Board.BOARD[x_][y_].player,King)):
					board.Board.CHECK_SQUARES[self.player][x_][y_]=QUEEN
				break
			else:
				moves.append(POSITION._make((x_,y_)))
			y_+=1


		x_,y_ = x,y-1
		while isValid((x_,y_)):
			if(board.Board.isPieceAt(POSITION._make((x_,y_)))):
				if(board.Board.getPiece(POSITION._make((x_,y_))).player!=self.player and not isinstance(board.Board.getPiece(POSITION._make((x_,y_))).player,King)):
					moves.append(POSITION._make((x_,y_)))
				elif (board.Board.BOARD[x_][y_].player==self.player and not isinstance(board.Board.BOARD[x_][y_].player,King)):
					board.Board.CHECK_SQUARES[self.player][x_][y_]=QUEEN
				break
			else:
				moves.append(POSITION._make((x_,y_)))
			y_-=1
		#----------------------------------------------------------



		#----------------------------------------------------------
		#DIAGONAL

		x_,y_ = x+1,y+1
		while isValid((x_,y_)):
			if(board.Board.isPieceAt(POSITION._make((x_,y_)))):
				if(board.Board.getPiece(POSITION._make((x_,y_))).player!=self.player and not isinstance(board.Board.getPiece(POSITION._make((x_,y_))).player,King)):
					moves.append(POSITION._make((x_,y_)))
				elif (board.Board.BOARD[x_][y_].player==self.player and not isinstance(board.Board.BOARD[x_][y_].player,King)):
					board.Board.CHECK_SQUARES[self.player][x_][y_]=QUEEN
				break
			else:
				moves.append(POSITION._make((x_,y_)))
			y_+=1
			x_+=1


		x_,y_ = x-1,y-1
		while isValid((x_,y_)):
			if(board.Board.isPieceAt(POSITION._make((x_,y_)))):
				if(board.Board.getPiece(POSITION._make((x_,y_))).player!=self.player and not isinstance(board.Board.getPiece(POSITION._make((x_,y_))).player,King)):
					moves.append(POSITION._make((x_,y_)))
				elif (board.Board.BOARD[x_][y_].player==self.player and not isinstance(board.Board.BOARD[x_][y_].player,King)):
					board.Board.CHECK_SQUARES[self.player][x_][y_]=QUEEN
				break
			else:
				moves.append(POSITION._make((x_,y_)))
			y_-=1
			x_-=1


		x_,y_ = x+1,y-1
		while isValid((x_,y_)):
			if(board.Board.isPieceAt(POSITION._make((x_,y_)))):
				if(board.Board.getPiece(POSITION._make((x_,y_))).player!=self.player and not isinstance(board.Board.getPiece(POSITION._make((x_,y_))).player,King)):
					moves.append(POSITION._make((x_,y_)))
				elif (board.Board.BOARD[x_][y_].player==self.player and not isinstance(board.Board.BOARD[x_][y_].player,King)):
					board.Board.CHECK_SQUARES[self.player][x_][y_]=QUEEN
				break
			else:
				moves.append(POSITION._make((x_,y_)))
			y_-=1
			x_+=1


		x_,y_ = x-1,y+1
		while isValid((x_,y_)):
			if(board.Board.isPieceAt(POSITION._make((x_,y_)))):
				if(board.Board.getPiece(POSITION._make((x_,y_))).player!=self.player and not isinstance(board.Board.getPiece(POSITION._make((x_,y_))).player,King)):
					moves.append(POSITION._make((x_,y_)))
				elif (board.Board.BOARD[x_][y_].player==self.player and not isinstance(board.Board.BOARD[x_][y_].player,King)):
					board.Board.CHECK_SQUARES[self.player][x_][y_]=QUEEN
				break
			else:
				moves.append(POSITION._make((x_,y_)))
			y_+=1
			x_-=1


		#------------------------------------------------------------

		if flag==False:
			self.moves = moves

		else:

			preserve = self.position
			for each in moves:
				preserve_piece = board.Board.BOARD[each.x][each.y]

				self.movePlayer(self.position,each)
				
				if(board.Board.checkCheck()==False):
					self.moves.append(each)

				self.movePlayer(self.position,preserve)
				board.Board.BOARD[each.x][each.y] = preserve_piece

		# self.moves = moves



		
		
		



class Bishop(Piece):

	def __init__(self,position,player):

		super().__init__(position,player)
		self.movement = [False,False,True]

	def updateMoves(self,flag=True):

		

		self.moves = []
		
		if(self.isPinned==True):
			return

		moves = []
		x,y = self.position.x,self.position.y

		#----------------------------------------------------------
		#DIAGONAL

		x_,y_ = x+1,y+1
		while isValid((x_,y_)):
			if(board.Board.isPieceAt(POSITION._make((x_,y_)))):
				if(board.Board.getPiece(POSITION._make((x_,y_))).player!=self.player and not isinstance(board.Board.getPiece(POSITION._make((x_,y_))).player,King)):
					moves.append(POSITION._make((x_,y_)))
				elif (board.Board.BOARD[x_][y_].player==self.player and not isinstance(board.Board.BOARD[x_][y_].player,King)):
					board.Board.CHECK_SQUARES[self.player][x_][y_]=BISHOP
				break
			else:
				moves.append(POSITION._make((x_,y_)))
			y_+=1
			x_+=1


		x_,y_ = x-1,y-1
		while isValid((x_,y_)):
			if(board.Board.isPieceAt(POSITION._make((x_,y_)))):
				if(board.Board.getPiece(POSITION._make((x_,y_))).player!=self.player and not isinstance(board.Board.getPiece(POSITION._make((x_,y_))).player,King)):
					moves.append(POSITION._make((x_,y_)))
				elif (board.Board.BOARD[x_][y_].player==self.player and not isinstance(board.Board.BOARD[x_][y_].player,King)):
					board.Board.CHECK_SQUARES[self.player][x_][y_]=BISHOP
				break
			else:
				moves.append(POSITION._make((x_,y_)))
			y_-=1
			x_-=1


		x_,y_ = x+1,y-1
		while isValid((x_,y_)):
			if(board.Board.isPieceAt(POSITION._make((x_,y_)))):
				if(board.Board.getPiece(POSITION._make((x_,y_))).player!=self.player and not isinstance(board.Board.getPiece(POSITION._make((x_,y_))).player,King)):
					moves.append(POSITION._make((x_,y_)))
				elif (board.Board.BOARD[x_][y_].player==self.player and not isinstance(board.Board.BOARD[x_][y_].player,King)):
					board.Board.CHECK_SQUARES[self.player][x_][y_]=BISHOP
				break
			else:
				moves.append(POSITION._make((x_,y_)))
			y_-=1
			x_+=1


		x_,y_ = x-1,y+1
		while isValid((x_,y_)):
			if(board.Board.isPieceAt(POSITION._make((x_,y_)))):
				if(board.Board.getPiece(POSITION._make((x_,y_))).player!=self.player and not isinstance(board.Board.getPiece(POSITION._make((x_,y_))).player,King)):
					moves.append(POSITION._make((x_,y_)))
				elif (board.Board.BOARD[x_][y_].player==self.player and not isinstance(board.Board.BOARD[x_][y_].player,King)):
					board.Board.CHECK_SQUARES[self.player][x_][y_]=BISHOP
				break
			else:
				moves.append(POSITION._make((x_,y_)))
			y_+=1
			x_-=1


		#------------------------------------------------------------

		if flag==False:
			self.moves = moves

		else:

			preserve = self.position
			for each in moves:
				preserve_piece = board.Board.BOARD[each.x][each.y]

				self.movePlayer(self.position,each)
				
				if(board.Board.checkCheck()==False):
					self.moves.append(each)

				self.movePlayer(self.position,preserve)
				board.Board.BOARD[each.x][each.y] = preserve_piece

		# self.moves = moves


		
		
		


class Rook(Piece):

	def __init__(self,position,player,moved=False):

		super().__init__(position,player)
		self.movement = [True,True,False]
		self.moved = moved

	def updateMoves(self,flag=True):
		

		self.moves = []
		
		if(self.isPinned==True):
			return

		moves = []
		x,y = self.position.x,self.position.y

		#----------------------------------------------------------
		#X_AXIS

		x_,y_ = x+1,y
		while isValid((x_,y_)):
			if(board.Board.isPieceAt(POSITION._make((x_,y_)))):
				if(board.Board.getPiece(POSITION._make((x_,y_))).player!=self.player and not isinstance(board.Board.getPiece(POSITION._make((x_,y_))).player,King)):
					moves.append(POSITION._make((x_,y_)))
				elif (board.Board.BOARD[x_][y_].player==self.player and not isinstance(board.Board.BOARD[x_][y_].player,King)):
					board.Board.CHECK_SQUARES[self.player][x_][y_]=ROOK
				break
			else:
				moves.append(POSITION._make((x_,y_)))
			x_+=1


		x_,y_ = x-1,y
		while isValid((x_,y_)):
			if(board.Board.isPieceAt(POSITION._make((x_,y_)))):
				if(board.Board.getPiece(POSITION._make((x_,y_))).player!=self.player and not isinstance(board.Board.getPiece(POSITION._make((x_,y_))).player,King)):
					moves.append(POSITION._make((x_,y_)))
				elif (board.Board.BOARD[x_][y_].player==self.player and not isinstance(board.Board.BOARD[x_][y_].player,King)):
					board.Board.CHECK_SQUARES[self.player][x_][y_]=ROOK
				break
			else:
				moves.append(POSITION._make((x_,y_)))
			x_-=1
		#----------------------------------------------------------


		#----------------------------------------------------------
		#Y_AXIS

		x_,y_ = x,y+1
		while isValid((x_,y_)):
			if(board.Board.isPieceAt(POSITION._make((x_,y_)))):
				if(board.Board.getPiece(POSITION._make((x_,y_))).player!=self.player and not isinstance(board.Board.getPiece(POSITION._make((x_,y_))).player,King)):
					moves.append(POSITION._make((x_,y_)))
				elif (board.Board.BOARD[x_][y_].player==self.player and not isinstance(board.Board.BOARD[x_][y_].player,King)):
					board.Board.CHECK_SQUARES[self.player][x_][y_]=ROOK
				break
			else:
				moves.append(POSITION._make((x_,y_)))
			y_+=1


		x_,y_ = x,y-1
		while isValid((x_,y_)):
			if(board.Board.isPieceAt(POSITION._make((x_,y_)))):
				if(board.Board.getPiece(POSITION._make((x_,y_))).player!=self.player and not isinstance(board.Board.getPiece(POSITION._make((x_,y_))).player,King)):
					moves.append(POSITION._make((x_,y_)))
				elif (board.Board.BOARD[x_][y_].player==self.player and not isinstance(board.Board.BOARD[x_][y_].player,King)):
					board.Board.CHECK_SQUARES[self.player][x_][y_]=ROOK
				break
			else:
				moves.append(POSITION._make((x_,y_)))
			y_-=1
		#----------------------------------------------------------

		if flag==False:
			self.moves = moves

		else:

			preserve = self.position
			for each in moves:
				preserve_piece = board.Board.BOARD[each.x][each.y]

				self.movePlayer(self.position,each)
				
				if(board.Board.checkCheck()==False):
					self.moves.append(each)

				self.movePlayer(self.position,preserve)
				board.Board.BOARD[each.x][each.y] = preserve_piece

		# self.moves = moves


		
		
		

		

class King(Piece):

	def __init__(self,position,player,moved=False):

		super().__init__(position,player)
		self.moved=moved


	def movePlayer(self,pos,another_pos):
		self.position=another_pos
		board.Board.BOARD[pos[0]][pos[1]]=None

		rValue = None

		if(board.Board.BOARD[another_pos[0]][another_pos[1]]!=None):
			board.Board.BOARD[another_pos[0]][another_pos[1]]=self
			rValue = True
		else:
			board.Board.BOARD[another_pos[0]][another_pos[1]]=self
			rValue = False

		if (another_pos in self.movesC):
			row_color = None
			if(self.player==BLACK):
				row_color = 8
			else:
				row_color =1

			if(another_pos[1]==7):
				board.Board.BOARD[row_color][8].keepPiece.movePlayer(board.Board.BOARD[row_color][8].position,POSITION._make((row_color,6)))
				board.Board.BOARD[row_color][8].movePlayer(board.Board.BOARD[row_color][8].position,POSITION._make((row_color,6)))
				rValue = False
			elif(another_pos[1]==3):
				board.Board.BOARD[row_color][1].keepPiece.movePlayer(board.Board.BOARD[row_color][1].position,POSITION._make((row_color,4)))
				board.Board.BOARD[row_color][1].movePlayer(board.Board.BOARD[row_color][1].position,POSITION._make((row_color,4)))
				rValue = False

		score.updateHash(self,pos,another_pos)

		return rValue



	def updateMoves(self,flag=True):
		
		self.movesC = []
		self.moves = []

		moves = []
		x,y = self.position.x,self.position.y
		#----------------------------------------------------------
		#X_AXIS

		x_,y_ = x+1,y
		if isValid((x_,y_)) and board.Board.CHECK_SQUARES[not self.player][x_][y_]==0:
			if(board.Board.isPieceAt(POSITION._make((x_,y_)))):
				if(board.Board.BOARD[x_][y_].player!=self.player and not isinstance(board.Board.BOARD[x_][y_].player,King)):
					moves.append(POSITION._make((x_,y_)))
				
			else:
				moves.append(POSITION._make((x_,y_)))
			x_+=1


		x_,y_ = x-1,y
		if isValid((x_,y_)) and board.Board.CHECK_SQUARES[not self.player][x_][y_]==0:
			if(board.Board.isPieceAt(POSITION._make((x_,y_)))):
				if(board.Board.BOARD[x_][y_].player!=self.player and not isinstance(board.Board.BOARD[x_][y_].player,King)):
					moves.append(POSITION._make((x_,y_)))
				
			else:
				moves.append(POSITION._make((x_,y_)))
			x_-=1
		#----------------------------------------------------------


		#----------------------------------------------------------
		#Y_AXIS

		x_,y_ = x,y+1
		if isValid((x_,y_)) and board.Board.CHECK_SQUARES[not self.player][x_][y_]==0:
			if(board.Board.isPieceAt(POSITION._make((x_,y_)))):
				if(board.Board.BOARD[x_][y_].player!=self.player and not isinstance(board.Board.BOARD[x_][y_].player,King)):
					moves.append(POSITION._make((x_,y_)))
				
			else:
				moves.append(POSITION._make((x_,y_)))
			y_+=1


		x_,y_ = x,y-1
		if isValid((x_,y_)) and board.Board.CHECK_SQUARES[not self.player][x_][y_]==0:
			if(board.Board.isPieceAt(POSITION._make((x_,y_)))):
				if(board.Board.BOARD[x_][y_].player!=self.player and not isinstance(board.Board.BOARD[x_][y_].player,King)):
					moves.append(POSITION._make((x_,y_)))
				
			else:
				moves.append(POSITION._make((x_,y_)))
			y_-=1
		#----------------------------------------------------------



		#----------------------------------------------------------
		#DIAGONAL

		x_,y_ = x+1,y+1
		if isValid((x_,y_)) and board.Board.CHECK_SQUARES[not self.player][x_][y_]==0:
			if(board.Board.isPieceAt(POSITION._make((x_,y_)))):
				if(board.Board.BOARD[x_][y_].player!=self.player and not isinstance(board.Board.BOARD[x_][y_].player,King)):
					moves.append(POSITION._make((x_,y_)))
				
			else:
				moves.append(POSITION._make((x_,y_)))
			y_+=1
			x_+=1


		x_,y_ = x-1,y-1
		if isValid((x_,y_)) and board.Board.CHECK_SQUARES[not self.player][x_][y_]==0:
			if(board.Board.isPieceAt(POSITION._make((x_,y_)))):
				if(board.Board.BOARD[x_][y_].player!=self.player and not isinstance(board.Board.BOARD[x_][y_].player,King)):
					moves.append(POSITION._make((x_,y_)))
				
			else:
				moves.append(POSITION._make((x_,y_)))
			y_-=1
			x_-=1


		x_,y_ = x+1,y-1
		if isValid((x_,y_)) and board.Board.CHECK_SQUARES[not self.player][x_][y_]==0:
			if(board.Board.isPieceAt(POSITION._make((x_,y_)))):
				if(board.Board.BOARD[x_][y_].player!=self.player and not isinstance(board.Board.BOARD[x_][y_].player,King)):
					moves.append(POSITION._make((x_,y_)))
				
			else:
				moves.append(POSITION._make((x_,y_)))
			y_-=1
			x_+=1


		x_,y_ = x-1,y+1
		if isValid((x_,y_)) and board.Board.CHECK_SQUARES[not self.player][x_][y_]==0:
			if(board.Board.isPieceAt(POSITION._make((x_,y_)))):
				if(board.Board.BOARD[x_][y_].player!=self.player and not isinstance(board.Board.BOARD[x_][y_].player,King)):
					moves.append(POSITION._make((x_,y_)))
				
			else:
				moves.append(POSITION._make((x_,y_)))
			y_+=1
			x_-=1


		if flag==False:
			self.moves = moves

		else:

			preserve = self.position
			for each in moves:
				preserve_piece = board.Board.BOARD[each.x][each.y]

				self.movePlayer(self.position,each)
				
				if(board.Board.checkCheck()==False):
					self.moves.append(each)

				self.movePlayer(self.position,preserve)
				board.Board.BOARD[each.x][each.y] = preserve_piece

		
		#------------------------------------------------------------
		#CASTLING


		x_,y_ = x,y+1
		while isValid((x_,y_)):
			if(board.Board.BOARD[x_][y_]!=None):
				break
			y_+=1
		
		if ( isValid((x_,y_)) and board.Board.BOARD[x_][y_].player==self.player and isinstance(board.Board.BOARD[x_][y_],Rook) ):
			if(self.moved==False and board.Board.BOARD[x_][y_].moved==False):
				self.movesC.append(POSITION._make((x,y+2)))

		x_,y_ = x,y-1
		while isValid((x_,y_)):
			if(board.Board.BOARD[x_][y_]!=None):
				break
			y_-=1
				
		if ( isValid((x_,y_)) and board.Board.BOARD[x_][y_].player==self.player and isinstance(board.Board.BOARD[x_][y_],Rook) ):
			if(self.moved==False and board.Board.BOARD[x_][y_].moved==False):
				self.movesC.append(POSITION._make((x,y-2)))

		self.moves.extend(self.movesC)
		

class Knight(Piece):

	def __init__(self,position,player):

		super().__init__(position,player)


	def updateMoves(self,flag=True):

		
		x,y = self.position.x,self.position.y
		self.moves = []
		moves=[]

		

		x_=x+1
		y_=y+2
		if(isValid((x_,y_))):
			if(board.Board.isPieceAt(POSITION._make((x_,y_)))):
				if(board.Board.BOARD[x_][y_].player!=self.player and not isinstance(board.Board.BOARD[x_][y_].player,King)):
					moves.append(POSITION._make((x_,y_)))
				elif (board.Board.BOARD[x_][y_].player==self.player and not isinstance(board.Board.BOARD[x_][y_].player,King)):
					board.Board.CHECK_SQUARES[self.player][x_][y_]=KNIGHT
			else:
				moves.append(POSITION._make((x_,y_)))

		x_=x+2
		y_=y+1
		if(isValid((x_,y_))):
			if(board.Board.isPieceAt(POSITION._make((x_,y_)))):
				if(board.Board.BOARD[x_][y_].player!=self.player and not isinstance(board.Board.BOARD[x_][y_].player,King)):
					moves.append(POSITION._make((x_,y_)))
				elif (board.Board.BOARD[x_][y_].player==self.player and not isinstance(board.Board.BOARD[x_][y_].player,King)):
					board.Board.CHECK_SQUARES[self.player][x_][y_]=KNIGHT
			else:
				moves.append(POSITION._make((x_,y_)))



		x_=x-1
		y_=y+2
		if(isValid((x_,y_))):
			if(board.Board.isPieceAt(POSITION._make((x_,y_)))):
				if(board.Board.BOARD[x_][y_].player!=self.player and not isinstance(board.Board.BOARD[x_][y_].player,King)):
					moves.append(POSITION._make((x_,y_)))
				elif (board.Board.BOARD[x_][y_].player==self.player and not isinstance(board.Board.BOARD[x_][y_].player,King)):
					board.Board.CHECK_SQUARES[self.player][x_][y_]=KNIGHT
			else:
				moves.append(POSITION._make((x_,y_)))


		x_=x-2
		y_=y+1
		if(isValid((x_,y_))):
			if(board.Board.isPieceAt(POSITION._make((x_,y_)))):
				if(board.Board.BOARD[x_][y_].player!=self.player and not isinstance(board.Board.BOARD[x_][y_].player,King)):
					moves.append(POSITION._make((x_,y_)))
				elif (board.Board.BOARD[x_][y_].player==self.player and not isinstance(board.Board.BOARD[x_][y_].player,King)):
					board.Board.CHECK_SQUARES[self.player][x_][y_]=KNIGHT
			else:
				moves.append(POSITION._make((x_,y_)))


		x_=x+2
		y_=y-1
		if(isValid((x_,y_))):
			if(board.Board.isPieceAt(POSITION._make((x_,y_)))):
				if(board.Board.BOARD[x_][y_].player!=self.player and not isinstance(board.Board.BOARD[x_][y_].player,King)):
					moves.append(POSITION._make((x_,y_)))
				elif (board.Board.BOARD[x_][y_].player==self.player and not isinstance(board.Board.BOARD[x_][y_].player,King)):
					board.Board.CHECK_SQUARES[self.player][x_][y_]=KNIGHT
			else:
				moves.append(POSITION._make((x_,y_)))


		x_=x+1
		y_=y-2
		if(isValid((x_,y_))):
			if(board.Board.isPieceAt(POSITION._make((x_,y_)))):
				if(board.Board.BOARD[x_][y_].player!=self.player and not isinstance(board.Board.BOARD[x_][y_].player,King)):
					moves.append(POSITION._make((x_,y_)))
				elif (board.Board.BOARD[x_][y_].player==self.player and not isinstance(board.Board.BOARD[x_][y_].player,King)):
					board.Board.CHECK_SQUARES[self.player][x_][y_]=KNIGHT
			else:
				moves.append(POSITION._make((x_,y_)))



		x_=x-1
		y_=y-2
		if(isValid((x_,y_))):
			if(board.Board.isPieceAt(POSITION._make((x_,y_)))):
				if(board.Board.BOARD[x_][y_].player!=self.player and not isinstance(board.Board.BOARD[x_][y_].player,King)):
					moves.append(POSITION._make((x_,y_)))
				elif (board.Board.BOARD[x_][y_].player==self.player and not isinstance(board.Board.BOARD[x_][y_].player,King)):
					board.Board.CHECK_SQUARES[self.player][x_][y_]=KNIGHT
			else:
				moves.append(POSITION._make((x_,y_)))


		x_=x-2
		y_=y-1
		if(isValid((x_,y_))):
			if(board.Board.isPieceAt(POSITION._make((x_,y_)))):
				if(board.Board.BOARD[x_][y_].player!=self.player and not isinstance(board.Board.BOARD[x_][y_].player,King)):
					moves.append(POSITION._make((x_,y_)))
				elif (board.Board.BOARD[x_][y_].player==self.player and not isinstance(board.Board.BOARD[x_][y_].player,King)):
					board.Board.CHECK_SQUARES[self.player][x_][y_]=KNIGHT
			else:
				moves.append(POSITION._make((x_,y_)))



		if flag==False:
			self.moves = moves

		else:

			preserve = self.position
			for each in moves:
				preserve_piece = board.Board.BOARD[each.x][each.y]

				self.movePlayer(self.position,each)
				
				if(board.Board.checkCheck()==False):
					self.moves.append(each)

				self.movePlayer(self.position,preserve)
				board.Board.BOARD[each.x][each.y] = preserve_piece

		# self.moves = moves


		
